import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

import src.hacka.pylib as hk
import src.hacka.games.connect4 as game

def assert_multiline( text1, text2 ) :
    print( f"--- --- ---\n{text1}\nvs\n{text2}" )
    ml1= text1.split("\n")
    ml2= text2.split('\n')
    assert( len(ml1) == len(ml2) )
    for l1, l2 in zip(ml1, ml2) :
        assert( l1 == l2 )

def test_countTripleAligned():
    grid= game.Grid()
    
    grid._pos[0]= [1, 1, 1, 0, 0, 0]
    grid._pos[1]= [2, 0, 0, 0, 0, 0]
    grid._pos[2]= [2, 0, 0, 0, 0, 0]
    grid._pos[3]= [2, 2, 0, 0, 0, 0]
    grid._pos[4]= [1, 2, 1, 0, 0, 0]
    grid._pos[5]= [2, 0, 0, 0, 0, 0]
    grid._pos[6]= [1, 0, 0, 0, 0, 0]

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "| O |   |   |   | O |   |   |\n"
            "| O |   |   | X | X |   |   |\n"
            "| O | X | X | X | O | X | O |\n"
            "-----------------------------" )

    assert_multiline( str(grid), test )

    assert( grid.countTriple(1) == 1 )
    assert( grid.countTriple(2) == 1 )
    
    grid._pos[0]= [1, 1, 1, 1, 0, 0]
    grid._pos[1]= [2, 0, 0, 0, 0, 0]
    grid._pos[2]= [2, 2, 1, 0, 0, 0]
    grid._pos[3]= [2, 2, 1, 0, 0, 0]
    grid._pos[4]= [1, 2, 1, 2, 2, 2]
    grid._pos[5]= [2, 0, 0, 0, 0, 0]
    grid._pos[6]= [1, 2, 2, 2, 0, 0]

    test= ( "  A   B   C   D       F   G\n"
            "|   |   |   |   | X |   |   |\n"
            "|   |   |   |   | X |   |   |\n"
            "| O |   |   |   | X |   | X |\n"
            "| O |   | O | O | O |   | X |\n"
            "| O |   | X | X | X |   | X |\n"
            "| O | X | X | X | O | X | O |\n"
            "-----------------------------" )

    assert_multiline( str(grid), test )

    assert( grid.countTriple(1) == 3 )
    assert( grid.countTriple(2) == 4 )


def test_countTripleDiags():
    grid= game.Grid()
    
    grid._pos[0]= [1, 1, 0, 0, 0, 0]
    grid._pos[1]= [2, 0, 0, 0, 0, 0]
    grid._pos[2]= [2, 0, 0, 0, 0, 0]
    grid._pos[3]= [2, 2, 0, 0, 0, 0]
    grid._pos[4]= [1, 2, 2, 1, 0, 0]
    grid._pos[5]= [2, 1, 1, 0, 0, 0]
    grid._pos[6]= [1, 1, 0, 0, 0, 0]

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   | O |   |   |\n"
            "|   |   |   |   | X | O |   |\n"
            "| O |   |   | X | X | O | O |\n"
            "| O | X | X | X | O | X | O |\n"
            "-----------------------------" )

    assert_multiline( str(grid), test )

    assert( grid.countTriple(1) == 1 )
    assert( grid.countTriple(2) == 2 )
    
    grid._pos[0]= [1, 1, 0, 0, 0, 0]
    grid._pos[1]= [2, 0, 0, 0, 0, 0]
    grid._pos[2]= [2, 0, 0, 0, 0, 0]
    grid._pos[3]= [2, 2, 0, 0, 0, 0]
    grid._pos[4]= [1, 2, 2, 1, 0, 0]
    grid._pos[5]= [1, 1, 1, 0, 0, 0]
    grid._pos[6]= [1, 1, 1, 0, 0, 0]

    test= ( "  A   B   C   D   E   F   G\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   |   |   |   |\n"
            "|   |   |   |   | O |   |   |\n"
            "|   |   |   |   | X | O | O |\n"
            "| O |   |   | X | X | O | O |\n"
            "| O | X | X | X | O | O | O |\n"
            "-----------------------------" )

    assert_multiline( str(grid), test )

    assert( grid.countTriple(1) == 5 )
    assert( grid.countTriple(2) == 2 )
    