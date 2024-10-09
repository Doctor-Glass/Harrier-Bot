# Basic includes
import os
import discord
from discord.ext import commands
# Network includes
from dotenv import load_dotenv
# Command includes
import roulette         # roulette.py, implements the !roulette command
import gettime          # gettime.py, implements the !time command
import pricecheck       # pricecheck.py, implements the !pricecheck command
import killfeed         # killfeed.py, implements the !killfeed command and its options

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
    arguments = ", ".join(args)
    response = gettime.convert_time(args)

    await ctx.send(response)

# error overload for the !time function, used to allow users to just call !time and get the current EVE server time
@cmd_time.error
async def cmd_time_error(ctx, error):
    response = gettime.convert_time(["ET"])
    await ctx.send(response)

# !pricecheck command, provides price checking functionality using the Janice API
@bot.command(name="pricecheck")
async def cmd_pricecheck(ctx, *args):
    arguments = ", ".join(args)
    response = pricecheck.check(args)

    await ctx.send(response)

@cmd_pricecheck.error
async def cmd_pricecheck_error(ctx, error):
    print(error)
    response = """
    **Usage:**
    **\!pricecheck [market (optional)] [item] [qty (optional)] ...**

    **[market (optional)]:** market to check, default is "Jita". Options are "Jita", "Amarr", "Dodixie", "Rens", "Hek", "MJ-SF9", "R10-GN", or "NPC"
    **[item]:** item(s) to check, multiple can be specified with or without quantities. Items with multiple words must be wrapped in quote marks.
    **[qty (optional)]:** optional quantity for the preceding item
    """

    await ctx.send(response)

@bot.command(name="killfeed")
async def cmd_killfeed(ctx, *args):
    arguments = ", ".join(args)

    response = ""
    
    match arguments[0]:
        case "create":
            response = killfeed.create(arguments)
        case "edit":
            response = killfeed.edit(arguments)
        case "remove":
            response = killfeed.remove(arguments)
        case _:
            response = killfeed.create(arguments)
    
    await ctx.send(response)

bot.run(TOKEN)