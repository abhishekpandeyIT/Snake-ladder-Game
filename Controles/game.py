import itertools


class Game:
    def __init__(self, players):
        self.players = itertools.cycle(players)
        self.num_players = len(players)

        # This list is created so that we can check if any players have won
        # For checking that, we have called next(..) function on the list
        # If we had used the next(..) function on the original players iterator list,
        # then it would alter the playing sequence and it is difficult to know which player's turn it is next
        # So, self.players is for the sole purpose of tracking next player
        # and self.mutable_players is kind of temporary list
        self.mutable_players = itertools.cycle(players)

    def has_finished(self):
        # if anyone of the player has won, the game is finished
        for i in range(self.num_players):
            player = next(self.mutable_players)
            if player.has_won():
                return True
        return False

    def next_player(self):
        return next(self.players)
