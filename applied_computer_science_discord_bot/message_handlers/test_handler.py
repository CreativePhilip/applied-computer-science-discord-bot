from discord import Message

import applied_computer_science_discord_bot.message_handlers.virtual_message_handler as virtual_handler


class TestHandler(virtual_handler.Handler):
    is_deleting = True

    def handle(self, message:  Message):
        pass
