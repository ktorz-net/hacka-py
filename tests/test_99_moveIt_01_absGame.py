import sys, pathlib
workdir= str( pathlib.Path( __file__ ).parent.parent )
sys.path.insert( 1, workdir )

"""
Test - MoveIt Games Class
"""

import src.hacka.pylib as hk
import src.hacka.games.moveIt as moveIt

def test_gameMethod():
    game= moveIt.GameMoveIt(38)

    assert( type( game.initialize().asPod() ) is hk.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hk.Pod )
    assert( game.applyPlayerAction( 1, "move 0" )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0.0 )