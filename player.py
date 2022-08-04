import random
import math

class Player:
    def __init__(self, letter):
        # Either letter x or o
        self.letter = letter

    # Allow all players to get their next move given the current state of the game
    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        # Computer will randomly choose an valid spot for their next move
        square = random.choice(game.availableMove())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        # User has not inputted an value ie 0 for the top left square
        val = None

        while not validSquare:
            square = input(self.letter + '\'s turn. Input (0-8):')
            # Validation checks
            # 1) Casting input to integer, if it fails then we can say its invalid
            # 2) if that spot is not available on the board, we can also say its invalid
            try:
                val = int(square)
                if val not in game.availableMove():#
                    raise ValueError
                # If both validation check passes then its an valid move
                validSquare = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


