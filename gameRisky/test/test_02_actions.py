# Local HackaGame:
import sys


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky

# Army Flags
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test action move
#------------------------------------------------------------------------------------------------
def test_risky_move():
    game= GameRisky(1)
    game.initialize()
    assert "\n"+ str(game.board) == """
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

    assert not game.applyPlayerAction(1, "move 1 3 6")
    assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [1, 6]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
  - A [0, 6]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

    assert not game.applyPlayerAction(1, "move 1 2 6")
    assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - A [0, 6]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
  - A [0, 6]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

    assert game.applyPlayerAction(1, "sleep")
    assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - A [1, 6]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
  - A [1, 6]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

    assert not game.applyPlayerAction(1, "move 2 3 3")
    assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - A [1, 3]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
  - A [0, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

    assert "\n"+ game.board.dump() == """
7 2 0 8 : board-4 1 4
6 2 0 0 : Cell-1 5 3
6 3 0 0 : Edge-1 2 3 4
6 2 0 1 : Cell-2 5 15
1 2 0 0 : A 1 3
6 3 0 0 : Edge-2 1 3 4
6 2 0 1 : Cell-3 1 9
1 2 0 0 : A 0 9
6 2 0 0 : Edge-3 1 2
6 2 0 0 : Cell-4 9 9
6 2 0 0 : Edge-4 1 2"""

#------------------------------------------------------------------------------------------------
# Test action Fight 1
#------------------------------------------------------------------------------------------------
# Test fight ...
samples= 10000
def test_risky_fight1(): # Failled attack
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  # Test winners...
  assert not game.isEnded()

  # get possible defences results for `samples` fight samples
  defences= [0 for i in range(13)]
  for i in range(samples):
    game.board.cell(2).child(1).setFlag(FORCE, 12)
    game.board.cell(1).child(1).setFlag(FORCE, 12)
    assert "\n"+ str(game.board) == """
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

    assert not game.applyPlayerAction(2, "move 2 1 4")
    assert "\n"+str(game.board.cell(2)) == """
Cell-2 [5, 15]
- B [1, 8]"""

    defences[ game.board.cell(1).child(1).flag(FORCE) ] += 1

  # Compare percentages: 
  print( [ (obs*100)/samples for obs in defences ] )
  for obs, ref in zip( defences, [ 0, 0, 0, 0, 0, 0, 0, 0, 6, 25, 37, 25, 6 ] ) :
    assert (obs*100)//samples in [ref-2, ref-1, ref, ref+1, ref+2]

  # Test winners...
  assert not game.isEnded()

#------------------------------------------------------------------------------------------------
# Test action Fight 2
#------------------------------------------------------------------------------------------------
def test_risky_fight2(): # Successive attack
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  # Test winners...
  assert not game.isEnded()

  # get possible defences results for `samples` fight samples on
  attack= [0 for i in range(15)]
  for i in range(samples):
    game.initialize()
    game.board.cell(1).child(1).setFlag(FORCE, 15)
    game.board.cell(2).child(1).setFlag(FORCE, 8)
    assert not game.applyPlayerAction(1, "move 1 2 14")
    assert "\n"+ str(game.board.cell(1)) == """
Cell-1 [5, 3]
- A [1, 1]"""

    if  game.board.cell(2).children() and game.board.cell(2).child(1).status() == 'A' :
      attack[ game.board.cell(2).child(1).attribute(FORCE) ] += 1
    else :
      attack[0] += 1

  # Compare percentages: 
  print( [ (obs*100)/samples for obs in attack ] )
  for obs, ref in zip( attack, [ 0, 0, 0, 0, 0, 2, 6, 17, 27, 25, 15, 6, 1, 0, 0 ] ) :
    assert (obs*100)//samples in [ref-2, ref-1, ref, ref+1, ref+2]

  # Test winners...
  assert game.isEnded()


#------------------------------------------------------------------------------------------------
# Test action Grow
#------------------------------------------------------------------------------------------------
def test_risky_grow():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert "\n"+ str(game.board) == """
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

  game.actionGrow(1, 1)

  assert "\n"+ str( game.board.cell(1) ) == """
Cell-1 [5, 3]
- A [0, 16]"""

  game.applyPlayerAction(1, "grow 1")

  assert "\n"+ str( game.board.cell(1) ) == """
Cell-1 [5, 3]
- A [0, 16]"""


  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "move 1 3 6")
  game.applyPlayerAction(1, "grow 1")

  assert "\n"+ str( game.board.cell(1) ) == """
Cell-1 [5, 3]
- A [0, 15]"""


#------------------------------------------------------------------------------------------------
# Test action Sleep
#------------------------------------------------------------------------------------------------
def test_risky_sleep():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert "\n"+ str(game.board) == """
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

  game.applyPlayerAction(1, "sleep")
  assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [2, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

  game.applyPlayerAction(1, "sleep")

  assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [2, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "sleep")


  assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [2, 12]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""


#------------------------------------------------------------------------------------------------
# Test action Fight 2
#------------------------------------------------------------------------------------------------
def test_risky_growNmove():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert "\n"+ str(game.board) == """
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

  game.applyPlayerAction(1, "move 1 3 1")
  game.applyPlayerAction(1, "grow 1")
  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "grow 3")
  game.applyPlayerAction(1, "move 1 3 1")

  assert "\n"+ str(game.board) == """
board-4 [1, 4]
- Cell-1 [5, 3]
  - A [1, 15]
- Edge-1 [2, 3, 4]
- Cell-2 [5, 15]
  - B [1, 12]
- Edge-2 [1, 3, 4]
- Cell-3 [1, 9]
  - A [0, 4]
- Edge-3 [1, 2]
- Cell-4 [9, 9]
- Edge-4 [1, 2]"""

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
