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
    assert( game.applyPlayerAction( 1, hg.Pod("test") )  )
    game.tic()
    assert( not game.isEnded() )
    assert( game.playerScore(1) == 1 )

def test_initialize():
    game= ge.GameConnect4()

    wakeUpPod= game.initialize().asPod()

    assert( str(wakeUpPod) == "hello:" )
    
    assert( wakeUpPod.family() == "hello" )
    assert( wakeUpPod.status() == "" )
    assert( wakeUpPod.flags() == [] )
    assert( wakeUpPod.values() == [] )
    assert( len( wakeUpPod.children() ) == 0 )

def test_playerHand():
    game= ge.GameConnect4()

    game.initialize().asPod()
    handPod= game.playerHand(1).asPod()

    assert( str(handPod) == 'hi: [0]' )
    
    assert( handPod.family() == "hi" )
    assert( handPod.status() == "" )
    assert( handPod.flags() == [0] )
    assert( handPod.values() == [] )
    assert( len( handPod.children() ) == 0 )