from msilib.schema import ODBCDataSource
import discord
from discord.ext import commands
from random import randint
import pytz
from datetime import datetime



#Funkcijas labāk glabā atsevišķā failā

# Apvieno, RAMS raud, apvieno vienā rindā
def rands(num1 = 0, num2 = 36):
    random = randint(num1,num2)
    return random

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
    arg1 = int(arg1)
    arg2 = int(arg2)
    random = rands(arg1,arg2)
    print(random)
    await ctx.send(random)
    
@client.command()
async def info(ctx, *args):
    if args:
        return
    Embeds = discord.Embed(
        title="Šī ir rulete!",
        description="""
        Tavs uzdevums uzminēt krāsu
        **Melna :black_circle:(Pāra skaitļi)**
        **Sarkana :red_circle:(Nepāra skaitļi)**
        **Zaļa :green_circle: (Nulle)**
        Ja uzminēsi krāsu, tu uzvarēji!
        """,
        
        timestamp=datetime.utcnow().replace(tzinfo=pytz.utc),
        colour=discord.Colour.purple()
    )
    Embeds.set_thumbnail(url="https://images.theconversation.com/files/147757/original/image-20161128-22748-1couruj.jpg?ixlib=rb-1.1.0&rect=0%2C252%2C5616%2C2723&q=45&auto=format&w=1356&h=668&fit=crop")
    await ctx.send(embed=Embeds)
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
async def rulete(ctx, arg):
    arg =  int(arg)
    random = rands()
    print(random)
    
    if random % 2 == 0:
        numType = True
    else:
        numType = False

    if arg % 2 == numType:
        await ctx.send("Tu uzminēji krāsu!")
    else:
        await ctx.send("Tu neuzminēji krāsu!")

client.run('OTUzNjc0NDE1NjI1ODc1NTc2.YjIAgw.PDgIP-3FZE3LT8KdunclvYOYmto')