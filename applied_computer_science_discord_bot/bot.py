import os
import asyncio
import discord
from discord.message import Message

TOKEN = os.environ["token"]

client = discord.Client()


@client.event
async def on_message(message: Message): pass


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN, bot=True, reconnect=True)
