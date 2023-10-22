"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge
from gameMoveIt.playerInteractive import PlayerShell

def debug( aString ):
    print("<--")
    for line in aString.split("\n") :
        print( '"'+ line + '",')
    print("-->")

def test_playerInteractive():
    game= ge.GameMoveIt(42)
    initPod= game.initialize()

    player= PlayerShell()
    player.wakeUp( 1, 1, initPod )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         ███████████         █         █         █",
"     █         █         ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▀▜████████▙▄   ▖▝   ▘▗  ",
"     █         ███████████         █         ███████████         █",
"     █         ███████████         █         ███████████         █",
"  ▄▟███▙▄   ▖▝▁▁▁▀▜███▛▀▁▁▁▘▗   ▄▟███▙▄   ▖▝▁▁▁▀▜███▛▀   ▘▗   ▖▝  ",
"███████████  ⎛R  ⎞  █  ⎛H  ⎞  ███████████  ⎛H  ⎞  █         █     ",
"███████████  ⎝  1⎠  █  ⎝  2⎠  ███████████  ⎝  3⎠  █         █     ",
"  ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( player._board.shell() )
    for l1, l2 in zip( player._board.shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( len(player._mobiles) == 3 )
    assert( str( player._mobiles[0] ) == "Robot-1[on(1, 0), dir(0), error(0.0)]" )
    assert( str( player._mobiles[1] ) == "Human-2[on(2, 0), dir(0), error(0.0)]" )
    assert( str( player._mobiles[2] ) == "Human-3[on(4, 0), dir(0), error(0.0)]" )

    assert( player._countTic == 0 )
    assert( player._countCycle == 0 )
    assert( player._score == 0 )

    player.perceive( game.playerHand(1) )

    assert( len(player._mobiles) == 3 )
    assert( str( player._mobiles[0] ) == "Robot-1[on(0, 1), dir(0), goal(0, 3)-F, error(0.0)]" )
    assert( str( player._mobiles[1] ) == "Human-2[on(5, 0), dir(0), error(0.0)]" )
    assert( str( player._mobiles[2] ) == "Human-3[on(4, 0), dir(0), error(0.0)]" )

    assert( player._countTic == 16 )
    assert( player._countCycle == 10 )
    assert( player._score == 0 )