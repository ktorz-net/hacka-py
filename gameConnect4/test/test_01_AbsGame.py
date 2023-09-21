"""
Test - Connect4.Engine
"""
import sys

sys.path.insert( 1, __file__.split('hackagames')[0] )
import hackagames.hackapy as hg
import hackagames.gameConnect4.gameEngine as ge

def test_gameMethod():
    game= ge.GameConnect4()

    assert( type( game.initialize().asPod() ) is hg.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hg.Pod )
    assert( game.applyPlayerAction( 1, "test" )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )
