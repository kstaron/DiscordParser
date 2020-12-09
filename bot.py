import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hist')
async def hist(ctx, arg: int):
    messages = await ctx.channel.history(limit=200).flatten()
    print(messages[arg])
    print(len(messages))


bot.run(TOKEN)
