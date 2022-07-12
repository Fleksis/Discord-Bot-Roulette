import discord
from discord import Spotify
from discord.ext import commands
from random import randint
import pytz
import os
from dotenv import load_dotenv
from function_db import *
import datetime
from datetime import timedelta
from time import sleep
import asyncio

load_dotenv()

client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    get_status()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    get_users()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith('!'):
        return
    set_user(message.author.id, message.author)
    await client.process_commands(message)

Roulette = [{"number": 0, "color_sym": "🟢", "color": "green"},
            {"number": 1, "color_sym": "🔴", "color": "red"},
            {"number": 2, "color_sym": "⚫", "color": "black"},
            {"number": 3, "color_sym": "🔴", "color": "red"},
            {"number": 4, "color_sym": "⚫", "color": "black"},
            {"number": 5, "color_sym": "🔴", "color": "red"},
            {"number": 6, "color_sym": "⚫", "color": "black"},
            {"number": 7, "color_sym": "🔴", "color": "red"},
            {"number": 8, "color_sym": "⚫", "color": "black"},
            {"number": 9, "color_sym": "🔴", "color": "red"},
            {"number": 10, "color_sym": "⚫", "color": "black"},
            {"number": 11, "color_sym": "⚫", "color": "black"},
            {"number": 12, "color_sym": "🔴", "color": "red"},
            {"number": 13, "color_sym": "⚫", "color": "black"},
            {"number": 14, "color_sym": "🔴", "color": "red"},
            {"number": 15, "color_sym": "⚫", "color": "black"},
            {"number": 16, "color_sym": "🔴", "color": "red"},
            {"number": 17, "color_sym": "⚫", "color": "black"},
            {"number": 18, "color_sym": "🔴", "color": "red"},
            {"number": 19, "color_sym": "🔴", "color": "red"},
            {"number": 20, "color_sym": "⚫", "color": "black"},
            {"number": 21, "color_sym": "🔴", "color": "red"},
            {"number": 22, "color_sym": "⚫", "color": "black"},
            {"number": 23, "color_sym": "🔴", "color": "red"},
            {"number": 24, "color_sym": "⚫", "color": "black"},
            {"number": 25, "color_sym": "🔴", "color": "red"},
            {"number": 26, "color_sym": "⚫", "color": "black"},
            {"number": 27, "color_sym": "🔴", "color": "red"},
            {"number": 28, "color_sym": "⚫", "color": "black"},
            {"number": 29, "color_sym": "⚫", "color": "black"},
            {"number": 30, "color_sym": "🔴", "color": "red"},
            {"number": 31, "color_sym": "⚫", "color": "black"},
            {"number": 32, "color_sym": "🔴", "color": "red"},
            {"number": 33, "color_sym": "⚫", "color": "black"},
            {"number": 34, "color_sym": "🔴", "color": "red"},
            {"number": 35, "color_sym": "⚫", "color": "black"},
            {"number": 36, "color_sym": "🔴", "color": "red"}]

def increment_wallet(user_ID, user_Name, bet, winning = 0, losing = 0):
    user_profile = get_user_profile(user_ID)
    bet += user_profile['wallet']
    winning += user_profile['winning']
    losing += user_profile['loss']
    update_user_profile(user_ID, bet, winning, losing)
    print(f"User {user_Name} changed wallet balance by {bet - user_profile['wallet']} and now have {user_profile['wallet'] + (bet - user_profile['wallet'])}")
    print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-{user_Name}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def get_Color(color):
    if color == "green":
        return "https://steamuserimages-a.akamaihd.net/ugc/837016417742838438/5258F84A9E37C7378C10813273F05FB7DC69F50A/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
    elif color == "black":
        return "https://cms.qz.com/wp-content/uploads/2016/03/kapoor.png?quality=75&strip=all&w=1200&h=900&crop=1"
    else:
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Socialist_red_flag.svg/1280px-Socialist_red_flag.svg.png"

def rands(num1=0, num2=36):
    return randint(int(num1), int(num2))

@client.command()
async def help(ctx, *arg):
    if arg:
        return
    Help = discord.Embed(
        title="__-==Komandu saraksts==-__",
        description=None,
        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    HelpImage = discord.File("Help_Image.jpg", filename="HelpImage.jpg")
    Help.set_thumbnail(url="attachment://HelpImage.jpg")
    Help.add_field(name="**Nejaušo skaitļu ģenerators**", value="<`/rand \"*Number1*\" \"*Number2 *\"`>", inline=False)
    Help.add_field(name="**Likme uz krāsu**", value="<`/betcolor \"*Color*\" \"*Bet*\"`>", inline=False)
    Help.add_field(name="**Likme uz skaitli**", value="<`/betonnumber \"*Number*\"`>", inline=False)
    Help.add_field(name="**Papildus informācija**", value="<`/info`>", inline=False)

    await ctx.send(file=HelpImage, embed=Help)

@client.command()
async def info(ctx, *args):
    if args:
        return

    Embeds = discord.Embed(
        title="__--===Rulete!===--__",
        description="",
        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    Embeds.add_field(name="**Uzmini krāsu vai skaitli**", value="""
    Ir dotas 3 krāsas 🔴⚫🟢
    Tu vari uzlikt likmi vienu no krāsām
    Vai uz kādu konkrētu cipraru
    """, inline=False)
    Embeds.add_field(name="**Likme uz krāsām**", value="""Liekot likmi uz krāsu jāieraksta skaitlis attiecīgi krāsai
    piemērs: <`/betcolor red 25`>
    Attiecīgi ja uzmini krāsu, tu uzvari!
    """, inline=True)
    Embeds.add_field(name="**Likme uz skaitļiem**", value="""Liekot likmi uz skaitli jāieraksta attiecīgs skaitlis uz kā tiks likta likme
    piemērs: <`/betonnumber 25`>
    Attiecīgi ja uzmini skaitli, tu uzvari!
    """, inline=True)
    file = discord.File("rulete.png", filename="image.png")
    Embeds.set_image(url="attachment://image.png")
    Embeds.set_thumbnail(
        url="https://images.theconversation.com/files/147757/original/image-20161128-22748-1couruj.jpg?ixlib=rb-1.1.0&rect=0%2C252%2C5616%2C2723&q=45&auto=format&w=1356&h=668&fit=crop")
    await ctx.send(file=file, embed=Embeds)

@client.command()
async def daily(ctx):
    user = get_user_profile(ctx.author.id)
    if user['daily_bonus'] < datetime.datetime.now().date():
        set_daily_date(ctx.author.id)
        increment_wallet(ctx.author.id, ctx.author.name, 100)

        await ctx.send("Jūsu maciņš papildināts!")
    else:
        await ctx.send("Gaidiet nākošo dienu, lai papildinātu maciņu!")

@client.command()
async def profile(ctx):
    user = get_user_profile(ctx.author.id)
    embedsProfile = discord.Embed(
        title=f"{ctx.author.name}",
        description="""
            **Balance**: {0}
            **Bonuss paņemts**: {1}
            **Uzvarēts**: {2}
            **Zaudēts**: {3}
            **Profit**: {4}
            """.format(user['wallet'], user['daily_bonus'], user['winning'], user['losing'], user['winning'] + user['losing']),

        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=ctx.author.colour
    )
    embedsProfile.set_thumbnail(url=ctx.author.avatar_url)
    embedsProfile.set_footer(text=f"{ctx.author}")
    await ctx.send(embed=embedsProfile)

@client.command()
async def balance(ctx, *args):
    if args:
        return

    user_ID = get_user_profile(ctx.author.id)
    await ctx.send(f"Jūsu maciņā ir {user_ID['wallet']}")


@client.command()
async def betcolor(ctx, inputColor, inputBet):
    inputColor = str(inputColor.lower())
    inputBet = int(inputBet)

    user = get_user_profile(ctx.author.id)

    if (inputBet <= 0 or inputBet > user['wallet']) or (
            inputColor != "red" and inputColor != "black" and inputColor != "green"):
        if inputBet <= 0 or user['wallet'] < inputBet:
            await ctx.send("Ievadīta nezināma likme!")
        else:
            await ctx.send("Ievadīta nezināma krāsa!")
        return
    random = rands()
    element = Roulette[random]

    link = get_Color(element['color'])

    winning = 0
    losing = 0

    if element['color'] == inputColor:
        multiplier = 10 if inputColor == "green" else 2
        bet = (0 - inputBet) + (inputBet * multiplier)
        result = f"Tu uzminēji krāsu un uzvarēji {bet + inputBet}"
        winning = bet
    else:
        bet = 0 - inputBet
        losing = bet
        result = f"Tu neuzminēji krāsu un zaudēji {bet}!"
    increment_wallet(ctx.author.id, ctx.author, bet, winning, losing)

    if inputColor == "red":
        symbolColor = "🔴"
    elif inputColor == "black":
        symbolColor = "⚫"
    else:
        symbolColor = "🟢"

    embedsResult = discord.Embed(
        title="-==Spēles rezūltāti==-",
        description="""
        **Jūsu ievadītā krāsa ir** - **{0}**
        **Izkritušais skaitlis ir** - **{1}**
        **Izkritušais skaitlis atbilst ar {2} krāsu**

        **{3}**
        """.format(symbolColor, random, element['color_sym'], result),

        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    embedsResult.set_thumbnail(url=link)
    embedsResult.set_footer(text=f"{ctx.author} • Tavā maciņā pašlaik ir {user['wallet'] + bet}")

    await ctx.send(embed=embedsResult)


@client.command()
async def betonnumber(ctx, betedNumber):  # TODO jāsāk taisīt
    betedNumber = int(betedNumber)
    random = rands()
    element = Roulette[random]
    link = get_Color(element['color_sym'])
    user = get_user_profile(ctx.author.id)

    winning = 0
    losing = 0

    # if element['number'] == Roulette[betedNumber]['number']:
    #     multiplier = 10 if inputColor == "green" else 2
    #     bet = (0 - inputBet) + (inputBet * multiplier)
    #     result = f"Tu uzminēji skaitli un uzvarēji {bet + inputBet}"
    #     winning = bet
    # else:
    #     bet = 0 - inputBet
    #     losing = bet
    #     result = f"Tu neuzminēji skaitli un zaudēji {bet}!"

    if element['number'] == Roulette[betedNumber]['number']:
        result = "Tu uzminēji skaitli!"
    else:
        result = "Tu neuzminēji skaitli!"

    embedsResult = discord.Embed(
        title="-==Spēles rezūltāti==-",
        description="""
        **Jūsu ievadītais skaitlis ir** - **{0}**
        **Izkritušais skaitlis ir** - **{1}**
        **Izkritušais skaitlis atbilst ar {2} krāsu**

        **{3}**
        """.format(betedNumber, element['number'], element['color_sym'], result),

        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    embedsResult.set_thumbnail(url=link)
    embedsResult.set_footer(text=f"{ctx.author} • Tavā maciņā pašlaik ir {user['wallet'] + bet}")

    await ctx.send(embed=embedsResult)

@client.command()
async def rand(ctx, arg1, arg2):
    random = rands(arg1, arg2)
    sends = await ctx.send(f"{ctx.author.name} nejaušais skaitlis: {random}")
    for times in range(10):
        random = rands(arg1, arg2)
        await sends.edit(content=f"{ctx.author.name} nejaušais skaitlis: {random}")
        sleep(0.01)

@client.command()
async def timer(ctx, *args):
    if args:
        return
    goal = datetime.datetime(2022, 7, 11, 5, 20, 00)
    while True:
        if not goal - datetime.datetime.now():
            break
        now = datetime.datetime.now()
        now = now.replace(microsecond=0)
        await ctx.send(f"{goal - now} left")
        await asyncio.sleep(30)
    await ctx.send("target is achieved")

@client.command()
async def guildTest(ctx, *args):
    print(ctx.guild.name)

    users = get_users_profile()
    strings = ""
    print(len(users))
    for x in range(len(users)):
        strings += str(x+1) + ". " + "**" + str(users[x]['nickname']) + "**\n"

    embedsTemplate = discord.Embed(
        title="-==Servera statistika==-",
        description="""
            {0}
            """.format(strings),

        timestamp=datetime.datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    top = discord.File("top_guild_logo.png", filename="top_guild_logo.png")
    embedsTemplate.set_thumbnail(url="attachment://top_guild_logo.png")
    embedsTemplate.set_footer(text=f"{ctx.author}")
    await ctx.send(file=top, embed=embedsTemplate)

client.run(os.getenv("TOKEN"))

# TODO idejas:
"""
1. !profile, izvadīs smuku embedu par useru(Nicku, bildi, balance, un visādus sīkumus ko var realizēt)(Aizstajot !balance)
2. !top (Serveru vai visu serveru tops ar to cik daudz naudas ir useriem vai serveru kopumam)
3. Betot procentoali no balances vērtības
4. Izveidot timeri.
5. Izveidot proiflu(prioritāte) (Done+/-)
6. kur salīdzina krāsas izmantot short if (Done)
"""
