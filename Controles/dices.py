# import itertools
# import random
# import time

# Snakes and ladders do basically the same thing, they take the player to some another box. I put them
# here together, so it would be easier to check later.

# SNAKESANDLADDERS = {
#     27: 7,
#     35: 5,
#     39: 3,
#     50: 34,
#     59: 46,
#     66: 24,
#     73: 12,
#     76: 63,
#     89: 67,
#     97: 86,
#     99: 26,
#     2: 23,
#     8: 29,
#     22: 41,
#     28: 77,
#     30: 32,
#     44: 58,
#     54: 69,
#     70: 90,
#     80: 83,
#     87: 93,
# }


# class Dice:

#     # Since all the players will use the same dice to play, there need not be more than one instances of dice
#     # So, it is better if Dice is made static.
#     @staticmethod
#     def rollDice():
#         return random.randint(1, 6)


# class Player:
#     def __init__(self, name):
#         self.name = name.capitalize()
#         self.position = 0

#         # Initially, the player is not born (meaning she will remain at position 0 till dice shows 1
#         self.born = False

#         # Store the last three consecutive moves, we will use this later to check if it equals [6,6,6]
#         self.last_three_moves = [0, 0, 0]

#     def has_won(self):
#         # If position = 100, player has won
#         return self.position == 100

#     def update_position(self, dicevalue):

#         # the following two lines will pop one element(zeroth index element) from the list,
#         # and add the latest dicevalue to the list
#         # so that the list will be updated
#         self.last_three_moves.pop(0)
#         self.last_three_moves.append(dicevalue)

#         if self.last_three_moves == [6, 6, 6]:
#             self.position = 0
#             self.born = False
#             return

#         new_pos = self.position + dicevalue

#         # if new position exceeds 100, don't update the current position
#         # instead, return
#         if new_pos >= 100:
#             return
#         else:
#             self.position = new_pos

#         # if the new position has a snake or ladder, update the position after snake or ladder
#         while self.position in SNAKESANDLADDERS:
#             self.position = SNAKESANDLADDERS[self.position]

#     def print_position(self):
#         print(self.name, "POSITION ==>", str(self.position))

#     def play(self):
#         dicevalue = Dice.roll()
#         print(self.name + ": DICE SHOWS " + str(dicevalue))

#         if dicevalue == 1:
#             self.born = True

#         if not self.born:
#             print(self.name + ": player is not born yet")
#         else:

#             # The following is emulation of a do-while loop
#             while True:
#                 self.update_position(dicevalue)
#                 self.print_position()
#                 # if dicevalue is not 6, her turn is finished
#                 if dicevalue != 6:
#                     break
#                 # else roll the dice again
#                 else:
#                     dicevalue = Dice.roll()


# class Game:
# def __init__(self, players):
#     self.players = itertools.cycle(players)
#     self.num_players = len(players)

#     # This list is created so that we can check if any players have won
#     # For checking that, we have called next(..) function on the list
#     # If we had used the next(..) function on the original players iterator list,
#     # then it would alter the playing sequence and it is difficult to know which player's turn it is next
#     # So, self.players is for the sole purpose of tracking next player
#     # and self.mutable_players is kind of temporary list
#     self.mutable_players = itertools.cycle(players)

# def has_finished(self):
#     # if anyone of the player has won, the game is finished
#     for i in range(self.num_players):
#         player = next(self.mutable_players)
#         if player.has_won():
#             return True
#     return False

# def next_player(self):
#     return next(self.players)


# if __name__ == "__main__":
#     no_of_players = int(input("Enter the no of player:"))
#     player_names = [name for name in input(
#         "Enter the name of players:").split()]
#     players = [Player(name) for name in player_names]

#     game = Game(players)

#     while not game.has_finished():
#         player = game.next_player()
#         player.play()
#         time.sleep(5)


# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:36:30 2019
@author: ARVIND KRISHNA
"""
import random
import sys
"""A program which will simulate rolling of a die and moves of a pawn in snake and ladders.
Max number of players allowed is 4 and with a min of 2.
Enjoy the game.
A simple Command-line snake-and-ladder game"""


def Move(Player, value):
    """THIS FUNCTION MOVES THE PAWN AND ALSO CHECKS FOR 
    WINNING AND OVERFLOW"""
    snake_squares = {16: 4, 22: 10, 33: 20, 48: 24,
                     62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder_squares = {3: 12, 7: 23, 11: 25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)
    num = value + Throw
    if num > 100:
        print("BAD LUCK, YOU CANT MOVE, YOU NEED A {} TO WIN".format(100 - value))
        return value
    if num == 100:
        return num
    # IF NONE OF THE OTHER CONDITIONS ARE MATCHED,
    print(Player, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        # if landed in a snake square
        print(Player, " got bitten by a snake and is now on square",
              snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        # if landed in a ladder square
        print(Player, " climbed a ladder and is now on square",
              ladder_squares[num])
        num = ladder_squares[num]

    return num


def playerscount():
    """ACCEPTS THE NUM OF PLAYERS"""
    numofplayers = int(input("How many players are in the game?"))
    print()
    if numofplayers > 4 or numofplayers < 2:
        print("Must be less than 5 and greater than 1")
    else:
        return numofplayers


def nameofplayers(N):
    """ACCEPTS THE NAME OF PLAYERS AND REUTUNS THE LIST OF NAMES"""
    Names = ['', '', '', '']
    for i in range(N):
        Names[i] = input("What is the name of Player "+str(i+1)+" ?")
    return Names


def turn(player, pos):
    COMMANDSTATE = "Press Enter to continue or press 'stop' to stop"
    WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
    COMMANDSTATE1 = str("Hey "+player+"! It's your turn now "+COMMANDSTATE)
    Command = input(COMMANDSTATE1)
    if Command.lower() == 'stop':
        # if the user commands to stop, the game must stop,
        # so the GameOver flag will become true
        return True, pos
    pos = Move(player, pos)
    if pos == 100:
        print(player, WINSTATEMENT)
        print("AT WINNING {} was at {}".format(player, pos))
        # if a player wins, the game is over
        # so the GameOver flag will become true
        return True, pos

    # if the function has not returned anywhere above
    # it means that the game is still on
    return False, pos


def main():
    """THE MAIN FUNCTION"""
    numofplayers = playerscount()
    playernames = nameofplayers(numofplayers)
    print(playernames[0], playernames[1], playernames[2],
          playernames[3], "- Welcome To Snakes And Ladders")
    COMMANDSTATE = "Press Enter to continue or press 'stop' to stop: "
    WINSTATEMENT = "WINS THE GAME! CONGRATULATIONS"
    Command = ''
    TURNS = 0
    PosArr = [1, 1, 1, 1]
    # A list containing the present positions of the pawns
    GameOver = False
    # Flag to check whether the game should be continued or not
    while not GameOver:
        while TURNS < numofplayers:
            # This loops takes care of each person's moves.
            # if TURNS == 1, it means that its person1's turn
            TURNS += 1
            GameOver, PosArr[TURNS -
                             1] = turn(playernames[TURNS - 1], PosArr[TURNS - 1])
            if GameOver:
                # if gameover, exit the function
                return
        TURNS = 0
    return


if __name__ == '__main__':
    main()
