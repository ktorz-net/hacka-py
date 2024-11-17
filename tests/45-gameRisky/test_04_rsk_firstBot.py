import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

from src.hacka.games.risky import GameRisky
from src.hacka.games.risky.firstBot import Bot as Player

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test play board-4 
#------------------------
def test_risky_play4():
  game= GameRisky( 2, "board-4" )
  player1= Player()
  player2= Player()
  game.launch( [player1, player2], 1 )

#------------------------------------------------------------------------------------------------
# Test play board-10 
#------------------------
def test_risky_play10():
  game= GameRisky( 2, "board-10" )
  player1= Player()
  player2= Player()
  game.launch( [player1, player2], 1 )
