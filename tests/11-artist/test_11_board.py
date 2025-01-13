import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.artist as hka
import src.hacka.board as hkb

def compareSvg( img1, img2 ):
    shotFile= open( img1 ) 
    refsFile= open( img2 ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_artist_tile():
    shotImg= "tests/outputs/shot-11-artist-tile.svg"
    pablo= hka.Artist( hka.SupportSVG( filePath= shotImg ) )
    tile= hkb.Tile()
    
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-tile-01.svg" )

    tile= hkb.Tile( 3, 0, (1.3, 0.9), 4.0 )
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-tile-02.svg" )

    tile= hkb.Tile( 1, 1 ).setShapeRegular( (0.4, 0.2), 2.0, 6 )
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-tile-03.svg" )

#    pablo= hka.Artist( hka.SupportSVG() )

