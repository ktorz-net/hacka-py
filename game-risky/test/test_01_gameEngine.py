from gameEngine import GameRisky

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

# Test move action ...
def test_risky_init():
    game= GameRisky()
    assert game.map == "board-4"
    assert game.numberOfPlayers == 1
    game.initialize()
    print(  )
    assert game.playerHand(1).dump() == """Board 1 2 0 8 : A 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 0 : 2 5 15
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

# Test move action ...
def test_risky_action():
    game= GameRisky()
    game.initialize()
    assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 0 : 2 5 15
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

    print( game.board.dump() )
    assert not game.applyPlayerAction(1, "move 1 3 6")
    print( game.board.dump() )
    assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 6
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 0 : 2 5 15
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 1 : 3 1 9
  - Army 1 2 0 0 : A 0 6
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

    assert not game.applyPlayerAction(1, "move 1 2 6")
    print( game.board.dump() )
    assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 0 : 1 5 3
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : A 0 6
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 1 : 3 1 9
  - Army 1 2 0 0 : A 0 6
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

    assert game.applyPlayerAction(1, "sleep")
    print( game.board.dump() )
    assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 0 : 1 5 3
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : A 1 6
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 1 : 3 1 9
  - Army 1 2 0 0 : A 1 6
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

    assert not game.applyPlayerAction(1, "move 2 3 3")
    print( game.board.dump() )
    assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 0 : 1 5 3
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : A 1 3
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 1 : 3 1 9
  - Army 1 2 0 0 : A 0 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

# Test end ...
def test_risky_end():
  game= GameRisky("board-4", 2)
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
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

  assert game.playerArmies() == [0, 12, 12]
  assert game.playerScore( 1 ) == 0
  assert game.playerScore( 2 ) == 0

  game.appendArmy( 1, 4, 6 )

  print(game.board.dump())

  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 12
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 1 : 4 9 9
  - Army 1 2 0 0 : A 0 6
- Edge-4 1 2 0 0 : 4 1 2"""

  assert not game.isEnded()

  assert game.playerArmies() == [0, 18, 12]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -6

  for i in range( game.duration ) :
    game.tic()

  assert game.isEnded()

  game.board.cell(2).children().pop()
  
  # Test winners...
  assert game.activePlayers() == [1]
  assert game.playerArmies() == [0, 18, 0]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -18
  assert game.isEnded()

# Test fight ...
def test_risky_fight():
  game= GameRisky("board-4", 2)
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
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

  # Test winners...
  assert not game.isEnded()

  assert not game.applyPlayerAction(2, "move 2 1 4")
  print( "> Escarmouche:\n" + game.board.dump() )
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 9
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 8
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

  # Test winners...
  assert not game.isEnded()

  assert not game.applyPlayerAction(1, "move 1 2 9")
  print( "> good deffence:\n" + game.board.dump() )
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 0 : 1 5 3
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 1
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

  # Test winners...
  assert game.isEnded()

  game.initialize()
  game.board.cell(2).child( 1 ).setAttribute(2, 2)
  print( "> Re-initialize:\n" + game.board.dump() )
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 12
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : B 1 2
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

  # Test winners...
  assert game.activePlayers() == [1, 2]
  assert not game.isEnded()

  assert not game.applyPlayerAction(1, "move 1 2 11")
  print( "> good deffence:\n" + game.board.dump() )
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
- Cell-1 1 2 0 1 : 1 5 3
  - Army 1 2 0 0 : A 1 1
- Edge-1 1 3 0 0 : 1 2 3 4
- Cell-2 1 2 0 1 : 2 5 15
  - Army 1 2 0 0 : A 0 11
- Edge-2 1 3 0 0 : 2 1 3 4
- Cell-3 1 2 0 0 : 3 1 9
- Edge-3 1 2 0 0 : 3 1 2
- Cell-4 1 2 0 0 : 4 9 9
- Edge-4 1 2 0 0 : 4 1 2"""

  print(  game.activePlayers() )

  # Test winners...
  assert game.activePlayers() == [1]
  assert game.isEnded()


# Test end ...
def test_risky_grow():
  game= GameRisky("board-4", 2)
  assert game.map == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()
  print( game.board.dump() )
  assert game.board.dump() == """Board 1 2 0 8 : board-4 1 4
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

  game.actionGrow(1, 1)

  assert game.board.cell(1).dump() == """Cell-1 1 2 0 1 : 1 5 3
- Army 1 2 0 0 : A 0 13"""

  game.applyPlayerAction(1, "grow 1")

  assert game.board.cell(1).dump() == """Cell-1 1 2 0 1 : 1 5 3
- Army 1 2 0 0 : A 0 13"""

  game.applyPlayerAction(1, "sleep")
  game.applyPlayerAction(1, "move 1 3 6")
  game.applyPlayerAction(1, "grow 1")

  assert game.board.cell(1).dump() == """Cell-1 1 2 0 1 : 1 5 3
- Army 1 2 0 0 : A 0 9"""

if __name__ == "__main__" :
  pass #test_risky_end()