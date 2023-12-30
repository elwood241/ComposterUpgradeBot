import api
import discord
from discord.ext import commands
import os 
from dotenv import dotenv_values
import asyncio
import contextlib
import sys
import logging

config = dotenv_values(".env")





# Custom filter to exclude the specific warning message
class DiscordGatewayFilter(logging.Filter):
    def filter(self, record):
        return 'Shard ID None heartbeat blocked' not in record.getMessage()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
script_logger = logging.getLogger(__name__)
script_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.addFilter(DiscordGatewayFilter())
script_logger.addHandler(handler)

# Define a custom filter for discord.py warnings
class DiscordWarningsFilter(logging.Filter):
    def filter(self, record):
        return 'Shard ID None heartbeat blocked' not in record.getMessage()

# Apply the custom filter to the discord.py logger
discord_logger = logging.getLogger('discord.gateway')
discord_logger.addFilter(DiscordWarningsFilter())

# Your bot code goes here
bot = commands.Bot("admin.", intents=discord.Intents.all(), application_id=config["APPLICATION_ID"])

@bot.event
async def on_ready():
    script_logger.info(f'We have logged in as {bot.user}')






async def loadextension(extensionname):
    extensionname = f"extensions.{extensionname}"
    try:
        await bot.load_extension(extensionname)
        print(f"{extensionname} loaded!")
    except Exception as e:
        print(f"Failed to load extension {extensionname}")
        raise
    
    
    
if __name__ == "__main__":
    api.createTables()

    print(discord.__version__)
    for extension in os.listdir(os.fsencode("extensions")):
        if os.fsdecode(extension).endswith(".py"):
            extension = os.fsdecode(extension).replace(".py", "")
            asyncio.run(loadextension(extension))
    

    
bot.run(config["TOKEN"])