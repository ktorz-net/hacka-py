# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('hackapy')[0] )

import hackapy.pieceOfData as pod

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - T E S T   D R A F T
# ------------------------------------------------------------------------ #

def test_Pod_load():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    assert gamel.dump() == "9 2 0 0 : SouriCity 3 8"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "9 2 0 0 : SouriCity 3 8"
