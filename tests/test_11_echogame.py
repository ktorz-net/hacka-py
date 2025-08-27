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
    aPod= game.initialize()
    assert type(aPod) == hk.Pod

    aPod= game.playerHand(1)
    assert type(aPod) == hk.Pod

    game.applyAction(aPod, 1)
    game.tic()
    assert type(game.isEnded()) == bool
    assert type(game.playerScore(1)) == float

def test_GameMaster_MyGame():
    game= hkg.EchoGame()
    assert str(game.initialize()) == 'EchoGame: 1 3'

    assert str(game.playerHand(1)) == 'Hello player: 1'

    aPod= hk.Pod("Salut nounou", [2, 3])
    game.applyAction(aPod, 1)
    assert str(game.playerHand(1)) == 'Salut nounou: 2 3'

    game.tic()
    assert game._tic == 1
    assert game.isEnded() == False
    assert game.playerScore(1) == 1.0

    