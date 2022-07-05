import discord
from discord.ext import commands
import greentext_maker

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Running...")


@client.command()
async def greentext(ctx, *, message):
    path = greentext_maker.greentext(message)

    await ctx.send(file=discord.File(path))


with open('token.txt', 'r') as f:
    token = f.read()
if token.strip() == '':
    print("Please add your token to token.txt")
    exit()
while token.endswith('\n'):
    token = token[:-1]
client.run(token)
