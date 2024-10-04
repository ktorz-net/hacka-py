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
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █         ███████████         █         █         █",
"     █ ⎣     ⎦1█         ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▀▜████████▙▄   ▖▝   ▘▗  ",
"     █  ⎛R  ⎞  ███████████         █         ███████████         █",
"     █  ⎝  1⎠  ███████████         █         ███████████         █",
"  ▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝▁▁▁▀▜███▛▀▁▁▁▘▗   ▖▝  ",
"███████████ ⎡     ⎤ █ ⎡     ⎤ ███████████  ⎛H  ⎞  █  ⎛H  ⎞  █     ",
"███████████ ⎣     ⎦3█ ⎣     ⎦2███████████  ⎝  3⎠  █  ⎝  2⎠  █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗▔▔▔▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( str(game.mobile(1)) == "Robot-1[on(0, 1), dir(0), goal(0, 3)-F, error(0.0)]" )
    assert( str(game.mobile(2)) == "Human-2[on(5, 0), dir(0), goal(2, 0)-F, error(0.15)]" )
    assert( str(game.mobile(3)) == "Human-3[on(4, 0), dir(0), goal(1, 0)-F, error(0.15)]" )


def test_gameEngine():

    game= ge.GameMoveIt(42)
    game.initialize()
    hand= game.playerHand(1)

    test= [
"MoveIt: [16, 10] [0]",
"- Robot: 1 [0, 1, 0, 0, 3, 0]",
"- Human: 2 [5, 0, 0]",
"- Human: 3 [4, 0, 0]"]
    #debug( str(hand) )
    for l1, l2 in zip( str(hand).split("\n"), test ) :
        assert( l1 == l2)
    
    game.mobile(2).setError(0.0)
    game.mobile(3).setError(0.0)

    assert( str( game.mobile(1) ) == "Robot-1[on(0, 1), dir(0), goal(0, 3)-F, error(0.0)]" )
    assert( str( game.mobile(2) ) == "Human-2[on(5, 0), dir(0), goal(2, 0)-F, error(0.0)]" )
    assert( str( game.mobile(3) ) == "Human-3[on(4, 0), dir(0), goal(1, 0)-F, error(0.0)]" )

    assert( game.applyPlayerAction( 1, "move 1" ) )
    game.tic()

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █         ███████████         █         █         █",
"     █ ⎣     ⎦1█         ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █  ⎛R  ⎞  █         █         ███████████         █     ",
"█         █  ⎝  1⎠  █         █         ███████████         █     ",
"  ▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄   ▖▝   ▘▗   ▖▝▁▁▁▀▜████████▙▄   ▖▝   ▘▗  ",
"     █         ███████████         █  ⎛H  ⎞  ███████████         █",
"     █         ███████████         █  ⎝  3⎠  ███████████         █",
"  ▄▟███▙▄   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀▁▁▁▘▗   ▖▝  ",
"███████████ ⎡     ⎤ █ ⎡     ⎤ ███████████         █  ⎛H  ⎞  █     ",
"███████████ ⎣     ⎦3█ ⎣     ⎦2███████████         █  ⎝  2⎠  █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗▔▔▔▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.score() == 0 )
    hand= game.playerHand(1)

    test= [
"MoveIt: [16, 10] [0]",
"- Robot: 1 [1, 2, 1, 0, 3, 0]",
"- Human: 2 [5, 0, 0]",
"- Human: 3 [3, 1, 6]"]
    #debug( str(hand) )
    for l1, l2 in zip( str(hand).split("\n"), test ) :
        assert( l1 == l2)

    assert( game.score() == 0 )
    assert( game.applyPlayerAction( 1, "move 6" ) )
    game.tic()

    assert( game.score() == 15 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡⎛R  ⎞⎤ █         ███████████         █         █ ⎡     ⎤ █",
"     █ ⎣⎝  1⎠⎦2█         ███████████         █         █ ⎣     ⎦1█",
"  ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝▁▁▁▘▗   ▖▝   ▀▜████████▙▄   ▖▝   ▘▗  ",
"     █         ███████████  ⎛H  ⎞  █         ███████████ ⎡     ⎤ █",
"     █         ███████████  ⎝  3⎠  █         ███████████ ⎣     ⎦3█",
"  ▄▟███▙▄   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▄▟███▙▄   ▖▝▁▁▁▀▜███▛▀   ▘▗   ▖▝  ",
"███████████         █         ███████████  ⎛H  ⎞  █         █     ",
"███████████         █         ███████████  ⎝  2⎠  █         █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.applyPlayerAction( 1, "move 2" ) )
    game.tic()

    assert( game.score() == 15 )
    assert( game._countDownCycle == 9 )

    game.mobile(1).setGoal( 1, 3 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █ ⎡⎛R  ⎞⎤ ███████████         █         █         █",
"     █ ⎣     ⎦2█ ⎣⎝  1⎠⎦1███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝▁▁▁▘▗   ▖▝▁▁▁▀▜████████▙▄   ▖▝   ▘▗  ",
"     █         ███████████  ⎛H  ⎞  █  ⎛H  ⎞  ███████████ ⎡     ⎤ █",
"     █         ███████████  ⎝  3⎠  █  ⎝  2⎠  ███████████ ⎣     ⎦3█",
"  ▄▟███▙▄   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"███████████         █         ███████████         █         █     ",
"███████████         █         ███████████         █         █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    assert( game.applyPlayerAction( 1, "move 0" ) )
    game.tic()
    assert( game.score() == 30 )
    assert( game._countDownCycle == 8 )

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █  ⎛R  ⎞  ███████████         █         █         █",
"     █ ⎣     ⎦3█  ⎝  1⎠  ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝▁▁▁▘▗   ▖▝▁▁▁▀▜████████▙▄   ▖▝   ▘▗  ",
"     █         ███████████ ⎡⎛H  ⎞⎤ █  ⎛H  ⎞  ███████████         █",
"     █         ███████████ ⎣⎝  3⎠⎦2█  ⎝  2⎠  ███████████         █",
"  ▄▟███▙▄   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"███████████ ⎡     ⎤ █         ███████████         █         █     ",
"███████████ ⎣     ⎦1█         ███████████         █         █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
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

    assert( game.applyPlayerAction( 1, "pass" ) )
    game.tic()

    assert( game.score() == 0 )
    assert( game._countDownCycle == 9 )

    for i in range(7) :
        assert( game.applyPlayerAction( 1, "pass" ) )
        game.tic()

    assert( game.score() == 0 )
    assert( game._countDownCycle == 2 )
    assert( not game.isEnded() )

    assert( game.applyPlayerAction( 1, "pass" ) )
    game.tic()
    assert( game.applyPlayerAction( 1, "pass" ) )
    game.tic()

    assert( game.score() == 0 )
    assert( game._countDownCycle == 0 )
    assert( game.isEnded() )

def test_copyBoard():
    game= ge.GameMoveIt(42)
    game.initialize()

    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █         ███████████         █         █         █",
"     █ ⎣     ⎦1█         ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▀▜████████▙▄   ▖▝   ▘▗  ",
"     █  ⎛R  ⎞  ███████████         █         ███████████         █",
"     █  ⎝  1⎠  ███████████         █         ███████████         █",
"  ▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝▁▁▁▀▜███▛▀▁▁▁▘▗   ▖▝  ",
"███████████ ⎡     ⎤ █ ⎡     ⎤ ███████████  ⎛H  ⎞  █  ⎛H  ⎞  █     ",
"███████████ ⎣     ⎦3█ ⎣     ⎦2███████████  ⎝  3⎠  █  ⎝  2⎠  █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗▔▔▔▖▝   ▘▗▔▔▔▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    #debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    board= game.board().copy()

    debug( board.shell() )
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)
