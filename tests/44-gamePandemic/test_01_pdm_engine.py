import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

import src.hacka.py as hk
import src.hacka.games.pandemic as pdm

def test_gameMethod():
    game= pdm.GameEngine()

    assert( type( game.initialize().asPod() ) is hk.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hk.Pod )
    assert( game.applyPlayerAction( 1, "test" )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )


def test_gridCell():

    game= pdm.GameEngine()

    assert len( game.grid() ) == 1
    assert len( game.grid()[0] ) == 1

    print(game.grid()[0][0])
    assert str( game.grid()[0][0] ) == "[1, 0]"


def test_initGridCell():
    game= pdm.GameEngine()
    game.initGridFull( 3, 4, 20 )

    assert len( game.grid() ) == 3
    i= 10
    for line in game.grid() :
        assert len(line) == 4
        for cell in line :
            assert type(cell) == pdm.engine.Cell
            cell.setPopulation(i)
            i+= 10

    print(game)
    assert "\n"+str( game ) == """
|[10, 0], [20, 0], [30, 0], [40, 0]|
|[50, 0], [60, 0], [70, 0], [80, 0]|
|[90, 0], [100, 0], [110, 0], [120, 0]|"""

    pod= game.initialize()

    assert str(pod) =="""Pandemic: 10 [10]
- Line:
  - Cell: 0 [10, 0]
  - Cell: 0 [20, 0]
  - Cell: 0 [30, 0]
  - Cell: 0 [40, 0]
- Line:
  - Cell: 0 [50, 0]
  - Cell: 0 [60, 0]
  - Cell: 0 [70, 0]
  - Cell: 0 [80, 0]
- Line:
  - Cell: 0 [90, 0]
  - Cell: 0 [100, 0]
  - Cell: 0 [110, 0]
  - Cell: 0 [120, 0]"""

    assert game.cell(1, 4).population() == 40
    assert game.cell(2, 2).population() == 60

    """
1:  1   2   3
2:    1   2   3
3:  1   2   3
"""

    print( '\n'.join( [str(line) for line in game.neighbor(2, 2) ] ) )
    assert game.neighbor(2, 2) == [[(1, 2), (1, 3)],
                                [(2, 1), (2, 3)],
                                [(3, 2), (3, 3)]]