from typing import Dict

from discord import Message, Client


class Handler:
    def __init__(self, client: Client):
        self.client = client

    async def handle(self, message: Message):
        pass


class CommandHandler:
    def __init__(self, client: Client):
        self.client = client

    async def handle(self, message:  Message, parsed_message, *, is_auth=True):
        pass


class ParsedCommand:
    def __init__(self, name: str, params: Dict):
        self.name = name
        self.arguments = params

    @classmethod
    def from_string(cls, message: str):
        message = message.replace("bot.", "")
        name = message[:message.find("(")]
        args_str = message[message.find("(") + 1: message.find(")")]
        args_str = args_str.replace(",", "").split(" ")
        args = {}
        try:
            for arg in args_str:
                key, value = arg.split("=")
                args.update({key: value})
        except (KeyError, ValueError):
            pass

        return cls(name, args)


if __name__ == '__main__':
    ParsedCommand.from_string("bot.john_cena(john=cena)")
