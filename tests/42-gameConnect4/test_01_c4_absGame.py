import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

from src.hacka import core as hk
import src.hacka.games.connect4 as ge

def test_gameMethod():
    game= ge.GameConnect4()

    assert( type( game.initialize().asPod() ) is hk.Pod  )
    assert( type( game.playerHand(1).asPod() ) is hk.Pod )
    assert( game.applyPlayerAction( 1, "test" )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 0 )
