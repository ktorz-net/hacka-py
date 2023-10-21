#!env python3
"""
HackaGame - Game - Hello 
"""
import sys, random, re

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
from . import board, mobile

Hexaboard= board.Hexaboard
Cell= board.Cell
Mobile= mobile.Mobile

class GameMoveIt( hg.AbsSequentialGame ) :
    
    # Initialization:
    def __init__( self, seed=False, sizeLine=6, sizeHeight=4,
                 numberOfRobots=1, numberOfHuman=2,
                 numberOfObstacles=6, defective=0.3,
                 numberOfCycle= 10, maximunTics= 16) :
        super().__init__( numberOfPlayers=1 )
        if seed :
            random.seed( seed )
        self._board= Hexaboard( sizeLine, sizeHeight )
        self._mobiles= [ Mobile( i+1, i%sizeLine, i//sizeLine) for i in range(numberOfRobots+numberOfHuman)]
        self._nbObstacles= numberOfObstacles
        self._countDownCycle= numberOfCycle+1
        self._maxTic= maximunTics
        self._countDownTic= 0
        self._actionRePattern = re.compile( "^move "+ ' '.join(["[0123456]" for i in range(numberOfRobots)]) )
        if defective :
            for robot in self._mobiles :
                if random.random() < defective :
                    robot.setError( random.choice([
                        0.1, 0.1, 0.1, 0.1,
                        0.2, 0.2, 0.2,
                        0.3 ]) )

    # Accessor: 
    def mobiles(self): 
        return self._mobiles
    
    def mobile(self, i): 
        return self._mobiles[i-1]

    def board(self): 
        return self._board

    def score(self):
        return self._score

    # Game interface :
    def initialize(self):
        # clean Up.
        self._board.clear()

        # initialize board.
        self._score= 0
        self.setupObstacles()
        self.setupMobile()

        # initialize cycle.
        self.initializeCycle()
        
        # initialize board.
        return self._board.asPod()
    
    def playerHand( self, iPlayer ):
        # ping with the increasing counter
        pod= hg.Pod( 'moveIt', values=[self._maxTic, self._countDownCycle, self._score] )
        self._countDownTic= 0
        for robot in self._mobiles :
            pod.append( robot.asPod() )
        return pod

    def applyPlayerAction( self, iPlayer, action ):
        # Extract robot directions
        if not self._actionRePattern.match( action ) :
             action= "move "+" ".join( ['0' for r in self._mobiles] )
        robotActions= [int(a) for a in action.split(" ")[1:] ]
        if len(robotActions) != len(self._mobiles) :
             robotActions= [0 for r in self._mobiles]
        
        # Extract robot directions
        collisions= self.board().multiMove( [ [r.x(), r.y(), dir] for r, dir in zip( self.mobiles(), robotActions ) ] )
        
        # valide robot goals
        allOk= True
        for robot in self.mobiles() :
            robot.updateGoalSatifaction()
            allOk= allOk and robot.isGoalSatisfied()

        if collisions > 0 :
            # Dommage
            self._score -= self._maxTic * 10 * collisions
            
        if allOk :
            # Bravo
            self._score += self._countDownTic
            self.initializeCycle()
        elif self._countDownTic == 0 :
            # Too late
            self.initializeCycle()
        else :
            # step on the counter
            self._countDownTic-= 1
        
        return True
    
    def tic( self ):
        pass

    def isEnded( self ):
        # if the counter reach it final value
        return self._countDownCycle == 0

    def playerScore( self, iPlayer ):
        # All players are winners.
        return self.score()

    # Board Managment:
    def setupObstacles(self):
        # initialize obstacles' positions:
        for iObst in range(self._nbObstacles) :
            options= self._board.cellsObstacleOk()
            if len(options) == 0 :
                break
            x, y= random.choice( options )
            self._board.at(x, y).setObstacle()

    def setupMobile(self):
        # initialize robot' positions:
        for robot in self._mobiles :
            x, y= random.choice( self._board.cellsEmpty() )
            robot.setPosition(x, y)
            self._board.at(x, y).attachMobile( robot )

    def initializeCycle(self):
        # initialize robot' Goals:
        goalOptions= self._board.cellsType( Cell.TYPE_FREE )
        for robot in self._mobiles :
            gx, gy= random.choice( goalOptions )
            robot.setGoal( gx, gy )
        # initialize cycle counters:
        self._countDownTic= self._maxTic
        self._countDownCycle-= 1