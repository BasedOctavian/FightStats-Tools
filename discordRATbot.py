import discord
from discord.ext import commands

TOKEN = "token"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)



@client.event
async def on_ready():
    print("Connected!")
    
    

client.run(TOKEN)
