import asyncio
import discord
from discord.ext import commands
import api


admins = [609454099427229736]


class adminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clearCash(self, ctx) -> None:
        if ctx.author.id not in admins:
            await ctx.send("You are not allowed to execute this")
            return
        self.bot.clear()
        await ctx.send("Cash geleert")

    @commands.command()
    async def sync(self, ctx) -> None:
        if ctx.author.id not in admins:
            await ctx.send("You are not allowed to execute this")
            return
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"{len(fmt)} Befehle wurden gesynced.")



async def setup(bot):
    await bot.add_cog(adminCog(bot))