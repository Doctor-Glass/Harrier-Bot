# Basic includes
import os
import discord
# Network includes
from dotenv import load_dotenv
# Command includes
import roulette      # roulette.py, implements the !roulette command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set intents
bot_intents = discord.Intents.default()

bot_intents.typing = True
bot_intents.messages = True
bot_intents.message_content = True
bot_intents.dm_messages = True
bot_intents.dm_typing = True

client = discord.Client(intents = bot_intents)

# on_ready() is called when the bot is set up and ready to go
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# on_member_join is called when a member joins the server
@client.event
async def on_member_join(member):
    if member == client.user:
        return
    
    await member.create_dm()
    await member.dm_channel.send(
        f"Greetings, {member.name} and welcome to Harrier Dynamics, the Caldari State's number one defense contractor! To get set up and authed in our Discord server, go to [seat.h-dyn.net](https://seat.h-dyn.net) and log in with your character, then click Discord on the left and \"Join Server\". We hope you enjoy your stay here."
    )

# on_message() is called whenever a message is sent in a chanmnel that the bot has access to
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    match message.content:
        # !test
        case "!test":
            response = "**We remain Caldari, *no matter the cost***"

            await message.channel.send(response)
        # !roulette
        case "!roulette":
            response = roulette.spin()

            await message.channel.send(response)
        # default
        case _:
            return


client.run(TOKEN)