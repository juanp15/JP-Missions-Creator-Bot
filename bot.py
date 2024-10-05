import os
import discord
import config.conf as conf
from dotenv import load_dotenv
from discord.ext import commands

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

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} has started successfully.')

bot.run(os.getenv("BOT_TOKEN"))
