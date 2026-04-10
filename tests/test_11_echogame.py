# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

import src.hacka as hk
import src.hacka.echogame as hkg

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S -  
# ------------------------------------------------------------------------ #


def test_GameMaster_GameInterface():
    game= hkg.EchoGame()
    aDataTree= game.initialize()
    assert type(aDataTree) == hk.DataTree

    aDataTree= game.playerHand(1)
    assert type(aDataTree) == hk.DataTree

    game.applyAction(1, aDataTree)
    game.tic()
    assert type(game.isEnded()) == bool
    assert type(game.playerScore(1)) == float

def test_GameMaster_MyGame():
    game= hkg.EchoGame()
    assert str(game.initialize()) == 'EchoGame : 1 3 :'

    assert str(game.playerHand(1)) == 'Hello player : 1 :'

    aDataTree= hk.DataTree("Salut nounou", [2, 3])
    game.applyAction(1, aDataTree)
    assert str(game.playerHand(1)) == 'Salut nounou : 2 3 :'

    game.tic()
    assert game._tic == 1
    assert game.isEnded() == False
    assert game.playerScore(1) == 1.0

    