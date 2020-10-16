from discord import Message
import applied_computer_science_discord_bot.message_handlers.virtual_message_handler as virtual_handler


class PrintHandler(virtual_handler.CommandHandler):
    async def handle(self, message:  Message, parsed_message, *, is_auth=True):
        if parsed_message.name == "print":
            if "text" in parsed_message.arguments:
                response = parsed_message.arguments["text"]
                await message.channel.send(response)

    def __str__(self):
        return "PrintHandler()"
