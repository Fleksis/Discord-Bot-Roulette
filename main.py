from msilib.schema import ODBCDataSource
import discord
from discord.ext import commands
from random import randint
import pytz
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

#Funkcijas labāk glabā atsevišķā failā

# Apvieno, RAMS raud, apvieno vienā rindā
def rands(num1 = 0, num2 = 36):
    random = randint(int(num1),int(num2))
    return random

def get_Color(color):
    if color == "🟢":
        return "https://steamuserimages-a.akamaihd.net/ugc/837016417742838438/5258F84A9E37C7378C10813273F05FB7DC69F50A/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
    elif color == "⚫":
        return "https://cms.qz.com/wp-content/uploads/2016/03/kapoor.png?quality=75&strip=all&w=1200&h=900&crop=1"
    else:
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Socialist_red_flag.svg/1280px-Socialist_red_flag.svg.png"

Roulette = [{"number": 0,"color": "🟢"},
{"number": 1,"color": "🔴"},
{"number": 2,"color": "⚫"},
{"number": 3,"color": "🔴"},
{"number": 4,"color": "⚫"},
{"number": 5,"color": "🔴"},
{"number": 6,"color": "⚫"},
{"number": 7,"color": "🔴"},
{"number": 8,"color": "⚫"},
{"number": 9,"color": "🔴"},
{"number": 10,"color": "⚫"},
{"number": 11,"color": "⚫"},
{"number": 12,"color": "🔴"},
{"number": 13,"color": "⚫"},
{"number": 14,"color": "🔴"},
{"number": 15,"color": "⚫"},
{"number": 16,"color": "🔴"},
{"number": 17,"color": "⚫"},
{"number": 18,"color": "🔴"},
{"number": 19,"color": "🔴"},
{"number": 20,"color": "⚫"},
{"number": 21,"color": "🔴"},
{"number": 22,"color": "⚫"},
{"number": 23,"color": "🔴"},
{"number": 24,"color": "⚫"},
{"number": 25,"color": "🔴"},
{"number": 26,"color": "⚫"},
{"number": 27,"color": "🔴"},
{"number": 28,"color": "⚫"},
{"number": 29,"color": "⚫"},
{"number": 30,"color": "🔴"},
{"number": 31,"color": "⚫"},
{"number": 32,"color": "🔴"},
{"number": 33,"color": "⚫"},
{"number": 34,"color": "🔴"},
{"number": 35,"color": "⚫"},
{"number": 36,"color": "🔴"}]

# client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
async def info(ctx, *args):
    if args:
        return

    Embeds = discord.Embed(
        title="Šī ir rulete!",
        description="""
        Tavs uzdevums uzminēt krāsu
        **Melna ⚫(2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)**
        **Sarkana 🔴(1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34.36)**
        **Zaļa 🟢 (Nulle)**
        Ja uzminēsi krāsu, tu uzvarēji!
        """,
        
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    file = discord.File("rulete.png", filename="image.png")
    Embeds.set_image(url="attachment://image.png")
    Embeds.set_thumbnail(url="https://images.theconversation.com/files/147757/original/image-20161128-22748-1couruj.jpg?ixlib=rb-1.1.0&rect=0%2C252%2C5616%2C2723&q=45&auto=format&w=1356&h=668&fit=crop")
    await ctx.send(file=file, embed=Embeds)
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
async def bet_color(ctx, arg):
    arg = int(arg)
    if arg >= 37 or arg <= -1:
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
        """.format(arg,random,element['color'],"Tu uzminēji krāsu!" if element['color'] == Roulette[arg]['color'] else "Tu neuzminēji krāsu!"),
        
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    embedsResult.set_thumbnail(url=f"{link}")

    await ctx.send(embed=embedsResult)


client.run(os.getenv("TOKEN"))