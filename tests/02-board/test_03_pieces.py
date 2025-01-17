# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka.pylib.pod import Pod
from src.hacka.tiled import Tile, Board, Piece

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - C O M P O N E N T
# ------------------------------------------------------------------------ #

def test_Piece_init():
    piece= Piece("42")
    assert piece.name() == "42"
    assert piece.type() == 0
    assert piece.center() == (0.0, 0.0)
    env= [ (round(x, 2), round(y, 2)) for x, y in piece.envelope() ]
    print(env)
    assert env == [
        (-0.23, 0.1), (-0.1, 0.23), (0.1, 0.23), (0.23, 0.1),
        (0.23, -0.1), (0.1, -0.23), (-0.1, -0.23), (-0.23, -0.1)
    ]
    