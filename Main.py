#imports required discord info 
import discord
from discord.ext import commands
import os, asyncio

#imports various useful API Keys
from APIkeys import *

from help_cog import help_cog
from music_cog import music_cog
from fun_cog import fun_cog
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '!', intents = intents)
#doesnt actually remove help function- idk why
bot.remove_command('help')


#Main
async def main():
    async with bot:
        print("I'm Ready!")
        print("---------------------------")
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.add_cog(fun_cog(bot))
        await bot.start(BotToken)
        


asyncio.run(main())