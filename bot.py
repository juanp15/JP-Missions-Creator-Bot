import os
import discord
import config.devConf as conf # Change to config.conf
from dotenv import load_dotenv
from discord.ext import commands
from services.schedules_service import ScheduledTasks
from config.db import engine
from models.models import Base
from services.translations_service import localization as loc

# Load environment variables
load_dotenv()

# Intents configuration
total_intents = 0

for intent, value in conf.confIntents['intents'].items():
    if value and intent in conf.confIntents['intentValues']:
        total_intents |= conf.confIntents['intentValues'][intent] 

intents = discord.Intents(total_intents)

# Create the bot
bot = commands.Bot(command_prefix=conf.prefix, intents=intents)

scheduled_tasks = ScheduledTasks()

# Load extensions and sync the slash commands
async def load_extensions():
    try:
        await bot.load_extension('commands.createMission')
        await bot.tree.sync()
    except Exception as e:
        print(f"{loc.get("ErrorLoadingExtensions")} {e}")

@bot.event
async def on_ready():
    await load_extensions()
    print(f'Bot {bot.user.name} {loc.get("BotReady")}')

    # Create the database schema
    Base.metadata.create_all(engine)

    # Start scheduled tasks when the bot is ready
    scheduled_tasks.start()

@bot.event
async def on_disconnect():
    # Stop scheduled tasks when the bot disconnects
    scheduled_tasks.stop()

bot.run(os.getenv("BOT_TOKEN"))
