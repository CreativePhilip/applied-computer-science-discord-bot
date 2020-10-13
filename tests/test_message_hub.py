import unittest

from applied_computer_science_discord_bot.message_handlers import TestHandler
from applied_computer_science_discord_bot.message_hub import MessageHub, MessageType


class MessageHubTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hub = MessageHub()

    def test_registering_invalid_object_raises_error(self):
        with self.assertRaises(TypeError):
            hub = MessageHub()
            hub.register_handler(MessageType.All, lambda x: x**2)

    def test_registering_new_msg_type_for_the_first_time_ads_a_field_to_handlers(self):
        test = TestHandler()

        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.NORMAL, test)
        self.hub.register_handler(MessageType.All, test)

        self.assertTrue(MessageType.COMMAND in self.hub.handlers)
        self.assertTrue(MessageType.All in self.hub.handlers)
        self.assertTrue(MessageType.NORMAL in self.hub.handlers)

    def test_registering_multiple_same_type_handlers_adds_properly(self):
        test = TestHandler()

        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.COMMAND, test)

        self.assertEqual(len(self.hub.handlers[MessageType.COMMAND]), 3)


if __name__ == '__main__':
    unittest.main()
