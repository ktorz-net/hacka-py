import sys
sys.path.insert( 1, __file__.split('gamePy421')[0] )

from gamePy421.gameEngine import GameSolo as Game
from gamePy421.playerFirstAI import AutonomousPlayer as Player

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1    G A M E
# ------------------------------------------------------------------------ #

def verbose(aString):
  print(aString)

# Test firstAI launch
def test_risky_play():
  game= Game()
  player1= Player()
  game.local( [player1], 1 )
