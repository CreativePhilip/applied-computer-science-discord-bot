from enum import Enum

from discord import Client

from applied_computer_science_discord_bot.message_handlers import Handler
from discord.message import Message


class MessageHub:
    """
    Main class for getting all the messages, to use it you just have to call
    obj.register_handler() with appropriate params
    """
    def __init__(self, client=Client):
        self.client = client
        self.handlers = {}

        self.last_message = None

    def accept_message(self, message: Message):
        """
        Method for handling every incoming message from the discord API
        :param message:
        """
        msg_type = self._message_type(message)
        self.__emit(message, msg_type)

    def _message_type(self, message: Message) -> "MessageType":
        pass

    def register_handler(self, msg_type: "MessageType", handler_object):
        """
        :param msg_type: Enum MessageType, it describes to which messages you want to subscribe to
        :param handler_object: subclass of Handler from applied_computer_science_discord_bot.message_handlers
        :return: None
        """
        if not issubclass(handler_object.__class__, Handler):
            raise TypeError("parameter 'handler_object' must be a subclass of Handler!")

        if msg_type not in self.handlers:
            self.handlers.update({msg_type: []})
        self.handlers[msg_type].append(handler_object)

    def __emit(self, message: Message, message_type: "MessageType"):
        pass


class MessageType(Enum):
    """
    Enum for describing the message type
    """
    All = 0
    NORMAL = 1
    COMMAND = 2
