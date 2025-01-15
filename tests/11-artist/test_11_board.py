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

# Test artist on tiles
def test_artist_tile():
    shotImg= "shot-11-artist-tile.svg"
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

    pablo.drawTile( tile )
    pablo.writeTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-tile-04.svg" )

# Test artist on board
def test_artist_board_tiles():
    shotImg= "tests/outputs/shot-11-artist-board.svg"
    pablo= hka.Artist( hka.SupportSVG( filePath= shotImg ) )
    board= hkb.Board()
    
    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-00.svg" )
    
    board= hkb.Board(3)
    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-01.svg" )

    pablo.setCamera( 1.1, 0.0 )
    pablo.setScale( 200 )

    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-02.svg" )

def test_artist_board_net():
    shotImg= "shot-11-artist-board.svg"
    pablo= hka.Artist( hka.SupportSVG( filePath= shotImg ) )
    board= hkb.Board()
    
    assert board.addTile( hkb.Tile().setShapeRegular( (-1.0, 0.0), 0.9, 6 ) ) == 1
    assert board.addTile( hkb.Tile( type=1 ).setShapeRegular( (0.0, 0.0), 0.9, 6 ) ) == 2
    assert board.addTile( hkb.Tile().setShapeRegular( (1.0, 0.0), 0.9, 6 ) ) == 3

    assert board.addTile( hkb.Tile().setShapeRegular( (0.5, 0.866), 0.9, 6 ) ) == 4
    assert board.addTile( hkb.Tile().setShapeRegular( (-0.5, -0.866), 0.9, 6 ) ) == 5

    pablo.drawBoardTiles(board)
    pablo.writeBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-11.svg" )
    
    board.connectAll( [ [1, 2], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4] ] )

    pablo.drawBoardNetwork(board)
    pablo.writeBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-12.svg" )
   
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/outputs/refs-11-artist-board-13.svg" )
    