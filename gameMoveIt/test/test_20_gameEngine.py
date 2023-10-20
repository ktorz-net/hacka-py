"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def test_construct():
    game= ge.GameMoveIt()
    print( game.board().shell() )
    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    for i, robot in zip( range(3), game.robots() ) :
         assert( robot.position() == ( i%6, i//6 ) )
         assert( robot.goal() == ( i%6, i//6 ) )

def test_initialize():
    game= ge.GameMoveIt(38)
    podInit= game.initialize()
    print( game.board().shell() )
    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)