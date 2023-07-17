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
def test_risky_initializeClassic():
  game= GameTTT()
  pod= game.initialize()
  assert str(pod) == "TicTacToe-Classic"
  assert "\n"+str(game.playerHand(1)) == """
grid
- A [0, 0, 0]
- B [0, 0, 0]
- C [0, 0, 0]
- targets [1]"""

  assert "\n"+str(game.playerHand(2)) == """
grid
- A [0, 0, 0]
- B [0, 0, 0]
- C [0, 0, 0]
- targets [1]"""

#------------------------------------------------------------------------------------------------
# Test Initialize Ultimate
#------------------------
def test_risky_initializeUltimate():
  game= GameTTT("ultimate")
  pod= game.initialize()
  assert str(pod) == "TicTacToe-Ultimate"
  assert "\n"+str(game.playerHand(1)) == """
grid
- A [0, 0, 0, 0, 0, 0, 0, 0, 0]
- B [0, 0, 0, 0, 0, 0, 0, 0, 0]
- C [0, 0, 0, 0, 0, 0, 0, 0, 0]
- D [0, 0, 0, 0, 0, 0, 0, 0, 0]
- E [0, 0, 0, 0, 0, 0, 0, 0, 0]
- F [0, 0, 0, 0, 0, 0, 0, 0, 0]
- G [0, 0, 0, 0, 0, 0, 0, 0, 0]
- H [0, 0, 0, 0, 0, 0, 0, 0, 0]
- I [0, 0, 0, 0, 0, 0, 0, 0, 0]
- targets [1, 4, 5]"""
