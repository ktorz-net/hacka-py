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
  assert str(pod) == "TicTacToe: Classic"

  print( f"<<\n{game.playerHand(1)}\n>>" )

  assert f"\n{game.playerHand(1)}\n" == """
Grid:
- Line: A [0, 0, 0]
- Line: B [0, 0, 0]
- Line: C [0, 0, 0]
- Targets: [1]
"""

  assert f"\n{game.playerHand(2)}\n" == """
Grid:
- Line: A [0, 0, 0]
- Line: B [0, 0, 0]
- Line: C [0, 0, 0]
- Targets: [1]
"""

#------------------------------------------------------------------------------------------------
# Test Initialize Ultimate
#------------------------
def test_risky_initializeUltimate():
  game= GameTTT("ultimate")
  pod= game.initialize()
  assert str(pod) == "TicTacToe: Ultimate"
  assert f"\n{game.playerHand(1)}\n" == """
Grid:
- Line: A [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: B [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: C [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: D [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: E [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: F [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: G [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: H [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Line: I [0, 0, 0, 0, 0, 0, 0, 0, 0]
- Targets: [1, 4, 5]
"""
