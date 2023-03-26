# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('gameRisky')[0] )

from gameEngine import GameRisky
from playerFirstAI import AutonomousPlayer as Player

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

def verbose(aString):
  print(aString)

# Test move action ...
def test_risky_play():
  game= GameRisky( 2, "board-10" )
  player1= Player()
  player2= Player()
  game.local( [player1, player2], 1 )
