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

def test_move_51():
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

    debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)
    
    game.applyPlayerAction( 1, "move 51" )
    game.tic()

    # Generate Human moves
    human= game._mobiles[game._nbRobots:][0]
    x, y= human.position()
    gx, gy= human.goal()
    dir= game.board().path( x, y, gx, gy )[0]
    tx, ty= game.board().at_dir(x, y, dir)
    
    print( human )
    print( f"-> at {(x, y)} dir({dir}) -> {(tx, ty)} - ({bool(game.board().at(tx, ty).mobile())})" )
    print( f"-> path: {game.board().path( x, y, gx, gy )}" )

    # Generate Human moves
    human= game._mobiles[game._nbRobots:][1]
    x, y= human.position()
    gx, gy= human.goal()
    dir= game.board().path( x, y, gx, gy )[0]
    tx, ty= game.board().at_dir(x, y, dir)
    
    print( human )
    print( f"-> at {(x, y)} dir({dir}) -> {(tx, ty)}" )
    print( f"-> path: {game.board().path( x, y, gx, gy )}" )
    
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

    debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)

    game.applyPlayerAction( 1, "51" )
    game.tic()
        
    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █ ⎡     ⎤ █         ███████████         █         █         █",
"     █ ⎣     ⎦1█         ███████████         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         ███████████         █     ",
"█         █         █         █         ███████████         █     ",
"  ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝▁▁▁▀▜████████▙▄   ▖▝   ▘▗  ",
"     █  ⎛R  ⎞  ███████████         █  ⎛H  ⎞  ███████████         █",
"     █  ⎝  1⎠  ███████████         █  ⎝  3⎠  ███████████         █",
"  ▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▄▟███▙▄▔▔▔▖▝   ▀▜███▛▀▁▁▁▘▗   ▖▝  ",
"███████████ ⎡     ⎤ █ ⎡     ⎤ ███████████         █  ⎛H  ⎞  █     ",
"███████████ ⎣     ⎦3█ ⎣     ⎦2███████████         █  ⎝  2⎠  █     ",
"  ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝   ▘▗▔▔▔▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔          "]

    debug( game.board().shell() )
    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)
