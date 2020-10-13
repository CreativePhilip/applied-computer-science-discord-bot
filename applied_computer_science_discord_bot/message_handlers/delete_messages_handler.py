from discord import Message, User, Client

import applied_computer_science_discord_bot.message_handlers.virtual_message_handler as virtual_handler


class DeleteMessagesHandler(virtual_handler.CommandHandler):

    confirm_delete = False

    async def handle(self, message:  Message, parsed_message):

        # TO-DO HIGH PRIORITY SECURITY
        # Validation of user permission to delete messages
        if parsed_message.name == "delete_messages":
            if "n" in parsed_message.arguments and parsed_message.arguments["n"].isnumeric():

                # Ensures Integer only input, may require improved validation
                self.number_of_messages = int(float(parsed_message.arguments["n"]))

                self.confirm_delete = True
                self.request_author = message.author
                self.request_channel = message.channel
                await message.channel.send(
                    "To confirm deletion of %d messages, type \"bot.confirm_delete()\"" % self.number_of_messages)

        elif parsed_message.name == "confirm_delete" and self.confirm_delete \
                and self.request_author == message.author and self.request_channel == message.channel:

            # Ensures the number is between 1 and 100 (purge limits)
            self.number_of_messages = max(0, min(100, self.number_of_messages))

            deleted = await message.channel.purge(limit=self.number_of_messages)
            await message.channel.send("%d messages were successfully deleted" % len(deleted))
