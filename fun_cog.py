import discord
import random
from discord.ext import commands

from APIkeys import *
import requests

class fun_cog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.goobye_message = "Adios, Amigo"
        self.dance_message = ":man_dancing: :mirror_ball: :dancer:"
    async def setup(self):
            await self.add_cog(fun_cog(self))


#In Progress
#    @self.event 
#    async def on_member_join(member):
#        url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"
#        headers = {
#            "X-RapidAPI-Key": JokeToken,
#            "X-RapidAPI-Host": "dad-jokes-by-api-ninjas.p.rapidapi.com"
#        }
#        response = requests.get(url, headers=headers)
#        joke = response.json()[0].get('joke')
#        channel = self.get_channel(welcomeChannel_ID)
#
#        await channel.send("Welcome to the server " , member , "\n" , joke)
#        
#    @self.event 
#    async def on_member_remove(member):
#        channel = self.get_channel(welcomeChannel_ID)
#        await channel.send("@" , member , "Clearly didn't like it here")



    #Commands
    @commands.command(name="goodbye", help ="Says goodbye (pero en espanol)")
    async def goodbye(self, ctx):
        await ctx.send(self.goobye_message)

    @commands.command(name="dadjoke", help ="Tells a dadjoke")
    async def dadjoke(self, ctx):
        joke = self.getDadJoke()
        await ctx.send(joke)

    @commands.command(name="dance", help ="Makes me dance")
    async def dance(self, ctx):
        await ctx.send(self.dance_message)

    @commands.command(name="blackjack",aliases= ["bj"], help ="Gamble")
    async def blackjack(self, ctx):
        d1Card = self.generateCards()
        p1Card = self.generateCards()
        p2Card = self.generateCards()
        embed = discord.Embed(title="BlackJack", colour = 0xFF5733)
        #Trying to implement this made the whole function not work 
        #embed.set_author(name= ctx.author.display_name, icon_url=ctx.display_avatar)
        embed.add_field(name="Type `hit` to draw another card or `stand` to continue", value ="", inline= False )
        embed.add_field(name= "Your Hand                ", value = p1Card[0] +  " and "  + p2Card[0], inline = True)
        embed.add_field(name= "Dealer's Hand", value= d1Card[0] + " and :question:", inline = True)
        embed.add_field(name ="", value="", inline= False)
        embed.add_field(name= "Value: " + str(p1Card[1] + p2Card[1]), value = "", inline= True )
        embed.add_field(name= "Value: " + str(d1Card[1]), value = "", inline= True)
        embed.set_footer(text="{}".format(ctx.author.display_name) + " is currently playing")
        await ctx.send(embed=embed)
        
    #In prog
    @commands.Cog.listener()
    async def on_message(self, message):
        if "stand" in message.content:
            await message.channel.send('You stood')
        elif "hit" in message.content:
            await message.channel.send('Ouch!')
    
    #Function to generate a dadjoke
    def getDadJoke(self):
        url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"
        headers = {
            "X-RapidAPI-Key": JokeToken,
            "X-RapidAPI-Host": "dad-jokes-by-api-ninjas.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        joke = response.json()[0].get('joke')
        return joke
    
    #Generates cards 
    def generateCards(self):
        cardVal = random.randint(1,14)
        cardType = str(cardVal)
    
        if cardVal == 11 :
            cardType = ':regional_indicator_j: :hearts:'
            cardVal = 10
        elif cardVal == 12:
            cardType = ':regional_indicator_q: :hearts:'
            cardVal = 10
        elif cardVal == 13:
            cardType = ':regional_indicator_k: :hearts:' 
            cardVal = 10
        elif cardVal == 14:
            cardType = ':regional_indicator_a: :hearts:'
            cardVal = 11

        output = cardType
        return output, cardVal