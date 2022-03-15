from discord.ext import commands
import discord
import os
from datetime import datetime, date
import time

channel = 940348551127523368
wordleDay = (datetime.today().date() - date(2021, 6, 19)).days

async def printWordle(self):
    discordChannel = self.bot.get_channel(channel)
    winners = {"highscore" : None, "winners" : []}
    async for message in discordChannel.history(limit = 100):
        if "Wordle" in message.content and "/6" in message.content and str(wordleDay) in message.content:
            score = message.content[11]
            if winners["highscore"] == None:
                winners["highscore"] = score
            if score == winners["highscore"]:
                winners["winners"].append(message.author.id)
            elif score < winners["highscore"]:
                winners["winners"] = [message.author.id]
                winners["highscore"] = score
    return winners


async def timer(self, ctx):
    while True:
        now = datetime.now()
        if now.hour == 23 and now.minute == 59:
            await sendEmbedWordle(self, ctx)
        time.sleep(60)
        
        
            
async def sendEmbedWordle(self, ctx):
        winners = await printWordle(self)
        embed = discord.Embed(title = f'Wordle Day {wordleDay}', url = f'https://www.nytimes.com/games/wordle/index.html', color = 0x14E400)
        stringOfWinners = ""
        for winner in winners['winners']:
            stringOfWinners += f"<@{winner}>" + " "
        stringOfWinners = stringOfWinners[:-1]
        embed.add_field(name = "Winners", value = stringOfWinners, inline=True)
        embed.add_field(name = "Score", value = winners['highscore'], inline = True)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed = embed)


class Wordle(commands.Cog, name="Wordle"):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="startTimer", aliases=[])
    @commands.has_permissions(administrator=True)
    async def _startTimer(self, ctx: commands.Context):
        await ctx.send("Timer Started")
        await timer(self, ctx)





def setup(bot):
    print("Wordle Cog Loaded")
    bot.add_cog(Wordle(bot))


def teardown(bot):
    print("Wordle Cog Unloaded")
