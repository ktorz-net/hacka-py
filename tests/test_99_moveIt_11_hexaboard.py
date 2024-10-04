import sys, pathlib
workdir= str( pathlib.Path( __file__ ).parent.parent )
sys.path.insert( 1, workdir )

"""
Test - MoveIt Games Class
"""

import src.hacka.pylib as hk
import src.hacka.games.moveIt as game

def test_Hexaboard():
    board= ge.Hexaboard()
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (8, 6) )
    #print( board.shell() )
    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔         ▔         ▔          "]

    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

def test_Obstacles():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(2, 1).setObstacle()

    assert( board.at(0, 0).type() == ge.Cell.TYPE_FREE )
    assert( board.at(2, 1).type() == ge.Cell.TYPE_OBSTACLE )
    assert( board.at(2, 2).type() == ge.Cell.TYPE_FREE )
    assert( board.at(2, 0).type() == ge.Cell.TYPE_FREE )
    assert( board.at(3, 2).type() == ge.Cell.TYPE_FREE )

    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗  ",
"     █         █         ███████████         █",
"     █         █         ███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

    board.at(0, 0).setObstacle()
    board.at(1, 0).setObstacle()
    board.at(1, 1).setObstacle()
    board.at(2, 1).setFree()

    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         ███████████         █         █",
"     █         ███████████         █         █",
"  ▄▟███▙▄   ▄▟████████▛▀   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)
    
    options= board.cellsType( ge.Cell.TYPE_FREE )
    assert( options == [(2, 0), (3, 0), (0, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2)] )

    board.at(0, 1).setObstacle()
    board.at(0, 2).setObstacle()
    board.at(1, 2).setObstacle()
    board.at(3, 1).setObstacle()
    
    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▄▟███▙▄   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜██████████████████▙▄   ▖▝   ▘▗   ▄▟███▙▄  ",
"     █████████████████████         ███████████",
"     █████████████████████         ███████████",
"  ▄▟██████████████████▛▀   ▘▗   ▖▝   ▀▜███▛▀  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

    options= board.cellsType( ge.Cell.TYPE_FREE )
    assert( options == [(2, 0), (3, 0), (2, 1), (2, 2), (3, 2)] )

    board.clear()
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █",
"     █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)


def test_ObstaclesOk():
    board= ge.Hexaboard(4, 3)

    board.at(0, 0).setObstacle()
    board.at(1, 0).setObstacle()
    board.at(1, 1).setObstacle()

    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         ███████████         █         █",
"     █         ███████████         █         █",
"  ▄▟███▙▄   ▄▟████████▛▀   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( board.isObstacleOkAt(0, 0) == False )
    assert( board.isObstacleOkAt(2, 1) == True )
    assert( board.isObstacleOkAt(1, 2) == False )
    assert( board.isObstacleOkAt(2, 2) == False )
    assert( board.isObstacleOkAt(0, 2) == True )
    assert( board.isObstacleOkAt(0, 1) == True )
    assert( board.isObstacleOkAt(0, 1) == True )


def test_path():
    board= ge.Hexaboard(4, 3)

    board.at(0, 0).setObstacle()
    board.at(1, 0).setObstacle()
    board.at(1, 1).setObstacle()

    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         ███████████         █         █",
"     █         ███████████         █         █",
"  ▄▟███▙▄   ▄▟████████▛▀   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( board.path( 0, 1, 0, 2 ) == [6] )
    assert( board.path( 0, 1, 1, 2 ) == [1] )
    assert( board.path( 2, 1, 2, 0 ) == [4] )
    assert( board.path( 2, 1, 2, 1 ) == [0] )
    assert( board.path( 2, 0, 3, 2 ) == [1, 1] )
    assert( board.path( 2, 0, 3, 2 ) == [1, 1] )
    assert( board.path( 0, 1, 2, 0 ) == [1, 2, 3, 4] )
    assert( board.path( 3, 2, 0, 0 ) == [] )
    