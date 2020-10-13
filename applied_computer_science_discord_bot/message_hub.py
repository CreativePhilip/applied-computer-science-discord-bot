from enum import Enum
import re
from discord import Client

from applied_computer_science_discord_bot.message_handlers import Handler, CommandHandler, ParsedCommand
from discord.message import Message


class MessageHub:
    """
    Main class for getting all the messages, to use it you just have to call
    obj.register_handler() with appropriate params
    """
    def __init__(self, client: Client):
        self.client = client
        self.handlers = {}

        self.last_message = None

    def accept_message(self, message: Message):
        """
        Method for handling every incoming message from the discord API
        :param message:
        """
        msg_type = self._message_type(message.content)
        self.__emit(message, msg_type)

    @staticmethod
    def _message_type(message: str) -> "MessageType":
        """
        Analyzes the message and determines its type
        :param message: message content
        :return:
        """
        return MessageType.COMMAND if re.match(r"^bot\..*[(].*[)]$", message) else MessageType.NORMAL

    def register_handler(self, msg_type: "MessageType", handler_object):
        """
        :param msg_type: Enum MessageType, it describes to which messages you want to subscribe to
        :param handler_object: subclass of Handler from applied_computer_science_discord_bot.message_handlers
        :return: None
        """
        if not (issubclass(handler_object.__class__, Handler) or issubclass(handler_object.__class__, CommandHandler)):
            raise TypeError("parameter 'handler_object' must be a subclass of Handler!")

        if msg_type not in self.handlers:
            self.handlers.update({msg_type: []})
        self.handlers[msg_type].append(handler_object)

    def __emit(self, message: Message, message_type: "MessageType"):
        if message_type not in self.handlers:
            return
        payload = {"message": message}
        if message_type == MessageType.COMMAND:
            payload.update({"parsed_message": ParsedCommand.from_string(message.content)})

        for handler in self.handlers[message_type]:
            handler.handle(**payload)


class MessageType(Enum):
    """
    Enum for describing the message type
    """
    All = 0
    NORMAL = 1
    COMMAND = 2
