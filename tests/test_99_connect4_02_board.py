"""
Test - Connect4.Engine
"""
import sys

sys.path.insert( 1, __file__.split('hackagames')[0] )
import hackagames.hackapy as hg
import hackagames.gameConnect4.gameEngine as ge

def assert_multiline( text1, text2 ) :
    print( f"--- --- ---\n{text1}\nvs\n{text2}" )
    ml1= text1.split("\n")
    ml2= text2.split('\n')
    assert( len(ml1) == len(ml2) )
    for l1, l2 in zip(ml1, ml2) :
        assert( l1 == l2 )

def test_GridInit():
    grid= ge.Grid()
    assert( type( grid ) is ge.Grid  )
    assert( grid.columnSize() == 7  )
    assert( grid.heightMax() == 6  )

    for c in range( 7 ) : 
        for h in range( 6 ) :
            assert( grid.position(c, h) == 0 )

def test_feelColumn():
    grid= ge.Grid()
    
    assert( grid.height(3) == 0 )
    assert( grid.playerPlay(1, 'D') )
   
    assert( grid.position(3, 0) == 1 )
    for h in range( 1, 6 ) :
        assert( grid.position(3, h) == 0 )

    assert( grid.height(3) == 1 )
    assert( grid.playerPlay(2, 'D') )

    assert( grid.height(3) == 2 )
    assert( grid.playerPlay(1, 'D') )

    assert( grid.height(3) == 3 )
    assert( grid.playerPlay(1, 'D') )

    assert( grid.height(3) == 4 )
    assert( grid.playerPlay(1, 'D') )

    assert( grid.column(3) == [1, 2, 1, 1, 1, 0] )

    assert( grid.height(3) == 5 )
    assert( grid.playerPlay(2, 'D') )

    assert( not grid.playerPlay(1, 'D') )

    assert( grid.column(3) == [1, 2, 1, 1, 1, 2] )

def test_GridStr():
    grid= ge.Grid()

    assert( grid.columnStr(0) == "|   |   |   |   |   |   |   |" )
    
    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "-----------------------------\n"
            "1:O, 2:X" )

    print( f"{grid}\nvs\n{test}" )

    assert_multiline( str(grid), test )

    assert( grid.playerPlay(1, 'A') )
    assert( grid.playerPlay(2, 'D') )

    assert( grid.columnStr(0) == "| O |   |   | X |   |   |   |" )

    assert( grid.playerPlay(1, 'A') )
    assert( grid.playerPlay(2, 'D') )
    assert( grid.playerPlay(1, 'E') )
    assert( grid.playerPlay(2, 'G') )
    assert( grid.playerPlay(1, 'D') )
    assert( grid.playerPlay(2, 'C') )
    assert( grid.playerPlay(1, 'C') )
    assert( grid.playerPlay(2, 'D') )

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   | X |   |   |   |\n"
            "|   |   |   | O |   |   |   |\n"
            "| O |   | O | X |   |   |   |\n"
            "| O |   | X | X | O |   | X |\n"
            "-----------------------------\n"
            "1:O, 2:X" )

    print( f"{grid}\nvs\n{test}" )

    assert_multiline( str(grid), test )

    assert( grid.playerPlay(1, 'D') )
    assert( grid.playerPlay(2, 'F') )
    assert( grid.playerPlay(1, 'E') )
    assert( grid.playerPlay(2, 'D') )

    test= ( "  A   B   C       E   F   G\n"
            "|   |   |   | X |   |   |   |\n"
            "|   |   |   | O |   |   |   |\n"
            "|   |   |   | X |   |   |   |\n"
            "|   |   |   | O |   |   |   |\n"
            "| O |   | O | X | O |   |   |\n"
            "| O |   | X | X | O | X | X |\n"
            "-----------------------------\n"
            "1:O, 2:X" )

    print( f"{grid}\nvs\n{test}" )

    assert_multiline( str(grid), test )

def test_podInterface():
    grid= ge.Grid()

    pod= grid.asPod()
    test= ( "Connect4:\n"
            "- column: A [0, 0, 0, 0, 0, 0]\n"
            "- column: B [0, 0, 0, 0, 0, 0]\n"
            "- column: C [0, 0, 0, 0, 0, 0]\n"
            "- column: D [0, 0, 0, 0, 0, 0]\n"
            "- column: E [0, 0, 0, 0, 0, 0]\n"
            "- column: F [0, 0, 0, 0, 0, 0]\n"
            "- column: G [0, 0, 0, 0, 0, 0]")
    
    assert_multiline( str(pod), test )

    pod.child(4).setFlags( [1,2,0, 0,0,0] )
    pod.pop(7)
    grid.fromPod( pod )

    test= ( "  A   B   C   D   E   F\n"
            "|   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |\n"
            "|   |   |   | X |   |   |\n"
            "|   |   |   | O |   |   |\n"
            "-------------------------\n"
            "1:O, 2:X" )
    
    assert_multiline( str(grid), test )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,1],
        [0,0,0, 0,1,1],
        [0,1,2, 1,2,2],
        [0,2,1, 2,1,1],
        [0,0,0, 0,1,1],
        [0,1,2, 1,1,2]
    ]

    gridBis= ge.Grid().fromPod( grid.asPod() )

    assert( grid._pos == gridBis._pos )

def test_internTools():
    grid= ge.Grid()

    assert( grid.verticals() == [ [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5) ],
                                [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5) ],
                                [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5) ],
                                [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5) ],
                                [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5) ],
                                [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5) ],
                                [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5) ] ] )

    test= [ [ (i, h) for i in range(7) ] for h in range(6) ]

    assert( grid.horizontals() == test )

    assert( grid.diagonalPosStarts() == [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0) ] )
    assert( grid.diagonalNegStarts() == [(0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5) ] )

    assert( grid.diagonalFrom( 0, 0 ) == [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5) ] )
    assert( grid.diagonalFrom( 2, 0 ) == [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4) ] )
    
    assert( grid.diagonalFrom( 0, 5, -1 ) == [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0) ] )
    assert( grid.diagonalFrom( 2, 5, -1 ) == [(2, 5), (3, 4), (4, 3), (5, 2), (6, 1) ] )

def test_tools():
    grid= ge.Grid()

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0]
    ]

    assert( grid.winner() == 0  )
    assert( grid.possibilities() == ['A','B','C','D','E','F','G']  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,1],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,2],
        [0,0,0, 0,0,0],
        [0,0,0, 0,0,0],
        [1,1,1, 1,2,2]
    ]
    
    assert( grid.winner() == 1  )
    assert( grid.possibilities() == ['A','B','C','D','E','F']  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,2],
        [0,0,0, 0,0,0],
        [1,2,1, 2,1,2],
        [1,2,1, 2,1,2],
        [0,0,0, 0,0,0],
        [0,1,2, 1,2,2]
    ]
    
    assert( grid.winner() == 0  )
    assert( grid.possibilities() == ['A','B','C','F','G'] )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,2],
        [0,0,0, 0,0,0],
        [0,0,2, 2,2,2],
        [1,2,1, 2,1,2],
        [0,0,0, 0,0,0],
        [0,1,2, 1,2,2]
    ]
    
    assert( grid.winner() == 2  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,2],
        [0,0,0, 0,0,2],
        [0,1,2, 2,1,2],
        [0,2,1, 2,1,2],
        [0,0,0, 0,0,0],
        [0,1,2, 1,2,2]
    ]
    
    assert( grid.winner() == 2  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,1],
        [0,0,0, 0,1,1],
        [0,1,2, 2,1,2],
        [0,2,1, 2,1,1],
        [0,0,0, 0,1,1],
        [0,1,2, 1,1,2]
    ]
    
    assert( grid.winner() == 1  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,1],
        [0,0,0, 0,1,1],
        [0,1,2, 1,2,2],
        [0,2,1, 2,1,1],
        [0,0,0, 0,1,1],
        [0,1,2, 1,1,2]
    ]
    
    assert( grid.winner() == 1  )

    grid._pos= [
        [0,0,0, 0,0,0],
        [0,0,2, 1,2,1],
        [0,0,0, 2,1,1],
        [0,1,1, 2,2,2],
        [0,2,1, 2,1,2],
        [0,0,0, 0,1,1],
        [0,1,2, 1,1,2]
    ]
    
    assert( grid.winner() == 2  )
