from msilib.schema import ODBCDataSource
import discord
from discord.ext import commands
from random import randint
import pytz
from datetime import datetime
import os
from dotenv import load_dotenv
from function_db import *

load_dotenv()

#Funkcijas labāk glabā atsevišķā failā

# Apvieno, RAMS raud, apvieno vienā rindā
def rands(num1 = 0, num2 = 36):
    return randint(int(num1),int(num2))

def get_Color(color):
    if color == "🟢":
        return "https://steamuserimages-a.akamaihd.net/ugc/837016417742838438/5258F84A9E37C7378C10813273F05FB7DC69F50A/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
    elif color == "⚫":
        return "https://cms.qz.com/wp-content/uploads/2016/03/kapoor.png?quality=75&strip=all&w=1200&h=900&crop=1"
    else:
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Socialist_red_flag.svg/1280px-Socialist_red_flag.svg.png"

def increment_wallet(user_ID):
    user_profile = get_user_profile(user_ID) #WALLET SISTĒMAS IZVEIDOŠANA(Jāturpina)
    print(user_profile[0][2])
    print(f"user {user_ID} have {user_profile[0][2]} on balance")
    print()
    update_user_profile(user_ID, 100)
    user_profile = get_user_profile(user_ID)
    print(f"now user {user_ID} have {user_profile[0][2]} on balance")

Roulette = [{"number": 0,"color": "🟢", "color": "green"},
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

# client = discord.Client()
client = commands.Bot(command_prefix='!')
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    get_status()
    print("-=-=-=-=-=-=-=-=-")
    get_users()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    
@client.command()
async def rand(ctx, arg1,arg2):
    random = rands(arg1,arg2)
    await ctx.send(random)

@client.command()
async def help(ctx, *arg):
    if arg:
        return
    Help = discord.Embed(
        title="__-==Komandu saraksts==-__",
        description=None,
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    HelpImage = discord.File("Help_Image.jpg", filename="HelpImage.jpg")
    Help.set_thumbnail(url="attachment://HelpImage.jpg")
    Help.add_field(name="**Nejaušo skaitļu ģenerators**", value="<`/rand \"*Number1*\" \"*Number2 *\"`>", inline=False)
    Help.add_field(name="**Likme uz krāsu**", value="<`/betcolor \"*Color*\"`>", inline=False)
    Help.add_field(name="**Likme uz skaitli**", value="<`/betonnumber \"*Number*\"`>", inline=False)
    Help.add_field(name="**Papildus informācija**", value="<`/info`>", inline=False)
    

    await ctx.send(file = HelpImage, embed=Help)

    
@client.command()
async def info(ctx, *args):
    if args:
        return

    set_user(ctx.author.id, ctx.author.name)
    print()
    increment_wallet(ctx.author.id)
    print()
    print(ctx.author)
    print()
    Embeds = discord.Embed(
        title="__--===Rulete!===--__",
        description="",
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    Embeds.add_field(name="**Uzmini krāsu vai skaitli**", value="""
    Ir dotas 3 krāsas 🔴⚫🟢
    Tu vari uzlikt likmi vienu no krāsām
    Vai uz kādu konkrētu cipraru
    """, inline=False)
    Embeds.add_field(name="**Likme uz krāsām**", value="""Liekot likmi uz krāsu jāieraksta skaitlis attiecīgi krāsai
    piemērs: <`/betcolor 25`>
    Attiecīgi ja uzmini krāsu, tu uzvari!
    """, inline=True)
    Embeds.add_field(name="**Likme uz skaitļiem**", value="""Liekot likmi uz skaitli jāieraksta attiecīgs skaitlis uz kā tiks likta likme
    piemērs: <`/betonnumber 25`>
    Attiecīgi ja uzmini skaitli, tu uzvari!
    """, inline=True)
    file = discord.File("rulete.png", filename="image.png")
    Embeds.set_image(url="attachment://image.png")
    Embeds.set_thumbnail(url="https://images.theconversation.com/files/147757/original/image-20161128-22748-1couruj.jpg?ixlib=rb-1.1.0&rect=0%2C252%2C5616%2C2723&q=45&auto=format&w=1356&h=668&fit=crop")
    await ctx.send(file=file, embed=Embeds)

### @client.command()
### async def formathelp(ctx):
###     qwerty=discord.Embed(
###     title="Text Formatting",
###         url="https://realdrewdata.medium.com/",
###         description="Here are some ways to format text",
###         color=discord.Color.blue())
###     qwerty.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
###     #qwerty.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
###     qwerty.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
###     qwerty.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=True)
###     qwerty.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=True)
###     qwerty.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=True)
###     qwerty.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=True)
###     qwerty.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=True)
###     qwerty.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=True)
###     qwerty.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=True)
###     qwerty.set_footer(text="Learn more here: realdrewdata.medium.com")

#     await ctx.send(embed=qwerty)
    # Embeds.add_field
    # *Italics*
    # **Bold**
    # __Underline__
    # ~~Strikethrough~~
    # `Code Chunks`
    # Blockquotes ">"
    # Secrets 
    # Embeds.set_footer

@client.command()
async def betcolor(ctx, arg):
    arg = str(arg.lower())
    if not arg == "red" or arg == "black" or arg == "green":
        await ctx.send("Ievadīta nezināma krāsa!")
        return
    random = rands()
    element = Roulette[random]

    link = get_Color(element['color'])


    embedsResult = discord.Embed(
        title="-==Spēles rezūltāti==-",
        description="""
        **Jūsu ievadītais skaitlis ir** - **{0}**
        **Izkritušais skaitlis ir** - **{1}**
        **Izkritušais skaitlis atbilst ar {2} krāsu**

        **{3}**
        """.format(arg, random, element['color_sym'], "Tu uzminēji krāsu!" if element['color'] == arg else "Tu neuzminēji krāsu!"),
        
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    embedsResult.set_thumbnail(url=link)

    await ctx.send(embed=embedsResult)

@client.command()
async def betonnumber (ctx, arg):
    OnBet = int(arg)
    #Bet = int(arg2)
    random = rands()
    element = Roulette[random]
    link = get_Color(element['color_sym'])

    if element['number'] == Roulette[OnBet]['number']:
        
        result = "Tu uzminēji Skaitli!"
    else:
        result = "Tu neuzminēji Skaitli!"


    embedsResult = discord.Embed(
        title="-==Spēles rezūltāti==-",
        description="""
        **Jūsu ievadītais skaitlis ir** - **{0}**
        **Izkritušais skaitlis ir** - **{1}**
        **Izkritušais skaitlis atbilst ar {2} krāsu**

        **{3}**
        """.format(OnBet,random,element['color_sym'],result),
        
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    embedsResult.set_thumbnail(url=link)

    await ctx.send(embed=embedsResult)



client.run(os.getenv("TOKEN"))