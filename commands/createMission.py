import discord
import config.devConf as conf # Change to config.conf
from discord.ext import commands
from services.translations_service import localization as loc

async def setup(bot: commands.Bot):
    @bot.tree.command(name="create_mission", description=loc.get("DescCreateMissionCommand"))
    async def create_mission(interaction: discord.Interaction):
        try:
            # Check if the command was executed in the allowed server
            if interaction.guild.id != conf.allowedGuildId:
                await interaction.response.send_message(loc.get("NotAllowedServer"), ephemeral=True, delete_after=10)
                return

            # Check if the user is allowed to create a mission
            if discord.utils.get(interaction.user.roles, id=conf.editorRoleId) is None:
                await interaction.response.send_message(loc.get("NotAllowedCreateMissions"), ephemeral=True, delete_after=10)
                return
            
        except Exception as e:
            await interaction.response.send_message(f"{loc.get("ErrorCreatingMission")} {e}", ephemeral=True)
