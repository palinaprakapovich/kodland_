import discord
from discord.ext import commands
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\\U0001f642')

@bot.command()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, is not cool')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(5):
        await ctx.send(content)

bot.run(" your token")
