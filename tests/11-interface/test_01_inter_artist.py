import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.interface as hki

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_artist_load():
    pablo= hki.Artist()
    assert type( pablo ) == hki.Artist

    pablo.tracePoint( 22.0, -8 )
    pablo.traceLine( 22.0, -8, 14.5, 3.4 )
    pablo.traceCircle( 22.0, -8, 14.7 )
    pablo.fillCircle( 22.0, -8, 14.7 )
    pablo.drawCircle( 22.0, -8, 14.7 )
    pablo.tracePolygon( [22.0, -8, 14.7], [12.0, 8, 4.1] )
    pablo.fillPolygon( [22.0, -8, 14.7], [12.0, 8, 4.1] )
    pablo.drawPolygon( [22.0, -8, 14.7], [12.0, 8, 4.1] )
    pablo.drawFrameGrid()
    pablo.drawFrameAxes()
