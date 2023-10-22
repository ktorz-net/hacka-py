"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def debug( aString ):
    print("<--")
    for line in aString.split("\n") :
        print( '"'+ line + '",')
    print("-->")

def test_construct():
    game= ge.GameMoveIt(42)
    game.initialize()
    
    assert( game.mobile(1).isRobot() )
    assert( not game.mobile(1).isHuman() )
    assert( not game.mobile(2).isRobot() )
    assert( game.mobile(2).isHuman() )
    assert( game.mobile(3).isHuman() )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▄▟███▙▄  ",
"     ███████████         █         ███████████████████████████████",
"     ███████████         █         ███████████████████████████████",
"  ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▀▜███▛▀   ▀▜███▛▀   ▀▜███▛▀  ",
"█         █         █         █  ⎛R  ⎞  █         █         █     ",
"█         █         █         █  ⎝  1⎠  █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █ ⎡     ⎤ █ ⎡     ⎤ █         █         █",
"     █         █         █ ⎣     ⎦2█ ⎣     ⎦3█         █         █",
"  ▖▝▁▁▁▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█  ⎛H  ⎞  █  ⎛H  ⎞  █████████████████████ ⎡     ⎤ █         █     ",
"█  ⎝  3⎠  █  ⎝  2⎠  █████████████████████ ⎣     ⎦1█         █     ",
"  ▘▗▔▔▔▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( str(game.mobile(1)) == "Robot-1[on(3, 2), dir(0), goal(4, 0)-F, error(0.0)]" )
    assert( str(game.mobile(2)) == "Human-2[on(1, 0), dir(0), goal(2, 1)-F, error(0.15)]" )
    assert( str(game.mobile(3)) == "Human-3[on(0, 0), dir(0), goal(3, 1)-F, error(0.15)]" )


def test_gameEngine():

    game= ge.GameMoveIt(42)
    game.initialize()
    hand= game.playerHand(1)

    test= [
"moveIt: [16, 10, 0]",
"- Robot: 1 [3, 2, 0, 4, 0, 0]",
"- Human: 2 [1, 0, 0]",
"- Human: 3 [0, 0, 0]"]
    #debug( str(hand) )
    for l1, l2 in zip( str(hand).split("\n"), test ) :
        assert( l1 == l2)
    
    game.mobile(2).setError(0.0)
    game.mobile(3).setError(0.0)

    assert( str( game.mobile(1) ) == "Robot-1[on(3, 2), dir(0), goal(4, 0)-F, error(0.0)]" )
    assert( str( game.mobile(2) ) == "Human-2[on(1, 0), dir(0), goal(2, 1)-F, error(0.0)]" )
    assert( str( game.mobile(3) ) == "Human-3[on(0, 0), dir(0), goal(3, 1)-F, error(0.0)]" )

    assert( game.applyPlayerAction( 1, "move 5" ) )
    game.tic()

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▄▟███▙▄  ",
"     ███████████         █         ███████████████████████████████",
"     ███████████         █         ███████████████████████████████",
"  ▖▝   ▀▜███▛▀   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▀▜███▛▀  ",
"█         █         █  ⎛R  ⎞  █         █         █         █     ",
"█         █         █  ⎝  1⎠  █         █         █         █     ",
"  ▘▗   ▖▝▁▁▁▘▗   ▖▝▁▁▁▘▗▔▔▔▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █  ⎛H  ⎞  █  ⎛H  ⎞  █ ⎡     ⎤ █ ⎡     ⎤ █         █         █",
"     █  ⎝  3⎠  █  ⎝  2⎠  █ ⎣     ⎦2█ ⎣     ⎦3█         █         █",
"  ▖▝   ▘▗▔▔▔▖▝   ▘▗▔▔▔▄▟███▙▄   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █████████████████████ ⎡     ⎤ █         █     ",
"█         █         █████████████████████ ⎣     ⎦1█         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.score() == 0 )
    hand= game.playerHand(1)

    test= [
"moveIt: [16, 10, 0]",
"- Robot: 1 [2, 2, 5, 4, 0, 0]",
"- Human: 2 [1, 1, 1]",
"- Human: 3 [0, 1, 1]"]

    #debug( str(hand) )
    for l1, l2 in zip( str(hand).split("\n"), test ) :
        assert( l1 == l2)

    assert( game.applyPlayerAction( 1, "move 2" ) )
    game.tic()
    assert( game.score() == 0 )

    assert( game.applyPlayerAction( 1, "move 2" ) )
    game.tic()
    assert( game.score() == 0 )

    assert( game.applyPlayerAction( 1, "move 3" ) )
    game.tic()
    assert( game.score() == 0 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▄▟███▙▄  ",
"     ███████████         █         ███████████████████████████████",
"     ███████████         █         ███████████████████████████████",
"  ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▀▜███▛▀  ",
"█         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗  ",
"     █         █  ⎛H  ⎞  █ ⎡⎛H  ⎞⎤ █ ⎡     ⎤ █  ⎛R  ⎞  █         █",
"     █         █  ⎝  3⎠  █ ⎣⎝  2⎠⎦2█ ⎣     ⎦3█  ⎝  1⎠  █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄▔▔▔▄▟███▙▄   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝  ",
"█         █         █████████████████████ ⎡     ⎤ █         █     ",
"█         █         █████████████████████ ⎣     ⎦1█         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.applyPlayerAction( 1, "move 4" ) )
    game.tic()
    assert( game.score() == 12 )
    assert( game._countDownCycle == 9 )

    game.mobile(1).setGoal( 4, 0 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▄▟███▙▄  ",
"     ███████████         █         ███████████████████████████████",
"     ███████████         █         ███████████████████████████████",
"  ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▀▜███▛▀  ",
"█ ⎡     ⎤ █         █         █ ⎡     ⎤ █         █         █     ",
"█ ⎣     ⎦3█         █         █ ⎣     ⎦2█         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █  ⎛H  ⎞  █  ⎛H  ⎞  █         █         █         █",
"     █         █  ⎝  3⎠  █  ⎝  2⎠  █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄▔▔▔▄▟███▙▄   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █████████████████████ ⎡⎛R  ⎞⎤ █         █     ",
"█         █         █████████████████████ ⎣⎝  1⎠⎦1█         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.applyPlayerAction( 1, "move 0" ) )
    game.tic()
    assert( game.score() == 28 )
    assert( game._countDownCycle == 8 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▄▟███▙▄  ",
"     ███████████         █         ███████████████████████████████",
"     ███████████         █         ███████████████████████████████",
"  ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▀▜███▛▀   ▀▜███▛▀   ▀▜███▛▀  ",
"█ ⎡     ⎤ █         █         █  ⎛H  ⎞  █         █         █     ",
"█ ⎣     ⎦1█         █         █  ⎝  2⎠  █         █         █     ",
"  ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █  ⎛H  ⎞  █         █         █         █         █         █",
"     █  ⎝  3⎠  █         █         █         █         █         █",
"  ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▄▟███▙▄   ▄▟███▙▄   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █████████████████████ ⎡⎛R  ⎞⎤ █ ⎡     ⎤ █     ",
"█         █         █████████████████████ ⎣⎝  1⎠⎦3█ ⎣     ⎦2█     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

def test_sleep():
    game= ge.GameMoveIt(42)
    game.initialize()
    hand= game.playerHand(1)
    
    assert( game.score() == 0 )
    assert( game._countDownCycle == 10 )

    assert( game.applyPlayerAction( 1, "sleep" ) )
    game.tic()

    assert( game.score() == 0 )
    assert( game._countDownCycle == 9 )

