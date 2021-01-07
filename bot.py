#!/usr/bin/env python3
"""Discord bot created in python. Started 11/6/20 by Derron Knox"""

import discord
import os
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv


# used to invoke intents
intents = discord.Intents.default()
intents.members = True

# loads a .env file that stores bot token
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('INSERT TOKEN HERE')
