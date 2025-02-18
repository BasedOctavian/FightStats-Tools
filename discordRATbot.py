import discord
from discord.ext import commands

TOKEN = "MTA3MjI3OTYyNjU1NjExNzEwMw.GhPV42.c-jMB_4FQT8SecMbMnwai3fM6YU2IP967zsPfg"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)



@client.event
async def on_ready():
    print("Connected!")
    
    

client.run(TOKEN)
