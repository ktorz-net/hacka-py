# Local HackaGame:
import sys, random


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky

# Army Flags
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Wrong Actions
#------------------------------------------------------------------------------------------------
def test_risky_wrongAction():
  game= GameRisky()
  game.initialize()

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

  assert game.wrongAction == [0, 0, 0]

  game.applyPlayerAction( 1, "move 1 2 0" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

  assert game.wrongAction == [0, 1, 0]


#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
def test_risky_Fight01():
  game= GameRisky()
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

  random.seed(4)
  game.fight( 1, 1, 10, 2 )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 4]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
def test_risky_fight02():
  game= GameRisky()
  game.initialize()
  random.seed(4)
  game.fight( 1, 1, 15, 2 )

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: A [0, 4]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""


#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
def test_risky_grow():
  game= GameRisky()
  game.initialize()
  game.actionGrow( 1, 1 )
  army= game.armyOn(1)
  assert str(army) == "Army: A [0, 16]"
  game.actionGrow( 1, 1 )
  assert str(army) == "Army: A [0, 16]"
  army.setFlag(ACTION, 2)
  assert str(army) == "Army: A [2, 16]"
  game.actionGrow( 1, 1 )
  assert str(army) == "Army: A [1, 22]"
  game.actionGrow( 1, 1 )
  assert str(army) == "Army: A [0, 24]"
  army.setFlag(ACTION, 2)
  game.actionGrow( 1, 1 )
  assert str(army) == "Army: A [1, 24]"


#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
def test_risky_wrongAction():
  game= GameRisky()
  game.initialize()
  assert game.wrongAction == [0, 0, 0]
  game.applyPlayerAction( 1, "move 1 2 10" )
  assert game.wrongAction == [0, 0, 0]
  game.initialize()
  game.applyPlayerAction( 1, "move 2 1 10" )
  assert game.wrongAction == [0, 1, 0]
  game.applyPlayerAction( 1, "move" )
  game.applyPlayerAction( 1, "grow 4" )
  game.applyPlayerAction( 2, "truc" )
  assert game.wrongAction == [0, 3, 1]

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
def test_risky_copy():
  game= GameRisky()
  game.initialize()
  game2= game.copy()

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

  print( f"<<\n{game2.playerHand(1).dump()}\n---\n{game.playerHand(1).dump()}\n>>" )
  assert game2.playerHand(1).dump() ==  game.playerHand(1).dump()

  game2.applyPlayerAction( 1, "move 1 3 10" )

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

  assert f"\n{game2.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 2]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Cell: [3, 1, 2] [1.0, 9.0]
    - Army: A [0, 10]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""
