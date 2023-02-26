
from leaderboard import LeaderBoard
from interface_game import IGame 

class Game3(IGame):

    def __init__(self) -> None:
        self.leaderboard = LeaderBoard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)

