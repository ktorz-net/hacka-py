# Local HackaGame:
import sys


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init():
    game= GameRisky(1)
    assert game.map == "board-4"
    assert game.numberOfPlayers == 1
    game.initialize()
    assert "\n"+ game.playerHand(1).dump() == """
7 2 0 8 : board-4 1 4
6 2 0 1 : Cell-1 5 3
1 2 0 0 : A 1 12
6 3 0 0 : Edge-1 2 3 4
6 2 0 0 : Cell-2 5 15
6 3 0 0 : Edge-2 1 3 4
6 2 0 0 : Cell-3 1 9
6 2 0 0 : Edge-3 1 2
6 2 0 0 : Cell-4 9 9
6 2 0 0 : Edge-4 1 2"""

    assert "\n"+ str(game.playerHand(1)) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [1, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_6():
    game= GameRisky( 2, "board-6" )
    assert game.map == "board-6"
    assert game.numberOfPlayers == 2
    game.initialize()
    assert "\n"+ game.playerHand(1).dump() == """
7 2 0 12 : board-6 1 6
6 2 0 1 : Cell-1 5 3
1 2 0 0 : A 1 12
6 4 0 0 : Edge-1 2 3 4 5
6 2 0 1 : Cell-2 5 15
1 2 0 0 : B 1 12
6 4 0 0 : Edge-2 1 3 4 6
6 2 0 0 : Cell-3 1 9
6 2 0 0 : Edge-3 1 2
6 2 0 0 : Cell-4 9 9
6 4 0 0 : Edge-4 1 2 5 6
6 2 0 0 : Cell-5 13 3
6 3 0 0 : Edge-5 1 4 6
6 2 0 0 : Cell-6 13 15
6 3 0 0 : Edge-6 2 4 5"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_10():
    game= GameRisky( 2, "board-10" )
    assert game.map == "board-10"
    assert game.numberOfPlayers == 2
    game.initialize()
    assert "\n"+ game.playerHand(1).dump() == """
8 2 0 20 : board-10 1 10
6 2 0 1 : Cell-1 11 3
1 2 0 0 : A 1 12
6 4 0 0 : Edge-1 3 5 7 9
6 2 0 1 : Cell-2 11 36
1 2 0 0 : B 1 12
6 4 0 0 : Edge-2 4 6 8 9
6 2 0 0 : Cell-3 1 9
6 4 0 0 : Edge-3 1 4 5 10
6 2 0 0 : Cell-4 1 29
6 4 0 0 : Edge-4 2 3 6 10
6 2 0 0 : Cell-5 7 9
6 3 0 0 : Edge-5 1 3 10
6 2 0 0 : Cell-6 7 30
6 3 0 0 : Edge-6 2 4 10
6 2 0 0 : Cell-7 11 13
6 2 0 0 : Edge-7 1 10
6 2 0 0 : Cell-8 11 26
6 2 0 0 : Edge-8 2 10
6 2 0 0 : Cell-9 15 20
6 2 0 0 : Edge-9 1 2
7 2 0 0 : Cell-10 7 19
7 6 0 0 : Edge-10 3 4 5 6 7 8"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_10():
    game= GameRisky( 2, "board-12" )
    assert game.map == "board-12"
    assert game.numberOfPlayers == 2
    game.initialize()
    assert "\n"+ game.playerHand(1).dump() == """
8 2 0 24 : board-12 1 12
6 2 0 1 : Cell-1 11 3
1 2 0 0 : A 1 12
6 4 0 0 : Edge-1 3 5 7 9
6 2 0 1 : Cell-2 11 36
1 2 0 0 : B 1 12
6 4 0 0 : Edge-2 4 6 8 10
6 2 0 0 : Cell-3 15 9
6 2 0 0 : Edge-3 1 11
6 2 0 0 : Cell-4 15 31
6 2 0 0 : Edge-4 2 11
6 2 0 0 : Cell-5 7 9
6 3 0 0 : Edge-5 1 9 12
6 2 0 0 : Cell-6 7 30
6 3 0 0 : Edge-6 2 10 12
6 2 0 0 : Cell-7 11 13
6 2 0 0 : Edge-7 1 12
6 2 0 0 : Cell-8 11 26
6 2 0 0 : Edge-8 2 12
6 2 0 0 : Cell-9 1 9
6 4 0 0 : Edge-9 1 5 10 12
7 2 0 0 : Cell-10 1 29
7 4 0 0 : Edge-10 2 6 9 12
7 2 0 0 : Cell-11 15 20
7 2 0 0 : Edge-11 3 4
7 2 0 0 : Cell-12 7 19
7 6 0 0 : Edge-12 5 6 7 8 9 10"""

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

    assert [2, 3, 4] == game.edgesFrom(1)
    assert game.armyOn(1)
    assert not game.armyOn(3)

    army= game.armyOn(1)
    assert game.playerLetter(1) == "A"
    assert army.status() == "A"
    assert army.attribute(FORCE) == 12
    assert army.attribute(ACTION) == 1

#------------------------------------------------------------------------------------------------
# Test end condition
#------------------------
def test_risky_end():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  
  assert "\n"+ str(game.playerHand(1)) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [1, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

  assert game.playerArmies() == [0, 12, 12]
  assert game.playerScore( 1 ) == 0
  assert game.playerScore( 2 ) == 0

  game.popArmy( 1, 4, 1, 6 )

  assert "\n"+ str(game.playerHand(1)) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [1, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
  - A [1, 6]
- Edge-4 [1, 2]"""

  assert not game.isEnded()

  assert game.playerArmies() == [0, 18, 12]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1

  for i in range( game.duration ) :
    game.tic()

  assert game.isEnded()

  game.board.cell(2).children().pop()
  
  # Test winners...
  assert game.activePlayers() == [1]
  assert game.playerArmies() == [0, 18, 0]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1
  assert game.isEnded()

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------