import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# on_ready() is called when the bot is set up and ready to go
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# on_member_join is called when a member joins the server
@client.event
async def on_member_join(member):
    return

client.run(TOKEN)