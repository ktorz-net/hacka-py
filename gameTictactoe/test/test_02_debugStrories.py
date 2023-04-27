# Local HackaGame:
import sys

sys.path.insert(1, __file__.split('gameTictactoe')[0])
from gameTictactoe.gameEngine import GameTTT

# ------------------------------------------------------------------------ #
#                   T E S T   T I C T A C T O E    G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_play():
  game= GameTTT()
  game.initialize()
  assert True
