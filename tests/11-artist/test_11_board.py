import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.artist as hka
import src.hacka.tiled as hkb

def compareSvg( img1, img2 ):
    shotFile= open( img1 ) 
    refsFile= open( img2 ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #
shotImg= "shot-test.svg"

# Test artist on tiles
def test_artist_tile():
    pablo= hka.Artist().initializeSVG( filePath= shotImg )
    tile= hkb.Tile()
    
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-tile-01.svg" )

    tile= hkb.Tile( 3, 0, (1.3, 0.9), 4.0 )
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-tile-02.svg" )

    tile= hkb.Tile( 1, 1 ).setShapeRegular( (0.4, 0.2), 2.0, 6 )
    pablo.drawTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-tile-03.svg" )

    pablo.drawTile( tile )
    pablo.writeTile( tile )
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-tile-04.svg" )

# Test artist on board
def test_artist_board_tiles():
    pablo= hka.Artist().initializeSVG( filePath= shotImg )
    board= hkb.Board()
    
    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-00.svg" )
    
    board= hkb.Board(3)

    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-01.svg" )

    pablo.setCamera( 1.1, 0.0 )
    pablo.setScale( 200 )

    pablo.drawBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-02.svg" )

def test_artist_board_net():
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

    compareSvg( shotImg, "tests/refs/11.11-artist-board-11.svg" )
    
    board.connectAll( [ [1, 2], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4] ] )

    pablo.drawBoardNetwork(board)
    pablo.writeBoardTiles(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-12.svg" )
   
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-13.svg" )

def test_artist_board_net():
    pablo= hka.Artist().initializeSVG( filePath= shotImg )
    board= hkb.Board()
    board.initializeSquares(
       [[0, 1, 1, -1, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, -1, 0, 1, 1, 0],
        [0, 0, 0, -1, 0, 0, 1, 0],
        [-1, -1, 0, 0, 0, -1, -1, -1]]
    )

    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-14.svg" )

    box= [ (round(x, 2), round(y, 2)) for x, y in board.box() ]
    assert box == [(-0.5, -0.5), (8.2, 4.9)] 

    pablo.fitBox( board.box() )
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-15.svg" )

    board.connectAllCondition(
        lambda tileFrom, tileTo : tileTo.type() == 0 and tileFrom.centerDistance( tileTo ) < 1.2,
        lambda tileFrom : tileFrom.type() == 0,
    )
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-board-16.svg" )


# Test artist on board
def test_artist_board_piece():
    pablo= hka.Artist().initializeSVG( filePath= shotImg )
    board= hkb.Board()
    board.initializeSquares(
       [[0, 1, 1, -1, 0, 0, 0, 0],
        [5, -1, 0, 2, 0, -1, 5, 0],
        [0, 0, 0, -1, 0, 1, 1, 0],
        [0, 4, 0, -1, 0, 2, 1, 6],
        [-1, -1, 0, 0, 0, -1, -1, -1]]
    )
    board.connectAllCondition(
        lambda tileFrom, tileTo : tileFrom.centerDistance( tileTo ) < 1.2,
    )

    pablo.fitBox( board.box() )
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-piece-01.svg" )

    board.tile(12).addPiece( hkb.Piece("R1.1", 3, (0.0, 0.0), 0.6) )
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-piece-02.svg" )

    board.tile(9).addPiece( hkb.Piece("R1.1", 3, (0.0, 0.0), 0.6) )
    board.tile(14).addPiece( hkb.Piece("R2.2", 5, (0.0, 0.0), 0.6) )
    board.tile(23).addPiece( hkb.Piece("R1.2", 3, (0.0, 0.0), 0.6) )
    board.tile(20).addPiece( hkb.Piece("R2.1", 5, (0.0, 0.0), 0.6) )

    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-piece-03.svg" )

    board.tile(17).addPiece( hkb.Piece("ViP1", 1, (0.0, 0.0), 0.6) )

    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-piece-04.svg" )

    for tile in board.tiles() :
        tile.clear()
    
    pablo.drawBoard(board)
    pablo.flip()

    compareSvg( shotImg, "tests/refs/11.11-artist-piece-01.svg" )
