"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

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