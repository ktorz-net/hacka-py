#!env python3
"""
HackaGame - Game - Connect4 
"""
import sys

sys.path.insert( 1, __file__.split('hackagames')[0] )
import hackagames.hackapy as hg

class GameConnect4( hg.AbsSequentialGame ) :
    
    # Game interface :
    def initialize(self):
        # Initialize a new game (returning the game setting as a Gamel, a game ellement shared with player wake-up)
        self.counter= 0
        return hg.Pod( 'hello' )
        
    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (an AbsGamel)
        return hg.Pod( 'hi', flags=[ self.counter ] )  

    def applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        print( f"Player-{iPlayer} say < {action} >" )
        return True
    
    def tic( self ):
        # called function at turn end, after all player played its actions. 
        self.counter= min( self.counter+1, 3 )

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        return self.counter == 3

    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        return 1
