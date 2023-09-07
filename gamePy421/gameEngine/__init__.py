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

    # Constructor: 
    def __init__(self):
        super().__init__(2)
        self._startHorizon= 3
        self._refDices= [0, 0 ,0]
        self._lastPlayer= 0

    # Accessors: 
    def refDices(self) :
        return self._refDices

    def initialize(self):
        # Initialize a new game (not returning anything)
        self.engine= ge.Engine421()
        self.engine.initialize(self._startHorizon)
        self._refDices= [0, 0 ,0]
        self._lastPlayer= 0
        return hg.Pod( 'Game', '421-Duo' )

    def playerHand( self, iPlayer ):
        if (self._lastPlayer == 0 and iPlayer == 1) or (self._lastPlayer != 0 and iPlayer == 2) :
            return self.currentPlayerHand()
        else :
            return self.opponentPlayerHand()

    def currentPlayerHand( self ):
        # Return the game elements in the player vision (an AbsGamel)
        gameElements= hg.Pod( 'Game', '421-Duo' )
        gameElements.append( hg.Pod( 'Horizon', flags=[ self.engine.turn() ] ) )
        gameElements.append( hg.Pod( 'Dices', flags= self.engine.dices() ) )
        gameElements.append( hg.Pod( 'Opponent', flags= self.refDices() ) )
        return gameElements
    
    def opponentPlayerHand( self ):
        # Return the game elements in the player vision (an AbsGamel)
        gameElements= hg.Pod( 'Game', '421-Duo' )
        gameElements.append( hg.Pod( 'Horizon', flags=[ 0 ] ) )
        gameElements.append( hg.Pod( 'Dices', flags= self.refDices() ) )
        gameElements.append( hg.Pod( 'Opponent', flags= self.engine.dices() ) )
        return gameElements
    
    def applyPlayerAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer. return a boolean at True if the player terminate its actions for the current turn.
        self.engine.step( action )
        if iPlayer == 1 and self.engine.isEnded() :
            self._refDices= [ d for d in self.engine.dices() ]
            self.engine.initialize( self._startHorizon-self.engine.turn() )
            self._lastPlayer= 1
            return True
        elif self.engine.isEnded() :
            self._lastPlayer= 2
            return True
        return False

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        return self._lastPlayer == 2 and self.engine.isEnded()

    def playerScore( self, iPlayer ):
        # Get appropriate combinaison:
        if iPlayer == 1: 
            ipCombi= self.refDices()
            opCombi= self.engine.dices()
        else :
            ipCombi= self.engine.dices()
            opCombi= self.refDices()
        
        # Compute scores:
        ipScore= self.engine.score( { "D1": ipCombi[0], "D2": ipCombi[1], "D3": ipCombi[2] } )
        opScore= self.engine.score( { "D1": opCombi[0], "D2": opCombi[1], "D3": opCombi[2] } )

        # Compare:
        if ipScore > opScore :
            return 1
        elif ipScore < opScore :
            return -1
        else :
            return 0
