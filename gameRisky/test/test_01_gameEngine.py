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

def verbose(aString):
  pass


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
- 6 2 0 1 : Cell-1 5 3
  - 1 2 0 0 : A 1 12
- 6 3 0 0 : Edge-1 2 3 4
- 6 2 0 0 : Cell-2 5 15
- 6 3 0 0 : Edge-2 1 3 4
- 6 2 0 0 : Cell-3 1 9
- 6 2 0 0 : Edge-3 1 2
- 6 2 0 0 : Cell-4 9 9
- 6 2 0 0 : Edge-4 1 2"""

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