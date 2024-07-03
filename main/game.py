
from .player import Player

class Game:
    NUMBER_OF_ROUNDS = 10

    def __innit__(self, players) -> None:
        self.players = players  # list of players in this game
        self.round = None   # current round

    def player_join(self, new_player: Player):

        # limit the number of players to 4
        if len(self.player) >= 4:
            return

        if new_player not in self.players:
            self.players.append(new_player)

    def update_scores(self, round_result):
        """
        Update the score of each player in the game
        :param round_result: dict {player: round_score}
        """
        for player in round_result:
            round_score = round_result[player]
            self.players[player].update_score(round_score)

    def start_new_round(self):
        pass

    def start(self) -> None:
        round_number = 1

        # while the game is not over, we will continue creating new rounds
        while round_number < self.NUMBER_OF_ROUNDS:

            # start a new round with the players
            # start the round
            # round returns the scores from the players
            # update players' scores

            round_number += 1

        pass

        # game over
        # show the result of the game


