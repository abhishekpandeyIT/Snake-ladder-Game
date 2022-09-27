from Controles.dice_controller import Dice

SNAKESANDLADDERS = {
    27: 7,
    35: 5,
    39: 3,
    50: 34,
    59: 46,
    66: 24,
    73: 12,
    76: 63,
    89: 67,
    97: 86,
    99: 26,
    2: 23,
    8: 29,
    22: 41,
    28: 77,
    30: 32,
    44: 58,
    54: 69,
    70: 90,
    80: 83,
    87: 93,
}


class Player:

    # def __init__(self):
    #     pass

    def __init__(self, name):
        self.name = name
        self.position = 0

        # Initially, the player is not born (meaning she will remain at position 0 till dice shows 1
        self.born = False

        # Store the last three consecutive moves, we will use this later to check if it equals [6,6,6]
        self.last_three_moves = [0, 0, 0]

    def has_won(self):
        # If position = 100, player has won
        return self.position == 100

    def update_position(self, dicevalue):

        # the following two lines will pop one element(zeroth index element) from the list,
        # and add the latest dicevalue to the list
        # so that the list will be updated
        self.last_three_moves.pop(0)
        self.last_three_moves.append(dicevalue)

        if self.last_three_moves == [6, 6, 6]:
            self.position = 0
            self.born = False
            return

        new_pos = self.position + dicevalue

        # if new position exceeds 100, don't update the current position
        # instead, return
        if new_pos >= 100:
            return
        else:
            self.position = new_pos

        # if the new position has a snake or ladder, update the position after snake or ladder
        while self.position in SNAKESANDLADDERS:
            self.position = SNAKESANDLADDERS[self.position]

    def print_position(self):
        print(self.name, "POSITION ==>", str(self.position))

    def play(self):
        dicevalue = Dice.rollDice()
        print(self.name + ": DICE SHOWS " + str(dicevalue))

        if dicevalue == 1:
            self.born = True

        if not self.born:
            print(self.name + ": player is not born yet")
        else:

            # The following is emulation of a do-while loop
            while True:
                self.update_position(dicevalue)
                self.print_position()
                # if dicevalue is not 6, her turn is finished
                if dicevalue != 6:
                    break
                # else roll the dice again
                else:
                    dicevalue = Dice.rollDice()
