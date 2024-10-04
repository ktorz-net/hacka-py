# Local HackaGame:
import sys

sys.path.insert(1, __file__.split('gameRisky')[0])

import hackapy as hg
from gameRisky.gameEngine import GameRisky

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Board (regarding Risky usage)
#------------------------------------------------------------------------------------------------

gamePath= __file__.split('gameRisky')[0] + "/gameRisky"

def test_board_load():
  aPod= hg.Pod()
  board= hg.Board()
  f= open(f"{gamePath}/resources/map-board-4.pod")
  aPod.load( f.read() )
  f.close()

  assert f"\n{aPod}\n" == """
Board: board-4
- Cell: [1, 2, 3, 4] [5.0, 3.0]
- Cell: [2, 1, 3, 4] [5.0, 15.0]
- Cell: [3, 1, 2] [1.0, 9.0]
- Cell: [4, 1, 2] [9.0, 9.0]
"""

  board.fromPod( aPod )

  assert f"\n{board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

def test_board_loadAll():
  aPod= hg.Pod()
  board= hg.Board()
  for map in [ "board-4", "board-6" ] :  
    f= open(f"{gamePath}/resources/map-board-4.pod")
    txt= f.read()
    f.close()
    aPod.load( txt )
    assert aPod.dump() == txt
    
    board.fromPod( aPod )

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------

def test_risky_init():
    game= GameRisky(1)
    assert game.map == "board-4"
    assert game.numberOfPlayers == 1
    aPod= game.initialize()

    print(f"<<\n{aPod}\n>>")
    assert f"\n{aPod}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

    print(f"<<\n{game.playerHand(1).dump()}\n>>")
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 7 2 0 1 : board-4 1 4
Board - 0 0 0 4 :
Cell - 0 4 2 1 : 1 2 3 4 5.0 3.0
Army - 1 2 0 0 : A 1 12
Cell - 0 4 2 0 : 2 1 3 4 5.0 15.0
Cell - 0 3 2 0 : 3 1 2 1.0 9.0
Cell - 0 3 2 0 : 4 1 2 9.0 9.0
"""

    print(f"<<\n{game.playerHand(1)}\n>>")
    assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
  - Cell: [3, 1, 2] [1.0, 9.0]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_init_6():
    game= GameRisky( 2, "board-6" )
    assert game.map == "board-6"
    assert game.numberOfPlayers == 2
    game.initialize()
    
    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 7 2 0 1 : board-6 1 6
Board - 0 0 0 6 :
Cell - 0 5 2 1 : 1 2 3 4 5 5.0 3.0
Army - 1 2 0 0 : A 1 12
Cell - 0 5 2 1 : 2 1 3 4 6 5.0 15.0
Army - 1 2 0 0 : B 1 12
Cell - 0 3 2 0 : 3 1 2 1.0 9.0
Cell - 0 5 2 0 : 4 1 2 5 6 9.0 9.0
Cell - 0 4 2 0 : 5 1 4 6 13.0 3.0
Cell - 0 4 2 0 : 6 2 4 5 13.0 15.0
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_10():
    game= GameRisky( 2, "board-10" )
    assert game.map == "board-10"
    assert game.numberOfPlayers == 2
    game.initialize()

    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 8 2 0 1 : board-10 1 10
Board - 0 0 0 10 :
Cell - 0 5 2 1 : 1 3 5 7 9 11.0 3.0
Army - 1 2 0 0 : A 1 12
Cell - 0 5 2 1 : 2 4 6 8 9 11.0 36.0
Army - 1 2 0 0 : B 1 12
Cell - 0 5 2 0 : 3 1 4 5 10 1.0 9.0
Cell - 0 5 2 0 : 4 2 3 6 10 1.0 29.0
Cell - 0 4 2 0 : 5 1 3 10 7.0 9.0
Cell - 0 4 2 0 : 6 2 4 10 7.0 30.0
Cell - 0 3 2 0 : 7 1 10 11.0 13.0
Cell - 0 3 2 0 : 8 2 10 11.0 26.0
Cell - 0 3 2 0 : 9 1 2 15.0 20.0
Cell - 0 7 2 0 : 10 3 4 5 6 7 8 7.0 19.0
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_12():
    game= GameRisky( 2, "board-12" )
    assert game.map == "board-12"
    assert game.numberOfPlayers == 2
    game.initialize()

    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 8 2 0 1 : board-12 1 12
Board - 0 0 0 12 :
Cell - 0 5 2 1 : 1 3 5 7 9 11.0 3.0
Army - 1 2 0 0 : A 1 12
Cell - 0 5 2 1 : 2 4 6 8 10 11.0 36.0
Army - 1 2 0 0 : B 1 12
Cell - 0 3 2 0 : 3 1 11 15.0 9.0
Cell - 0 3 2 0 : 4 2 11 15.0 31.0
Cell - 0 4 2 0 : 5 1 9 12 7.0 9.0
Cell - 0 4 2 0 : 6 2 10 12 7.0 30.0
Cell - 0 3 2 0 : 7 1 12 11.0 13.0
Cell - 0 3 2 0 : 8 2 12 11.0 26.0
Cell - 0 5 2 0 : 9 1 5 10 12 1.0 9.0
Cell - 0 5 2 0 : 10 2 6 9 12 1.0 29.0
Cell - 0 3 2 0 : 11 3 4 15.0 20.0
Cell - 0 7 2 0 : 12 5 6 7 8 9 10 7.0 19.0
"""

#------------------------------------------------------------------------------------------------
# Test some accessors...
#------------------------
def test_risky_accessors():
    game= GameRisky(1)
    game.initialize()
    assert not game.isCell(0)
    assert game.isCell(1)
    assert game.isCell(2)
    assert game.isCell(3)
    assert game.isCell(4)
    assert not game.isCell(5)
    assert not game.isCell(42)
    assert not game.isCell(-3)

    assert [2, 3, 4] == game.cell(1).adjacencies()
    assert game.armyOn(1)
    assert not game.armyOn(3)

    army= game.armyOn(1)
    assert game.playerLetter(1) == "A"
    assert army.status() == "A"
    assert army.flag(FORCE) == 12
    assert army.flag(ACTION) == 1

#------------------------------------------------------------------------------------------------
# Test end condition
#------------------------
def test_risky_end():
  game= GameRisky(2, "board-4")
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

  assert game.playerArmies() == [0, 12, 12]
  assert game.playerScore( 1 ) == 0
  assert game.playerScore( 2 ) == 0

  game.popArmy( 1, 4, 1, 6 )

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
    - Army: A [1, 6]
"""

  assert not game.isEnded()

  assert game.playerArmies() == [0, 18, 12]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1

  for i in range( game.duration ) :
    game.tic()

  assert game.isEnded()

  game.board.cell(2).pieces().pop()
  
  # Test winners...
  assert game.activePlayers() == [1]
  assert game.playerArmies() == [0, 18, 0]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1
  assert game.isEnded()

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------