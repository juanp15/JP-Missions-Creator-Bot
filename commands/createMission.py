import discord
import config.devConf as conf # Change to config.conf
from discord.ext import commands
from services.translationsService import localization as loc
from datetime import datetime

async def setup(bot: commands.Bot):
    @bot.tree.command(name="create_mission", description=loc.get("DescCreateMissionCommand"))
    async def createMission(interaction: discord.Interaction, title: str, description: str, embed_color: str, mission_date: str, datetime_start: str, datetime_end: str, images_descriptions: str = ""):
        # Message ID of the images embeds
        imagesEmbedsIDs = []

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

            if not await checkDates_Times(interaction, mission_date, datetime_start, datetime_end):
                return

            # Convert the dates to timestamp
            timestampDate = int(datetime.strptime(mission_date, "%Y-%m-%d").timestamp())
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
                        raise Exception(loc.get("InvalidImageURL"))

                    imageEembed = discord.Embed(color = color)
                    imageEembed.set_image(url=imageURLs[i])
                    imageEembed.description = f"**{descriptions[i]}**"
                    imageMessage = await interaction.channel.send(embed=imageEembed)

                    imagesEmbedsIDs.append(imageMessage.id)

            # Create the mission embed
            
            
        except Exception as e:
            # Delete the images embeds if they were created and any error occurred
            if len(imagesEmbedsIDs) > 0:
                for messageID in imagesEmbedsIDs:
                    message = await interaction.channel.fetch_message(messageID)
                    await message.delete

            await interaction.response.send_message(f"{loc.get("ErrorCreatingMission")} {e}", ephemeral=True, delete_after=20)


# Check if the user has the necessary role to create a mission, if the command was executed in the allowed server and if the number of images and descriptions is correct
async def checkGuild_Role_Images(interaction, imagesDescriptions):
    # Check if the command was executed in the allowed server
    if interaction.guild.id != conf.allowedGuildId:
        await interaction.response.send_message(loc.get("NotAllowedServer"), ephemeral=True, delete_after=10)
        return

    # Check if the user is allowed to create a mission
    if discord.utils.get(interaction.user.roles, id=conf.editorRoleId) is None:
        await interaction.response.send_message(loc.get("NotAllowedCreateMissions"), ephemeral=True, delete_after=10)
        return
    
    # Check if exceeds the maximum number of images (10 images and 10 descriptions) or is less than 1
    if (len(imagesDescriptions) > 20):
        await interaction.response.send_message(loc.get("ErrorMaxImages"), ephemeral=True, delete_after=10)
        return
    
    # Check if the number of images and descriptions is even
    if  len(imagesDescriptions) != 0 or len(imagesDescriptions) % 2 != 0:
        await interaction.response.send_message(loc.get("ErrorImagesDescriptions"), ephemeral=True, delete_after=10)
        return
    
    return True

# Check if the date and datetimes are correct
async def checkDates_Times(interaction, mission_date, datetime_start, datetime_end):
    try:
        missionDate = datetime.strptime(mission_date, "%Y-%m-%d")
        datetimeStart = datetime.strptime(datetime_start, "%Y-%m-%d %H:%M")
        datetimeEnd = datetime.strptime(datetime_end, "%Y-%m-%d %H:%M")
        
        if missionDate < datetime.now():
            await interaction.response.send_message(loc.get("InvalidMissionDate"), ephemeral=True, delete_after=10)
            return False
        
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
