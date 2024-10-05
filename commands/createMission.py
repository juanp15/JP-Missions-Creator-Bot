import discord
from discord.ext import commands

async def setup(bot: commands.Bot):
    @bot.tree.command(name="create_mission", description="Creates a new mission.")
    async def create_mission(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.name}!", ephemeral=True, delete_after=5)
