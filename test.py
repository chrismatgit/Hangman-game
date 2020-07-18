import unittest
from unittest.mock import patch
from game import Game, start_game


class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=['python', 'javascript', 'java'])
    def test_random_word(self, mock):
        self.assertIn(Game.random_word(self), 'python')

    @patch('builtins.input', side_effect=[''])
    def test_random_word_randomly(self, mock):
        rand_word = Game.random_word(self)
        exp_word = rand_word
        self.assertEqual(rand_word, exp_word)


if __name__ == "__main__":
    unittest.main()
