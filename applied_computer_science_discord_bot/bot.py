import os
import discord
from discord.message import Message

from applied_computer_science_discord_bot.message_hub import MessageHub

TOKEN = os.environ["token"]

client = discord.Client()
hub = MessageHub(client)


@client.event
async def on_message(message: Message):
    print(message.content)
    if client.user != message.author:
        hub.accept_message(message)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN, bot=True, reconnect=True)
