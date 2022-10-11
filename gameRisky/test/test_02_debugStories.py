from gameEngine import GameRisky
import random

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

def verbose(aString):
  print(aString)

# Test move action ...
def test_risky_Fight01():
  game= GameRisky()
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert game.playerHand(1).dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 12
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""
  random.seed(4)
  game.actionFight( 1, 1, 10, 2 )
  verbose( game.playerHand(1).dump() )
  assert game.playerHand(1).dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 4
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

def test_risky_fight02():
  game= GameRisky()
  game.initialize()
  random.seed(4)
  game.actionFight( 1, 1, 15, 2 )
  verbose( game.playerHand(1).dump() )
  assert game.playerHand(1).dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : A 0 4
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

def test_risky_grow():
  game= GameRisky()
  game.initialize()
  game.actionGrow( 1, 1 )
  army= game.armyOn(1)
  verbose( army.dump() )
  assert army.dump() == "Army 1 2 0 0 : A 0 16"
  game.actionGrow( 1, 1 )
  assert army.dump() == "Army 1 2 0 0 : A 0 16"
  army.setAttribute(ACTION, 2)
  assert army.dump() == "Army 1 2 0 0 : A 2 16"
  game.actionGrow( 1, 1 )
  assert army.dump() == "Army 1 2 0 0 : A 1 22"
  game.actionGrow( 1, 1 )
  assert army.dump() == "Army 1 2 0 0 : A 0 24"
  army.setAttribute(ACTION, 2)
  game.actionGrow( 1, 1 )
  assert army.dump() == "Army 1 2 0 0 : A 1 24"