import unittest
from unittest.mock import patch
from rps_game import get_user_choice, get_computer_choice, determine_winner


class TestRPSGame(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_get_user_choice(self, input):
        self.assertEqual(get_user_choice(), 'rock')

    def test_get_computer_choice(self):
        self.assertIn(get_computer_choice(), ['rock', 'paper', 'scissors'])

    def test_determine_winner(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'Meat bags win!')
        self.assertEqual(determine_winner('rock', 'paper'), 'Meat bags: 0 Computers: 1')
        self.assertEqual(determine_winner('rock', 'rock'), "It's a tie!")


if __name__ == '__main__':
    unittest.main()

