from discord.ext import commands
import API.secret as secret
import os
import discord

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='Wordle ', intents=intents)


def loadModules():
    # Change "cogs" to your folder name
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            bot.load_extension(f"modules.{filename[:-3]}")


loadModules()


bot.run(secret.WORDLE_BOT)
