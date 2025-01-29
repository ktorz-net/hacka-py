import sys
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

import src.hacka.py as hk
import src.hacka.tiled as hkmap
from src.hacka.games.risky import GameRisky

# Army Attributes
ACTION= 1
FORCE=  2

#------------------------------------------------------------------------------------------------
# Test Map (regarding Risky usage)
#------------------------------------------------------------------------------------------------

gamePath= workdir + "/src/hacka/games/risky"

def test_map_load():
  aPod= hk.Pod()
  map= hkmap.Map()
  print( f">>>> {gamePath}/resources/map-board-4.pod" )
  f= open( f"{gamePath}/resources/map-board-4.pod" )
  aPod.load( f.read() )
  f.close()

  assert f"\n{aPod}\n" == """
Map: board-4
- Tile: [1, 0, 2, 3, 4] [5.0, 3.0]
- Tile: [2, 0, 1, 3, 4] [5.0, 15.0]
- Tile: [3, 0, 1, 2] [1.0, 9.0]
- Tile: [4, 0, 1, 2] [9.0, 9.0]
"""

  map.fromPod( aPod )

  print( f">>> {map}.")
  assert f"\n{map}\n" == """
Map:
- Tile-1/0 center: (5.0, 3.0) adjs: [2, 3, 4] pieces(0)
- Tile-2/0 center: (5.0, 15.0) adjs: [1, 3, 4] pieces(0)
- Tile-3/0 center: (1.0, 9.0) adjs: [1, 2] pieces(0)
- Tile-4/0 center: (9.0, 9.0) adjs: [1, 2] pieces(0)
"""

def test_map_loadAll():
  aPod= hk.Pod()
  map= hkmap.Map()
  for mapName in [ "map-4", "map-6" ] :  
    f= open(f"{gamePath}/resources/map-board-4.pod")
    txt= f.read()
    f.close()
    aPod.load( txt )
    assert aPod.dump() == txt
    
    map.fromPod( aPod )

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------

def test_risky_init():
    game= GameRisky(1)
    assert game.mapName == "board-4"
    assert game.numberOfPlayers == 1
    aPod= game.initialize()

    print(f"<<\n{aPod}\n>>")
    assert f"\n{aPod}\n" == """
Risky: board-4 [1, 4]
- Map:
  - Tile: [1, 0, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Tile: [2, 0, 1, 3, 4] [5.0, 15.0]
  - Tile: [3, 0, 1, 2] [1.0, 9.0]
  - Tile: [4, 0, 1, 2] [9.0, 9.0]
"""

    print(f"<<\n{game.playerHand(1).dump()}\n>>")
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 7 2 0 1 : board-4 1 4
Map - 0 0 0 4 :
Tile - 0 5 2 1 : 1 0 2 3 4 5.0 3.0
Army - 1 2 0 0 : A 1 12
Tile - 0 5 2 0 : 2 0 1 3 4 5.0 15.0
Tile - 0 4 2 0 : 3 0 1 2 1.0 9.0
Tile - 0 4 2 0 : 4 0 1 2 9.0 9.0
"""

    print(f"<<\n{game.playerHand(1)}\n>>")
    assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Map:
  - Tile: [1, 0, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Tile: [2, 0, 1, 3, 4] [5.0, 15.0]
  - Tile: [3, 0, 1, 2] [1.0, 9.0]
  - Tile: [4, 0, 1, 2] [9.0, 9.0]
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_init_6():
    game= GameRisky( 2, "board-6" )
    assert game.mapName == "board-6"
    assert game.numberOfPlayers == 2
    game.initialize()
    
    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 7 2 0 1 : board-6 1 6
Map - 0 0 0 6 :
Tile - 0 6 2 1 : 1 0 2 3 4 5 5.0 3.0
Army - 1 2 0 0 : A 1 12
Tile - 0 6 2 1 : 2 0 1 3 4 6 5.0 15.0
Army - 1 2 0 0 : B 1 12
Tile - 0 4 2 0 : 3 0 1 2 1.0 9.0
Tile - 0 6 2 0 : 4 0 1 2 5 6 9.0 9.0
Tile - 0 5 2 0 : 5 0 1 4 6 13.0 3.0
Tile - 0 5 2 0 : 6 0 2 4 5 13.0 15.0
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_10():
    game= GameRisky( 2, "board-10" )
    assert game.mapName == "board-10"
    assert game.numberOfPlayers == 2
    game.initialize()

    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 8 2 0 1 : board-10 1 10
Map - 0 0 0 10 :
Tile - 0 6 2 1 : 1 0 3 5 7 9 11.0 3.0
Army - 1 2 0 0 : A 1 12
Tile - 0 6 2 1 : 2 0 4 6 8 9 11.0 36.0
Army - 1 2 0 0 : B 1 12
Tile - 0 6 2 0 : 3 0 1 4 5 10 1.0 9.0
Tile - 0 6 2 0 : 4 0 2 3 6 10 1.0 29.0
Tile - 0 5 2 0 : 5 0 1 3 10 7.0 9.0
Tile - 0 5 2 0 : 6 0 2 4 10 7.0 30.0
Tile - 0 4 2 0 : 7 0 1 10 11.0 13.0
Tile - 0 4 2 0 : 8 0 2 10 11.0 26.0
Tile - 0 4 2 0 : 9 0 1 2 15.0 20.0
Tile - 0 8 2 0 : 10 0 3 4 5 6 7 8 7.0 19.0
"""

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_risky_init_12():
    game= GameRisky( 2, "board-12" )
    assert game.mapName == "board-12"
    assert game.numberOfPlayers == 2
    game.initialize()

    print( f"<<\n{game.playerHand(1).dump()}\n>>" )
    assert f"\n{game.playerHand(1).dump()}\n" == """
Risky - 8 2 0 1 : board-12 1 12
Map - 0 0 0 12 :
Tile - 0 6 2 1 : 1 0 3 5 7 9 11.0 3.0
Army - 1 2 0 0 : A 1 12
Tile - 0 6 2 1 : 2 0 4 6 8 10 11.0 36.0
Army - 1 2 0 0 : B 1 12
Tile - 0 4 2 0 : 3 0 1 11 15.0 9.0
Tile - 0 4 2 0 : 4 0 2 11 15.0 31.0
Tile - 0 5 2 0 : 5 0 1 9 12 7.0 9.0
Tile - 0 5 2 0 : 6 0 2 10 12 7.0 30.0
Tile - 0 4 2 0 : 7 0 1 12 11.0 13.0
Tile - 0 4 2 0 : 8 0 2 12 11.0 26.0
Tile - 0 6 2 0 : 9 0 1 5 10 12 1.0 9.0
Tile - 0 6 2 0 : 10 0 2 6 9 12 1.0 29.0
Tile - 0 4 2 0 : 11 0 3 4 15.0 20.0
Tile - 0 8 2 0 : 12 0 5 6 7 8 9 10 7.0 19.0
"""

#------------------------------------------------------------------------------------------------
# Test some accessors...
#------------------------
def test_risky_accessors():
    game= GameRisky(1)
    game.initialize()
    assert not game.isTile(0)
    assert game.isTile(1)
    assert game.isTile(2)
    assert game.isTile(3)
    assert game.isTile(4)
    assert not game.isTile(5)
    assert not game.isTile(42)
    assert not game.isTile(-3)

    assert [2, 3, 4] == game.tile(1).adjacencies()
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
  assert game.mapName == "board-4"
  assert game.numberOfPlayers == 2
  game.initialize()

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Map:
  - Tile: [1, 0, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Tile: [2, 0, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Tile: [3, 0, 1, 2] [1.0, 9.0]
  - Tile: [4, 0, 1, 2] [9.0, 9.0]
"""

  assert game.playerArmies() == [0, 12, 12]
  assert game.playerScore( 1 ) == 0
  assert game.playerScore( 2 ) == 0

  game.popArmy( 1, 4, 1, 6 )

  print( f"<<\n{game.playerHand(1)}\n>>" )
  assert f"\n{game.playerHand(1)}\n" == """
Risky: board-4 [1, 4]
- Map:
  - Tile: [1, 0, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 12]
  - Tile: [2, 0, 1, 3, 4] [5.0, 15.0]
    - Army: B [1, 12]
  - Tile: [3, 0, 1, 2] [1.0, 9.0]
  - Tile: [4, 0, 1, 2] [9.0, 9.0]
    - Army: A [1, 6]
"""

  assert not game.isEnded()

  assert game.playerArmies() == [0, 18, 12]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1

  for i in range( game.duration ) :
    game.tic()

  assert game.isEnded()

  game.map.tile(2).pieces().pop()
  
  # Test winners...
  assert game.activePlayers() == [1]
  assert game.playerArmies() == [0, 18, 0]
  assert game.playerScore( 1 ) == 1
  assert game.playerScore( 2 ) == -1
  assert game.isEnded()

#------------------------------------------------------------------------------------------------
# Test ...
#------------------------