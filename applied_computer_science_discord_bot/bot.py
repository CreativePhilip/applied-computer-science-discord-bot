#!/usr/bin/env python3

import os
import discord
from discord.message import Message

from applied_computer_science_discord_bot.message_hub import MessageHub, MessageType
from applied_computer_science_discord_bot.message_handlers import PrintHandler

TOKEN = os.environ["token"]

client = discord.Client()
hub = MessageHub(client)


@client.event
async def on_message(message: Message):
    if client.user != message.author:
        await hub.accept_message(message)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    hub.register_handler(MessageType.COMMAND, PrintHandler(client=client))


client.run(TOKEN, bot=True, reconnect=True)
