# Local HackaGame:
import sys


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky
from gameRisky.playerFirstAI import AutonomousPlayer as Player

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
  game.local( [player1, player2], 1 )

#------------------------------------------------------------------------------------------------
# Test play board-10 
#------------------------
def test_risky_play10():
  game= GameRisky( 2, "board-10" )
  player1= Player()
  player2= Player()
  game.local( [player1, player2], 1 )
