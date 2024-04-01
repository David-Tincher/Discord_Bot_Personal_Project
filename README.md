# Python Discord Music Bot(with extra funcitons)

## A Discord Bot developed in Python that can play music from Youtube aswell as some other basic functions. 

This project was made as a PET project because I was interested in developing a Music Bot for Discord because most of the mainstream Bots have been taken down over the years. To use this bot you will need to install some dependencies that I will list below. Once everything has been set up you can add your own Discord Bot to your server to play any music (from youtube) in your voice channels. All of the commands can be used in text channels by typing a `!` before the commands. If you are ever confused on what commands are available just type `!functions` in a text channel. 

## Dependencies
- Discord Developer Portal - https://discord.com/developers/docs/intro
- An IDE of your choice - https://code.visualstudio.com/download - Download for Visual Studio Code
- Most Recent Version of Python - https://www.python.org/downloads/ 
- Python Libraries - Discord, VideosSearch, YoutubeDL, and asyncio - Use `pip install (name_of_lib)` in terminal on IDE to install
- FFMPEG - https://ffmpeg.org/download.html 
- Dad Joke Generator (optional) - https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes 
- Helpful Youtube PlayList For Discord Bot Basics - https://www.youtube.com/watch?v=cCiqcu2NP8I&list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP&pp=iAQB

## How to set it up 
The first thing you'll need to do to use this bot is to go to the Discord Developer Portal and create an applicaiton for your own bot. Once you have gotten access to your bot you will need to find its API key and save it somewhere where you won't lose it. Also do not share this key with anyone else as then they could manipulate your bot. Once this is completed you'll need to install both an IDE of your choice, I used visual studio code, and Python. When installing Python make sure you add it to your PATH variable if you are on Windows. After this download all of the .py files from this repository and open them in your IDE. Then you will need to install the Python libaries that are used. You can do this by typing `pip install (name_of_lib)`, for example `pip install Discord` inside the terminal section at the bottom of your IDE. After this you will need to install FFMPEG and add it to the PATH variable on your machine aswell. Now the final step is to put the aforementioned discord bot's API key into your code. You will need to replace the `BotToken` in `await bot.start(BotToken)` on line 28 of the `Main.py` file with your discord API key. If you would like to use the `!dadjoke` function aswell you will need to follow the link I attached above and get the API key for it. Once this has been obtained replace the `JokeToken` in `"X-RapidAPI-Key": JokeToken` on line 81 of the `fun_cog.py` file. 

## Future Functions
The next thing I would like to add to this Bot is a blackjack function that allows users to play against the Bot. This function would be a simple GUI setup inside of the text channel that its summoned in. I am also considering adding a global user balance function to this as well so you and friends can compare each others scores. 




Developed by: David Tincher 