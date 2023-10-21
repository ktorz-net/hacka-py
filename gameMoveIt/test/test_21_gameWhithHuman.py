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
    
    debug( game.board().shell() )
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

    for l1, l2 in zip( game.board().shell().split("\n"), test ) :
        assert( l1 == l2)
