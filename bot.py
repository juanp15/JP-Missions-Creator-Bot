import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from services.schedules_service import ScheduledTasks
from config.db import engine
from models.models import Base

# Load environment variables
load_dotenv()

# Load configuration
devConf = True # Use False
if devConf:
    import config.devConf as conf
else:
    import config.conf as conf

# Intents configuration
total_intents = 0

for intent, value in conf.confIntents['intents'].items():
    if value and intent in conf.confIntents['intentValues']:
        total_intents |= conf.confIntents['intentValues'][intent] 

intents = discord.Intents(total_intents)

# Create the bot
bot = commands.Bot(command_prefix=conf.prefix, intents=intents)

scheduled_tasks = ScheduledTasks()

@bot.event
async def on_ready():
    await bot.load_extension('commands.createMission')
    await bot.tree.sync()
    print(f'Bot {bot.user.name} has started successfully.')

    # Create the database schema
    Base.metadata.create_all(engine)

    # Start scheduled tasks when the bot is ready
    scheduled_tasks.start()

@bot.event
async def on_disconnect():
    # Stop scheduled tasks when the bot disconnects
    scheduled_tasks.stop()

bot.run(os.getenv("BOT_TOKEN"))
