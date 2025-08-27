# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

import src.hacka as hk

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S -  
# ------------------------------------------------------------------------ #

class MyGame :
    # Game interface :
    def initialize(self):
        self._hand= [ 1 for i in range(9) ]
        self._tic= 0
        return hk.Pod("Hello", [1, 2, 3], [4.5])
    
    def playerHand( self, iPlayer ):
        return hk.Pod("Hand", [self._hand[iPlayer]])

    def applyAction( self, action, iPlayer ):
        assert type(action) == hk.Pod
        self._hand[iPlayer]+= 1
        return True

    def tic( self ):
        self._tic+= 1

    def isEnded( self ):
        return self._tic > 10

    def playerScore( self, iPlayer ):
        return 1.2


def test_GameMaster_GameInterface():
    game= MyGame()
    aPod= game.initialize()
    assert type(aPod) == hk.Pod

    aPod= game.playerHand(1)
    assert type(aPod) == hk.Pod

    assert type(game.applyAction(aPod, 1)) == bool
    game.tic()
    assert type(game.isEnded()) == bool
    assert type(game.playerScore(1)) == float

def test_GameMaster_MyGame():
    game= MyGame()
    aPod= game.initialize()
    assert str(aPod) == 'Hello: 1 2 3 4.5'

    assert str(game.playerHand(1)) == 'Hand: 1'
    game.applyAction(aPod, 1)
    assert str(game.playerHand(1)) == 'Hand: 2'

    game.tic()
    assert game._tic == 1
    assert game.isEnded() == False
    assert game.playerScore(1) == 1.2

def test_GameMaster_Sequential():
    popetmaster= hk.SequentialGameMaster( MyGame() )
    assert popetmaster.numberOfPlayers() == 1
    