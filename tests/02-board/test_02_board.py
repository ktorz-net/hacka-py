# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka.pylib.pod import Pod
from src.hacka.board import Tile, Board 

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - C O M P O N E N T
# ------------------------------------------------------------------------ #

def test_Board_init():
    tile= Tile(42)
    assert tile.number() == 42
    
    board= Board(3)
    assert board.tile(1).number() == 1
    assert board.tile(2).number() == 2
    assert board.tile(3).number() == 3
    assert board.tiles() == [ board.tile(1), board.tile(2), board.tile(3) ]
    assert board.edges() == []

    assert board.tile(1).center() == (0.0, 0.0)
    assert board.tile(1).envelope() == [(-0.45, 0.45), (0.45, 0.45), (0.45, -0.45), (-0.45, -0.45) ]

    assert board.tile(2).center() == (1.0, 0.0)
    env= [ (round(x, 2), round(y, 2)) for x, y in board.tile(2).envelope() ]
    assert env == [(0.55, 0.45), (1.45, 0.45), (1.45, -0.45), (0.55, -0.45)]

    assert board.tile(3).center() == (2.0, 0.0)
    env= [ (round(x, 2), round(y, 2)) for x, y in board.tile(3).envelope() ]
    assert env == [(1.55, 0.45), (2.45, 0.45), (2.45, -0.45), (1.55, -0.45)]
    
def test_Board_construction():
    board= Board(3)
    assert board.tile(1).adjacencies() == []
    assert board.tile(2).adjacencies() == []
    assert board.tile(3).adjacencies() == []
    board.connect(1, 2)
    board.connect(1, 3)
    board.connect(2, 2)
    board.connect(2, 1)
    board.connect(3, 1)
    board.connect(3, 2)
    board.connect(3, 3)
    assert board.tile(1).adjacencies() == [2, 3]
    assert board.tile(2).adjacencies() == [1, 2]
    assert board.tile(3).adjacencies() == [1, 2, 3]
    assert board.edges() == [ (1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3) ]
    idBoard= id(board)
    board.__init__(3)
    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )
    print(f">>> {board.edges()}")
    assert( idBoard == id(board) )
    assert board.edges() == [ (1, 1), (1, 3), (2, 1), (2, 2), (3, 2) ]


def test_Board_str():
    board= Board(3)
    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )
    board.tile(2).append( Pod('Piece', 'dragon', [10, 3], [22.0]) )

    print( f">>> {board}." )

    assert "\n"+str(board)+"\n" == """
Board:
- Tile-1/0 center: (0.0, 0.0) adjs: [1, 3] pieces(0)
- Tile-2/0 center: (1.0, 0.0) adjs: [1, 2] pieces(1)
  - Piece: dragon [10, 3] [22.0]
- Tile-3/0 center: (2.0, 0.0) adjs: [2] pieces(0)
"""

def test_Board_pod():
    board= Board(4)
    board.connectAll( [ [1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4],
                       [3, 1], [3, 2], [4, 1], [4, 2]
                        ] )

    board.tile(1).setCenter( 5.0, 3.0 )
    board.tile(2).setCenter( 5.0, 15.0 )
    board.tile(3).setCenter( 1.0, 9.0 )
    board.tile(4).setCenter( 9.0, 9.0 )

    boardPod= board.asPod()

    print(f">>> {boardPod}")
    assert '\n'+ str(boardPod) +'\n' == """
Board:
- Tile: [1, 0, 2, 3, 4] [5.0, 3.0, -0.45, 0.45, 0.45, 0.45, 0.45, -0.45, -0.45, -0.45]
- Tile: [2, 0, 1, 3, 4] [5.0, 15.0, 0.55, 0.45, 1.45, 0.45, 1.45, -0.45, 0.55, -0.45]
- Tile: [3, 0, 1, 2] [1.0, 9.0, 1.55, 0.45, 2.45, 0.45, 2.45, -0.45, 1.55, -0.45]
- Tile: [4, 0, 1, 2] [9.0, 9.0, 2.55, 0.45, 3.45, 0.45, 3.45, -0.45, 2.55, -0.45]
"""

    print(f">>> {boardPod.dump()}")
    assert '\n'+ boardPod.dump() +'\n' == """
Board - 0 0 0 4 :
Tile - 0 5 10 0 : 1 0 2 3 4 5.0 3.0 -0.45 0.45 0.45 0.45 0.45 -0.45 -0.45 -0.45
Tile - 0 5 10 0 : 2 0 1 3 4 5.0 15.0 0.55 0.45 1.45 0.45 1.45 -0.45 0.55 -0.45
Tile - 0 4 10 0 : 3 0 1 2 1.0 9.0 1.55 0.45 2.45 0.45 2.45 -0.45 1.55 -0.45
Tile - 0 4 10 0 : 4 0 1 2 9.0 9.0 2.55 0.45 3.45 0.45 3.45 -0.45 2.55 -0.45
"""


def test_Board_copy():
    board= Board(3)

    board.connectAll( [ [1, 3], [1, 1], [2, 2], [2, 1], [3, 2], [3, 2] ] )

    boardBis= board.copy()

    board.connect(3, 1)

    assert type(board) == type(boardBis)
    assert boardBis.size() == 3
    assert boardBis.edges() == [ (1, 1), (1, 3), (2, 1), (2, 2), (3, 2) ]

def t_est_Board_connection():
    board= board.Board(3)
    board.connect(1, 2)
    board.connect(2, 2)
    board.connect(2, 3)
    board.connect(3, 2)
    assert "\n"+str(board) == """
Board
- tile-1
- Edge-1 [2]
- tile-2
- Edge-2 [2, 3]
- tile-3
- Edge-3 [2]"""

    assert board.edgesFrom(1) == [2]
    assert board.edgesFrom(2) == [2, 3]
    assert board.edgesFrom(3) == [2]
    
    assert board.isEdge(1, 2)
    assert board.isEdge(2, 2)
    assert board.isEdge(3, 2)
    assert not board.isEdge(2, 1)
    assert not board.isEdge(1, 3)
    assert not board.isEdge(3, 1)
  
def t_est_Board_iterator():
    board= Board(3)
    board.connect(1, 2)
    board.connect(2, 2)
    board.connect(2, 3)
    board.connect(3, 2)

    ref= [
        [ "tile-1", [2]],
        [ "tile-2", [2, 3]],
        [ "tile-3", [2] ]
    ]
    i= 0
    for tile, edges in board :
        assert board.itile() == i+1
        assert str(tile) == ref[i][0]
        assert edges == ref[i][1]
        i+=1
