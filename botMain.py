import discord
from discord.ext import commands
import asyncio
from textblob import TextBlob
from os import environ

Client = discord.Client()
bot = commands.Bot(command_prefix = "s.")
await bot.change_presence(game=discord.Game(name=="Say s.text"))

@bot.event
async def on_ready():
    print ("Bot is online")
    print ("Username: ",bot.user.name)
    print ("*********************")

@bot.command()
async def text(*arg):
    blob = TextBlob(" ".join(arg))
    sent = blob.sentiment.polarity
    sub = blob.sentiment.subjectivity
    if(sent < -0.5):
        await  bot.say("The statement is negative")
    elif(sent < -0.1):
        await  bot.say("The statement is slightly negative")
    elif(sent > -0.1 and sent < 0.1):
        await  bot.say("The statement neutral")
    elif(sent< 0.5):
        await  bot.say("The statement is slightly positive")
    elif(sent <= 1):
        await  bot.say("The statement is positive")
    if(sub > 0.8):
        await  bot.say("It is subjective")
    elif(sub > 0.4):
        await  bot.say("It maybe subjective")



bot.run(environ.get("DISCORD_TOKEN"))
