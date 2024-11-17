# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka.core  import Pod
from src.hacka.board import Tile

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - C O M P O N E N T
# ------------------------------------------------------------------------ #

def test_Tile_init():
    
    tile= Tile()

    assert tile.number() == 0
    assert tile.center() == (0.0, 0.0)
    assert tile.limits() == [(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]
    assert tile.adjacencies() == []
    assert tile.pieces() == []
    
    tile= Tile( 3, (10.3, 9.7), 42.0 )

    assert tile.number() == 3
    assert tile.stamp() == 0
    assert tile.center() == (10.3, 9.7)
    assert tile.limits() == [(-10.7, 30.7), (31.3, 30.7), (31.3, -11.3), (-10.7, -11.3)]
    assert tile.adjacencies() == []
    assert tile.pieces() == []

    tile.setNumber(1).setStamp(8).setShapeSquare( (1.0, 1.0), 2.0 )

    assert tile.number() == 1
    assert tile.stamp() == 8
    assert tile.center() == (1.0, 1.0)
    assert tile.limits() == [(0.0, 2.0), (2.0, 2.0), (2.0, 0.0), (0.0, 0.0)]
    assert tile.adjacencies() == []
    assert tile.pieces() == []

def test_Tile_regular():
    tile= Tile( 1 ).setShapeRegular( (10.0, 10.0), 20.0, 6 )
    assert tile.number() == 1
    assert tile.center() == (10.0, 10.0)
    assert len(tile.limits()) == 6
    limits= [ ( round(x, 2), round(y, 2) ) for x, y in tile.limits() ]
    assert limits == [
        (1.34, 15.0), (10.0, 20.0),
        (18.66, 15.0), (18.66, 5.0),
        (10.00, 0.0), (1.34, 5.0)]

def test_Tile_adjencies():
    tile= Tile(1)
    assert tile.adjacencies() == []
    tile.connect( 2 )
    assert tile.adjacencies() == [2]
    tile.connectAll( [3, 4] )
    assert tile.adjacencies() == [2, 3, 4]

def test_Tile_pieces():
    tile= Tile(1)
    assert tile.pieces() == []
    
    tile.append( Pod('Piece', 'dragon', [10, 3], [22.0]) )

    assert len(tile.pieces()) == 1
    assert tile.piece(1) == Pod('Piece', 'dragon', [10, 3], [22.0])
    
    tile.clear()
    assert tile.pieces() == []

def test_Tile_str():
    tile= Tile(8, (18.5, 4.07))
    print(f">>> {tile}")
    assert str(tile) == "Tile-8/0 center: (18.5, 4.07) limits: [(18.0, 4.57), (19.0, 4.57), (19.0, 3.57), (18.0, 3.57)] adjs: [] pieces(0)"
    tile.setStamp(2).connectAll( [1, 2, 3] )
    print(f">>> {tile}")
    assert str(tile) == "Tile-8/2 center: (18.5, 4.07) limits: [(18.0, 4.57), (19.0, 4.57), (19.0, 3.57), (18.0, 3.57)] adjs: [1, 2, 3] pieces(0)"

def test_Tile_pod():
    tile= Tile( 3, (1.0, 2.0), 2.0 )
    tile._adjacencies= [1, 2, 4]
    print( tile.limits() )
    assert tile.limits() == [(0.0, 3.0), (2.0, 3.0), (2.0, 1.0), (0.0, 1.0)]    
    
    pod= tile.asPod()
    print(f">>> {pod}")
    assert str(pod) == "Tile: [3, 0, 1, 2, 4] [1.0, 2.0, 0.0, 3.0, 2.0, 3.0, 2.0, 1.0, 0.0, 1.0]"
    
    tileBis= Tile().fromPod(pod)
    assert tileBis.number() == 3
    assert tileBis.center() == (1.0, 2.0)
    assert tile.limits() == [(0.0, 3.0), (2.0, 3.0), (2.0, 1.0), (0.0, 1.0)]
    assert tileBis.adjacencies() == [1, 2, 4]
    assert tileBis.asPod() == tile.asPod()

def test_Tile_load():
    tile= Tile( 3, (1.4, 2.0), 1.0, 9)
    assert tile.stamp() == 9
    tile.connectAll( [1, 2, 4] )
    tileBis= Tile().load( tile.dump() )
    print( tile )
    print( tileBis )
    assert tileBis.asPod() == tile.asPod()
