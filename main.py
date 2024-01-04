import api
import discord
from discord.ext import commands
import os 
from dotenv import dotenv_values
import asyncio
import logging

config = dotenv_values(".env")



bot = commands.Bot("admin.", intents=discord.Intents.all(), application_id=config["APPLICATION_ID"])

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')






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