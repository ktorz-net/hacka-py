#!env python3
"""
HackaGame - Game - Hello 
"""
import sys, random

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
from . import board, robot

Hexaboard= board.Hexaboard
Cell= board.Cell
Robot= robot.Robot

class GameMoveIt( hg.AbsSequentialGame ) :
    
    # Initialization:
    def __init__( self, seed=False, sizeLine=6, sizeHeight=4, numberOfRobots=3, numberOfObstacles=6 ) :
        super().__init__( numberOfPlayers=1 )
        if seed :
            random.seed( seed )
        self._board= Hexaboard( sizeLine, sizeHeight )
        self._robots= [ Robot( i, i%sizeLine, i//sizeLine) for i in range(1, numberOfRobots+1 )]
        self._nbObstacles= numberOfObstacles

    # Accessor: 
    def robots(self): 
        return self._robots

    def board(self): 
        return self._board

    # Game interface :
    def initialize(self):
        # clean Up.
        self._board.clear()

        # initialize the score.
        self._score= 0
        # initialize obstacles' positions:

        # initialize robot' positions:
        goalOptions= self._board.cellsType( Cell.TYPE_FREE )
        for robot in self._robots :
            x, y= random.choice( self._board.cellsEmpty() )
            robot.setPosition(x, y)
            gx, gy= random.choice( self._board.cellsEmpty() )
            robot.setGoal( gx, gy )
            self._board.at(x, y).attachRobot( robot )
        return hg.Pod( 'hello' )
        
    def playerHand( self, iPlayer ):
        # ping with the increasing counter
        return hg.Pod( 'hi' )  

    def applyPlayerAction( self, iPlayer, action ):
        # print the receive action message. And that all.
        print( f"Player-{iPlayer} say < {action} >" )
        return True
    
    def tic( self ):
        # step on the counter.
        pass

    def isEnded( self ):
        # if the counter reach it final value
        return False

    def playerScore( self, iPlayer ):
        # All players are winners.
        return 1
