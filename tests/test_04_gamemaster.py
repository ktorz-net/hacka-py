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
        return hk.DataTree("Hello", [1, 2, 3], [4.5])
    
    def playerHand( self, iPlayer ):
        return hk.DataTree("Hand", [self._hand[iPlayer]])

    def applyAction( self, iPlayer, action ):
        assert type(action) == hk.DataTree
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
    aDataTree= game.initialize()
    assert type(aDataTree) == hk.DataTree

    aDataTree= game.playerHand(1)
    assert type(aDataTree) == hk.DataTree

    assert type(game.applyAction(1, aDataTree)) == bool
    game.tic()
    assert type(game.isEnded()) == bool
    assert type(game.playerScore(1)) == float

def test_GameMaster_MyGame():
    game= MyGame()
    aDataTree= game.initialize()
    assert str(aDataTree) == 'Hello : 1 2 3 : 4.5'

    assert str(game.playerHand(1)) == 'Hand : 1 :'
    game.applyAction(1, aDataTree)
    assert str(game.playerHand(1)) == 'Hand : 2 :'

    game.tic()
    assert game._tic == 1
    assert game.isEnded() == False
    assert game.playerScore(1) == 1.2

def test_GameMaster_Sequential():
    popetmaster= hk.SequentialGameMaster( MyGame() )
    assert popetmaster.numberOfPlayers() == 1
    