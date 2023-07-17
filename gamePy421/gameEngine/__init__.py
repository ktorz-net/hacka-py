#!env python3
"""
HackaGame - Game - Single421 
"""
import sys
from . import engine as ge

sys.path.insert( 1, 'gamePy421'.join( __file__.split('gamePy421')[:1]) )
import hackapy as hg

# Modes:
#Game2Players= mode2players.Game

class GameSolo( hg.AbsSequentialGame ) :

    def __init__(self):
        super().__init__(1)
    
    # Game interface :
    def initialize(self):
        # Initialize a new game (not returning anything)
        self.engine= ge.Engine421()
        self.engine.initialize()
        self.score= 0
        return hg.Pod( 'Game', '421-Solo' )
    
    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (an AbsGamel)
        gameElements= hg.Pod( 'Game', '421-Solo' )
        gameElements.append( hg.Pod( 'Horizon', flags=[ self.engine.turn() ] ) )
        gameElements.append( hg.Pod( 'Dices', flags=self.engine.dices() ) )
        gameElements.append( hg.Pod( 'Scores', values= [ self.engine.score( self.engine.state ), 0.0 ] ) )
        return gameElements

    def applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        self.score= self.engine.step( action )
        return True

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        return self.engine.isEnded()

    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        return self.score


class GameDuo(hg.AbsSequentialGame) :

    def __init__(self):
        super().__init__(2)
        self.horizon= 3

    def initialize(self):
        # Initialize a new game (not returning anything)
        self.engine= ge.Engine421()
        self.engine.initialize(self.horizon)
        self.score= 0
        self.scoreRef= -1
        self.lastPlayer= 0
        return hg.Pod( 'Game', '421-Duo' )

    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (an AbsGamel)
        gameElements= hg.Pod( 'Game', '421-Duo' )
        gameElements.append( hg.Pod( 'Horizon', flags=[ self.engine.turn() ] ) )
        gameElements.append( hg.Pod( 'Dices', flags=self.engine.dices() ) )
        gameElements.append( hg.Pod( 'Scores', flags=[ self.score, self.scoreRef ] ) )
        return gameElements

    def applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        self.score= self.engine.step( action )
        self.lastPlayer= iPlayer
        if iPlayer == 1 and self.engine.isEnded() :
            self.scoreRef= self.score
            print( f"H: {self.engine.state['H']}" )
            self.engine.initialize( self.horizon-self.engine.state['H'] )
            return True
        return self.engine.isEnded()

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        return self.lastPlayer == 2 and self.engine.isEnded()

    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        if self.scoreRef == self.score :
            return 0
        elif iPlayer == 1 and self.scoreRef > self.score :
            return 1
        elif iPlayer == 2 and self.score > self.scoreRef :
            return 1
        else :
            return -1
