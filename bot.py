devConf = True # Use False

import os
import discord
if devConf:
    import config.devConf as conf
else:
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
    await bot.load_extension('commands.createMission')
    await bot.tree.sync()
    print(f'Bot {bot.user.name} has started successfully.')

bot.run(os.getenv("BOT_TOKEN"))
