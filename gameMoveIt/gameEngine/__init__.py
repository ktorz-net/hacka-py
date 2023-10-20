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
    def __init__( self, seed=False, sizeLine=6, sizeHeight=4, numberOfRobots=3, numberOfObstacles=6, defective=0.3 ) :
        super().__init__( numberOfPlayers=1 )
        if seed :
            random.seed( seed )
        self._board= Hexaboard( sizeLine, sizeHeight )
        self._robots= [ Robot( i+1, i%sizeLine, i//sizeLine) for i in range(numberOfRobots)]
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

        # initialize board.
        self._score= 0
        self.setupObstacles()
        self.setupRobot()
        self.setupGoals()
        
        # initialize board.
        return self._board.asPod()
        
    def playerHand( self, iPlayer ):
        # ping with the increasing counter
        pod= hg.Pod( 'moveIt', values=[self._score] )
        for robot in self._robots :
            pod.append( robot.asPod() )
        return pod

    def applyPlayerAction( self, iPlayer, action ):
        # Extract robot directions
        robotActions= [int(a) for a in action.split(" ")[1:] ]

        # Extract robot directions
        self.board().multiMove( [ [r.x(), r.y(), dir] for r, dir in zip( self.robots(), robotActions ) ] )
        
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

    # Board Managment:
    def setupObstacles(self):
        # initialize obstacles' positions:
        for iObst in range(self._nbObstacles) :
            options= self._board.cellsObstacleOk()
            if len(options) == 0 :
                break
            x, y= random.choice( options )
            self._board.at(x, y).setObstacle()

    def setupRobot(self):
        # initialize robot' positions:
        for robot in self._robots :
            x, y= random.choice( self._board.cellsEmpty() )
            robot.setPosition(x, y)
            self._board.at(x, y).attachRobot( robot )

    def setupGoals(self):
        # initialize robot' positions:
        goalOptions= self._board.cellsType( Cell.TYPE_FREE )
        for robot in self._robots :
            gx, gy= random.choice( goalOptions )
            robot.setGoal( gx, gy )