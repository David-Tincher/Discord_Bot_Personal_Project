import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        self.help_message = """
```
Help:
!functions - displays all available commands

General commands:
!dadjoke - tells a (funny) dad joke
!blackjack/bj - play blackjack (In Progress)
!dance - party time
!goodbye - says goodbye(pero en espanol)

Music commands:
!p <Keywords> - searches for song then plays it in your current VC
!q - displays the current songs in queue
!skip - skips the current song
!clear - clears the queue of all songs
!kick - Removes the bot from the VC
!pause - pauses the current song or resumes if already paused
!resume - resumes the current song 
```
"""

        self.text_channel_text = []

    async def setup(self):
            await self.add_cog(help_cog(self))
    
    @commands.command(name="functions", help ="Displays all available commands")
    async def functions(self,ctx):
        await ctx.send(self.help_message)