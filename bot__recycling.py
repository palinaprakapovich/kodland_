import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send(f'Pan(i) może wybrać przedmiot z listy i dowiedzieć się w jakim czasie rozkłada się ten przedmiot\n'
                     'lista:\n'
                     '-guma do zucia\n'
                     '-szklane butelki\n'
                     '-baterie\n'
                     '-karty plastykowe\n'
                     '-kubki\n'
                     '-owoce\n'
                     '-warzywa\n'
                     '-butelki plastykowe\n'
                     '-puszki aluminiowe\n'
                     '-szkło\n'
                     '-siatki rybackie\n'
                     '-torby plastykowe\n'
                     '-ubrania\n')

@bot.command()                                            
async def szkło(ctx):                                                 
    await ctx.send(f'1 mln lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def guma(ctx):
    await ctx.send(f'5 lat')
    with open('images/image.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def owoce(ctx):
    await ctx.send(f'3-12 mies.')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def warzywa(ctx):
    await ctx.send(f'3-12 mies.')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def butekli_plastykowe(ctx):
    await ctx.send(f'do 450 lat')
    with open('images/image.webp', 'rb') as f:
          picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def torby_plastykowe(ctx):
    await ctx.send(f'do 1000 lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def puszki_aluminiowe(ctx):
    await ctx.send(f'80-200 lat') 
    with open('images/image.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def kubki_styropianowe(ctx):
    await ctx.send(f'500 lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def baterie(ctx):
    await ctx.send(f'100 lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ubrania_syntetyczne(ctx):
    await ctx.send(f'kilkaset lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def karty_plastikowe(ctx):
    await ctx.send(f'do 1000 lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def butelki_szklane(ctx):
    await ctx.send(f'1 mln lat')
    with open('images/image.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def siatki_rybackie(ctx):
    await ctx.send(f'do 600 lat')
    with open('images/image.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("Тоken")





#Papierowe ręczniki - 2 do 4 tygodni
#Gazety - 6 tygodni
#Skórka od banana - 2 lata
#Buty gumowe - 50 do 80 lat
#Filtry do papierosów - 10 do 12 lat
#Pieluchy jednorazowe - 450 do 500 lat
#Kapsułki do kawy - 150 do 500 lat
#Papierowe torby - około 1 miesiąc
#Chusteczki higieniczne - 3 do 4 miesiące
#Zapałki - 6 miesięcy
#Drewniane meble - 13 do 100 lat
#Ubrania bawełniane - 5 miesięcy do 1 roku  
#Tetra Pak - do 30 lat
#Sznurki i liny - 3 do 14 miesięcy
#Plastikowe butelki na wodę - 450 lat
#Papierowa chusteczka - 3 miesiące
#Karton mleczny - do 5 lat
#Zębatki z drewna - 13 lat
#Siatki rybackie - do 600 lat
#Kubki papierowe z powłoką - 30 lat
