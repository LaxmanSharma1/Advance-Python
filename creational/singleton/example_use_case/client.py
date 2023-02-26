
from game1 import Game1
from game2 import Game2
from game3 import Game3 


game1 = Game1()
game1.add_winner(1,"Ramesh")
game2 = Game2()
game2.add_winner(2,"Suresh")
game3 = Game3() 
game3.add_winner(3,"Rajesh")
game1.leaderboard.print()
game2.leaderboard.print()
game3.leaderboard.print()