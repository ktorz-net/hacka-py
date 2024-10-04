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
    print( f"<<\n{game.board}\n>>" )
    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

    assert not game.applyPlayerAction(1, "move 1 3 6")
    print( f"<<\n{game.board}\n>>" )
    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 6]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Army: A [0, 6]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

    assert not game.applyPlayerAction(1, "move 1 2 6")
    print( f"<<\n{game.board}\n>>" )
    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: A [0, 6]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Army: A [0, 6]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

    assert game.applyPlayerAction(1, "sleep")
    print( f"<<\n{game.board}\n>>" )
    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: A [1, 6]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Army: A [1, 6]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

    assert not game.applyPlayerAction(1, "move 2 3 3")
    print( f"<<\n{game.board}\n>>" )
    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: A [1, 3]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Army: A [0, 9]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""


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
    game.board.cell(2).piece().setFlag(FORCE, 12)
    game.board.cell(1).piece().setFlag(FORCE, 12)

    assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

    assert not game.applyPlayerAction(2, "move 2 1 4")
    
    assert f"\n{game.board.cell(2)}\n" == """
Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 8]
"""

    defences[ game.board.cell(1).piece().flag(FORCE) ] += 1

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
    game.board.cell(1).piece().setFlag(FORCE, 15)
    game.board.cell(2).piece().setFlag(FORCE, 8)
    assert not game.applyPlayerAction(1, "move 1 2 14")

    assert f"\n{game.board.cell(1)}\n" == """
Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 1]
"""

    if  game.board.cell(2).pieces() and game.board.cell(2).piece().status() == 'A' :
      attack[ game.board.cell(2).piece().flag(FORCE) ] += 1
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

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

  game.actionGrow(1, 1)

  print( f"<<\n{game.board.cell(1)}\n>>" )
  assert f"\n{game.board.cell(1)}\n" == """
Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [0, 16]
"""

  game.applyPlayerAction(1, "grow 1")

  print( f"<<\n{game.board.cell(1)}\n>>" )
  assert f"\n{game.board.cell(1)}\n" == """
Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [0, 16]
"""

  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "move 1 3 6")
  game.applyPlayerAction(1, "grow 1")

  print( f"<<\n{game.board.cell(1)}\n>>" )
  assert f"\n{game.board.cell(1)}\n" == """
Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [0, 15]
"""

#------------------------------------------------------------------------------------------------
# Test action Sleep
#------------------------------------------------------------------------------------------------
def test_risky_sleep():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

  game.applyPlayerAction(1, "sleep")
  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [2, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

  game.applyPlayerAction(1, "sleep")

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [2, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "sleep")

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [2, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""


#------------------------------------------------------------------------------------------------
# Test action Fight 2
#------------------------------------------------------------------------------------------------
def test_risky_growNmove():
  game= GameRisky(2, "board-4")
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 12]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

  game.applyPlayerAction(1, "move 1 3 1")
  game.applyPlayerAction(1, "grow 1")
  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "grow 3")
  game.applyPlayerAction(1, "move 1 3 1")

  print( f"<<\n{game.board}\n>>" )
  assert f"\n{game.board}\n" == """
Board:
- Cell-1 coords: [5.0, 3.0] adjs: [2, 3, 4]
- Army: A [1, 15]
- Cell-2 coords: [5.0, 15.0] adjs: [1, 3, 4]
- Army: B [1, 12]
- Cell-3 coords: [1.0, 9.0] adjs: [1, 2]
- Army: A [0, 4]
- Cell-4 coords: [9.0, 9.0] adjs: [1, 2]
"""

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------------------------------------------------------------------------------
