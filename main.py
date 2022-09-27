from modulefinder import IMPORT_NAME
import time
from Controles.player_controller import Player
from Controles.game import Game
from Models.dice_model import Dices


if __name__ == "__main__":
    no_of_players = int(input("Enter the no of player:"))
    player_names = [name for name in input(
        "Enter the name of players:").split()]

    # player = Player(player_names)
    # game1 = Game()
    dices = Dices()
    players = [Player(name) for name in player_names]

    game = Game(players)

    print(dices.dice_value_4)
    while not game.has_finished():
        player = game.next_player()
        player.play()
        time.sleep(5)
