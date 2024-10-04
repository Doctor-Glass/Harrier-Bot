# Basic includes
import os
import discord
from discord.ext import commands
# Network includes
from dotenv import load_dotenv
# Command includes
import roulette      # roulette.py, implements the !roulette command
import gettime       # gettime.py, implements the !time command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set intents
bot_intents = discord.Intents.default()

bot_intents.typing = True
bot_intents.messages = True
bot_intents.message_content = True
bot_intents.dm_messages = True
bot_intents.dm_typing = True

bot = commands.Bot(command_prefix="!", intents=bot_intents)

# on_ready() is called when the bot is set up and ready to go
@bot.event
async def on_ready():
    print(f'Harrier Bot has connected to Discord!')

# on_member_join is called when a member joins the server
@bot.event
async def on_member_join(member):
    if member == bot.user:
        return
    
    await member.create_dm()
    await member.dm_channel.send(
        f"Greetings, {member.name} and welcome to Harrier Dynamics, the Caldari State's number one defense contractor! To get set up and authed in our Discord server, go to [seat.h-dyn.net](https://seat.h-dyn.net) and log in with your character, then click Discord on the left and \"Join Server\". We hope you enjoy your stay here."
    )

# !test command, used to test if the bot is functional and provide some entertaining propaganda        
@bot.command(name="test")
async def cmd_test(ctx):
    response = "**We remain Caldari, *no matter the cost!***"

    await ctx.send(response)

# !roulette command, performs the Fit Roulette
@bot.command(name="roulette")
async def cmd_roulette(ctx):
    response = roulette.spin()

    await ctx.send(response)

# !time command, provides options for getting the time and for converting it to different timezones
@bot.command(name="time")
async def cmd_time(ctx, *args):
    print(args)

    arguments = ", ".join(args)
    response = gettime.convert_time(args)

    await ctx.send(response)

# error overload for the !time function, used to allow users to just call !time and get the current EVE server time
@cmd_time.error
async def cmd_time_error(ctx, error):
    response = gettime.convert_time(["ET"])
    await ctx.send(response)


bot.run(TOKEN)