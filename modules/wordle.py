from discord.ext import commands
import discord
import os
from datetime import datetime, date

channel = 798356926605033495


async def printWordle(self, ctx):
    discordChannel = self.bot.get_channel(channel)
    somethingOrOther = list[discordChannel.history(limit=10)]
    print(somethingOrOther)


class Wordle(commands.Cog, name="Wordle"):
    wordleDay = date(2021, 6, 19) - datetime.today().date()

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wordles", aliases=[])
    @commands.has_permissions(administrator=True)
    async def _ping(self, ctx: commands.Context):
        await printWordle(self, ctx)


def setup(bot):
    print("Wordle Cog Loaded")
    bot.add_cog(Wordle(bot))


def teardown(bot):
    print("Wordle Cog Unloaded")
