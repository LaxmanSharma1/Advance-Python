
class LeaderBoard():

    _table = {}

    def __new__(cls):
        return cls
    
    @classmethod
    def print(cls): 

        print("-----------------leaderboard------------------------")
        for key,value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
    
    
    @classmethod
    def add_winner(cls,position,name): 
        cls._table[position] = name

    
