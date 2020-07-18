import string
from random import choice
from helper import MAX_GUESSES, HANGMAN_STRINGS


class Game():
    """ Class that initialize contain the hangman game"""
    HANGMAN_STRINGS = HANGMAN_STRINGS
    MAX_GUESSES = MAX_GUESSES

    def __init__(self):
        self.word = self.random_word()
        self.incorrect = []
        self.correct = []
        self.progress = self.get_progress()
        self.gameover = False

    def random_word(self):
        """ 
            method that chose randomly a word
            @return word from the list of words

        """
        input_list = input(
            "\nEnter your list of words separated by comma. Leave empty for default: ").lower()
        user_word = [w.strip() for w in input_list.split(',')]

        dictionary = open('dictionary.txt', 'r').readlines()
        words = [word.strip() for word in dictionary]

        # checking word in list of word. Return word
        if input_list:
            return choice(user_word)
        else:
            return choice(words)

        print("\n### Game Initialized. Let's play!!\n")

    def get_progress(self):
        # change lsit back to string
        return "".join([let if let in self.correct else "_" for let in self.word])

    def already_guessed(self, guess):
        """ Method to return the already guessed string """
        return guess in self.correct + self.incorrect

    def guess_letter(self, guess):
        """ Method to return the guessed string """
        if guess in self.word:
            self.correct.append(guess)
        else:
            self.incorrect.append(guess)

    def status(self):
        """
            Methode to check the current status
            @return message with the correct if you loose
            @return message a positive message if you won
        """
        if len(self.incorrect) >= Game.MAX_GUESSES:
            self.gameover = True
            return "\nYou lose. The word was {}.".format(self.word)
        if set(self.correct) == set(self.word):
            self.gameover = True
            return "\nYou won!"
        return ""

    def __str__(self):
        result = ""
        result += Game.HANGMAN_STRINGS[len(self.incorrect)]
        result += "\nIncorrect guesses: {}".format(", ".join(self.incorrect))
        result += "\nProgress: {}".format(self.get_progress())
        result += self.status()
        return result


def valid_guess(game):
    # function to validate the game
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or guess not in string.ascii_lowercase:
            print("Please guess a letter.")
        elif game.already_guessed(guess):
            print("You've already guessed {}.".format(guess))
        else:
            return guess


def start_game():
    """ Function to start the game """
    keepGoing = True
    while keepGoing:
        # playing the game
        game = Game()
        print("\n**************************")
        print("###### HANGMAN GAME ######")
        print("**************************")
        print(game)  # printing the image
        while not game.gameover:
            guess = valid_guess(game)
            game.guess_letter(guess)
            print(game)
        play_again = input("Play again? (y/n): ").lower()
        if "n" in play_again:
            keepGoing = False
    print("Thanks for playing!")


if __name__ == "__main__":
    start_game()
