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
        # Initialize a new game
        # Return the game configuration (as a Pod)
        # The returned Pod is given to player's wake-up method
        pass
    
    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (as a Pod)
        pass

    def applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        pass

    def tic( self ):
        # called function at turn end, after all player played its actions. 
        pass

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        pass

    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        pass

def test_GameMaster_GameInterface():
    game= MyGame()

def test_GameMaster_init():
    game= MyGame()
    popetmaster= hk.SequentialGameMaster(game)
