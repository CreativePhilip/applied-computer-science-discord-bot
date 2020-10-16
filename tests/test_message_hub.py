import unittest

from applied_computer_science_discord_bot.message_handlers import TestHandler
from applied_computer_science_discord_bot.message_hub import MessageHub, MessageType


class MessageHubTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hub = MessageHub(None)

    def test_registering_invalid_object_raises_error(self):
        with self.assertRaises(TypeError):
            hub = MessageHub(None)
            hub.register_handler(MessageType.All, lambda x: x**2)

    def test_registering_new_msg_type_for_the_first_time_ads_a_field_to_handlers(self):
        test = TestHandler(None)

        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.NORMAL, test)
        self.hub.register_handler(MessageType.All, test)

        self.assertTrue(MessageType.COMMAND in self.hub.handlers)
        self.assertTrue(MessageType.All in self.hub.handlers)
        self.assertTrue(MessageType.NORMAL in self.hub.handlers)

    def test_registering_multiple_same_type_handlers_adds_properly(self):
        test = TestHandler(None)

        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.COMMAND, test)
        self.hub.register_handler(MessageType.COMMAND, test)

        self.assertEqual(len(self.hub.handlers[MessageType.COMMAND]), 3)

    def test_message_type_recognizes_valid_commands(self):
        type1 = self.hub._message_type("bot.twoja_stara()")
        type2 = self.hub._message_type("bot.twoja_stara(xd=12)")

        self.assertEqual(type1, MessageType.COMMAND)
        self.assertEqual(type2, MessageType.COMMAND)

    def test_message_type_recognizes_other_message(self):
        type1 = MessageHub._message_type("bottwoja_stara()")
        type2 = MessageHub._message_type("bottwoja_stara(xd=12)")

        self.assertEqual(type1, MessageType.NORMAL)
        self.assertEqual(type2, MessageType.NORMAL)


if __name__ == '__main__':
    unittest.main()
