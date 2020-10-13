import unittest

from applied_computer_science_discord_bot.message_handlers import ParsedCommand


class ParsedCommandTests(unittest.TestCase):
    def test_from_string_class_method(self):
        cmd = ParsedCommand.from_string("bot.john_cena()")
        cmd2 = ParsedCommand.from_string("bot.john_cena(john=cena)")

        self.assertEqual(cmd.arguments, {})
        self.assertEqual(cmd2.arguments, {'john': 'cena'})


if __name__ == '__main__':
    unittest.main()
