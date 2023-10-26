"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def test_gameMethod():
    game= ge.GameMoveIt(38)

    assert( type( game.initialize().asPod() ) is hg.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hg.Pod )
    assert( game.applyPlayerAction( 1, "move 0" )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )