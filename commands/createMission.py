import discord
import config.devConf as conf # Change to config.conf
from discord.ext import commands
from discord.ui import Select, Button, View
from services.translationsService import localization as loc
from datetime import datetime

class InvalidImageURLException(Exception):
    pass

async def setup(bot: commands.Bot):
    @bot.tree.command(name="create_mission", description=loc.get("DescCreateMissionCommand"))
    async def createMission(interaction: discord.Interaction, title: str, description: str, embed_color: str, datetime_start: str, datetime_end: str, images_descriptions: str = ""):
        # Message ID of the images embeds
        imagesEmbedsIDs = []
        emojis = conf.emojis

        try:
            imagesDescriptionsList = []

            if len(images_descriptions) > 0:
                imagesDescriptionsList = images_descriptions.split(";")

            if not await checkGuild_Role_Images(interaction, imagesDescriptionsList):
                return
            
            # Check if the embed color is a valid hexadecimal color
            try:
                color = discord.Color(int(embed_color, 16))
            except Exception:
                await interaction.response.send_message(loc.get("InvalidColor"), ephemeral=True, delete_after=10)
                return
            
            # If has images and descriptions, separate them into two lists
            if len(imagesDescriptionsList) > 1:
                imageURLs = imagesDescriptionsList[::2]
                descriptions = imagesDescriptionsList[1::2]

            if not await checkDates_Times(interaction, datetime_start, datetime_end):
                return

            # Convert the dates to timestamp
            timestampStart = int(datetime.strptime(datetime_start, "%Y-%m-%d %H:%M").timestamp())
            timestampEnd = int(datetime.strptime(datetime_end, "%Y-%m-%d %H:%M").timestamp())

            # Calculate the time remaining for the mission start
            now = datetime.now()
            timeRemaining = datetime.strptime(datetime_start, "%Y-%m-%d %H:%M") - now

            # Format the enters in the description
            description = description.replace("\\n", "\n")

            # Create the images embeds
            if len(imagesDescriptionsList) > 1:
                for i, imageURL in enumerate(imageURLs):
                    if not imageURL.startswith("http") or not imageURL.startswith("https"):
                        raise InvalidImageURLException(loc.get("InvalidImageURL"))

                    imageEembed = discord.Embed(color = color)
                    imageEembed.set_image(url=imageURLs[i])
                    imageEembed.description = f"**{descriptions[i]}**"
                    imageMessage = await interaction.channel.send(embed=imageEembed)

                    imagesEmbedsIDs.append(imageMessage.id)

            # Create the mission embed
            embed = discord.Embed(
                title=title,
                description=description,
                color=color
            )

            embed.set_thumbnail(url=conf.thumbnail)
            embed.add_field(name="\n", value="", inline=False)
            embed.add_field(name=emojis["Inscriptions"] + " 0", value="", inline=False)
            embed.add_field(name=emojis["Date"] + " " + f"<t:{timestampStart}:D>", value="", inline=True)
            embed.add_field(name=emojis["StartFinish"] + " " + f"<t:{timestampStart}:t>" + " - " + f"<t:{timestampEnd}:t>", value="", inline=True)

            if timeRemaining.total_seconds() > 0:
                embed.add_field(name=emojis["TimeToStart"] + " " + f"<t:{timestampStart}:R>", value="", inline=True)
            else:
                embed.add_field(name=emojis["TimeToStart"] + " " + loc.get("MissionStarted"), value="", inline=True)

            embed.add_field(name="\n", value="", inline=False)
            
            # Add the roles to the embed
            for role in ["CAP", "TASMO", "STRIKE", "CAS", "SEAD", "RIO", "PILOT", "CPG"]:
                embed.add_field(name=emojis[role] + f" {role} 0", value=loc.get("WithoutParticipants"), inline=True)

            embed.add_field(name="\n", value="", inline=False)
            embed.add_field(name=conf.missionsTextVoiceChannel, value=conf.usersRoleId, inline=False)
            embed.add_field(name="\n", value="", inline=False)
            
            embed.set_footer(text="JP Missions Creator")

            await interaction.channel.send(embed=embed)

            # Select menu to select the roles
            selectRole = Select(
                placeholder="Seleccione su clase...",
                options=[discord.SelectOption(label="CAP", description="Combat Air Patrol (CAP)", emoji=emojis["CAP"]),
                        discord.SelectOption(label="TASMO", description="Maritime Strike (TASMO)", emoji=emojis["TASMO"]),
                        discord.SelectOption(label="STRIKE", description="Ground Attack (STRIKE)", emoji=emojis["STRIKE"]),
                        discord.SelectOption(label="CAS", description="Close Air Support (CAS)", emoji=emojis["CAS"]),
                        discord.SelectOption(label="SEAD", description="Suppression of Enemy Air Defenses (SEAD)", emoji=emojis["SEAD"]),
                        discord.SelectOption(label="RIO", description="Radar Intercept Officer (RIO)", emoji=emojis["RIO"]),
                        discord.SelectOption(label="PILOT", description="Helicopter Pilot (PILOT)", emoji=emojis["PILOT"]),
                        discord.SelectOption(label="CPG", description="Co-Pilot Gunner (CPG)", emoji=emojis["CPG"])],
                custom_id="select_role"
            )

            # Select menu to select the aircraft
            selectAircraft = Select(
                placeholder=loc.get("SelectAircraft"),
                options=[discord.SelectOption(label=loc.get("SelectRoleFirst"))],
                custom_id="select_aircraft"
            )

            await interaction.response.send_message(loc.get("MissionCreated"), ephemeral=True, delete_after=10)

        # Exceptions
        except InvalidImageURLException as e:
            # Delete the images embeds if they were created and any error occurred
            if len(imagesEmbedsIDs) > 0:
                await deleteImagesEmbeds(interaction, imagesEmbedsIDs)
                imageEembedsIDs = []

            await interaction.response.send_message(f"{loc.get("InvalidImageURL")}", ephemeral=True, delete_after=20)
            return

        except Exception as e:
            # Delete the images embeds if they were created and any error occurred
            if len(imagesEmbedsIDs) > 0:
                await deleteImagesEmbeds(interaction, imagesEmbedsIDs)
                imageEembedsIDs = []

            await interaction.response.send_message(f"{loc.get("ErrorCreatingMission")} {e}", ephemeral=True, delete_after=20)
            return

async def deleteImagesEmbeds(interaction, imagesEmbedsIDs_):
    for messageID in imagesEmbedsIDs_:
        message = await interaction.channel.fetch_message(messageID)
        await message.delete()
        imagesEmbedsIDs_.remove(messageID)

# Check if the user has the necessary role to create a mission, if the command was executed in the allowed server and if the number of images and descriptions is correct
async def checkGuild_Role_Images(interaction, imagesDescriptionsList):
    # Check if the command was executed in the allowed server
    if interaction.guild.id != conf.allowedGuildId:
        await interaction.response.send_message(loc.get("NotAllowedServer"), ephemeral=True, delete_after=10)
        return

    # Check if the user is allowed to create a mission
    if discord.utils.get(interaction.user.roles, id=conf.editorRoleId) is None:
        await interaction.response.send_message(loc.get("NotAllowedCreateMissions"), ephemeral=True, delete_after=10)
        return
    
    # Check if exceeds the maximum number of images (10 images and 10 descriptions) or is less than 1
    if (len(imagesDescriptionsList) > 20):
        await interaction.response.send_message(loc.get("ErrorMaxImages"), ephemeral=True, delete_after=10)
        return
    
    # Check if the number of images and descriptions is even
    if  len(imagesDescriptionsList) % 2 != 0:
        await interaction.response.send_message(loc.get("ErrorImagesDescriptions"), ephemeral=True, delete_after=10)
        return
    
    return True

# Check if the date and datetimes are correct
async def checkDates_Times(interaction, datetime_start, datetime_end):
    try:
        datetimeStart = datetime.strptime(datetime_start, "%Y-%m-%d %H:%M")
        datetimeEnd = datetime.strptime(datetime_end, "%Y-%m-%d %H:%M")
        
        if datetimeStart < datetime.now():
            await interaction.response.send_message(loc.get("InvalidMissionStartDate"), ephemeral=True, delete_after=10)
            return False
        
        if datetimeEnd < datetime.now():
            await interaction.response.send_message(loc.get("InvalidMissionEndDate"), ephemeral=True, delete_after=10)
            return False
        
        if datetimeStart > datetimeEnd:
            await interaction.response.send_message(loc.get("InvalidMissionStartEnd"), ephemeral=True, delete_after=10)
            return False

        return True
    
    except ValueError:
        await interaction.response.send_message(loc.get("ErrorDateTime"), ephemeral=True, delete_after=20)
        return
