from random import randint


class Dice:
    # Since all the players will use the same dice to play, there need not be more than one instances of dice
    # So, it is better if Dice is made static.

    @staticmethod
    def rollDice():
        return randint(1, 6)
