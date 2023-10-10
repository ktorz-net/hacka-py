#!env python3
"""
HackaGame - Game - Hello 
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg


class GameMoveIt( hg.AbsSequentialGame ) :
    
    # Initialization:
    def __init__(self) :
        super().__init__( numberOfPlayers=1 )
        self._myAttribut= "Some initializations"
    
    # Game interface :
    def initialize(self):
        # initialize the counter and only say hello.
        self.counter= 0
        return hg.Pod( 'hello' )
        
    def playerHand( self, iPlayer ):
        # ping with the increasing counter
        return hg.Pod( 'hi', flags=[ self.counter ] )  

    def applyPlayerAction( self, iPlayer, action ):
        # print the receive action message. And that all.
        print( f"Player-{iPlayer} say < {action} >" )
        return True
    
    def tic( self ):
        # step on the counter.
        self.counter= min( self.counter+1, 3 )

    def isEnded( self ):
        # if the counter reach it final value
        return self.counter == 3

    def playerScore( self, iPlayer ):
        # All players are winners.
        return 1
