"""
    This is where the players wait for the game to start
"""

from .player import Player
from .game import Game

NUMBER_PLAYERS_LIMIT = 4

class Lobby:

    def __init__(self, leader: Player) -> None:
        self.leader = leader    # only player allowed to start the game
        self.players = [leader]


    def player_join(self, new_player: Player) -> bool:

        # limit the number of players to 4
        if len(self.player) >= NUMBER_PLAYERS_LIMIT:
            return False

        self.players.append(new_player)        
        return True
    
    def player_left(self, player) -> None:
        self.players.remove(player)

    def start_game(self) -> None:
        """
        Start the game with the players in the lobby
        """
        game = Game(self.players)
        game.start()