"""
Test - MoveIt Hexagonal-cells' board Class
"""
"""
Test - MoveIt Robot Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg

import random

class Cell:
    TYPE_FREE= 0
    TYPE_OBSTACLE= 1

    # Construction:
    def __init__(self):
        self._type= Cell.TYPE_FREE
        self._robot= False
        self._reservation= 0

    def setFree(self):
        self._type= Cell.TYPE_FREE

    def setObstacle(self):
        self._type= Cell.TYPE_OBSTACLE

    def attachRobot(self, aRobot):
        if self._type == Cell.TYPE_FREE and not self._robot :
            self._robot= aRobot
            return True
        return False

    def removeRobot(self):
        r= self._robot
        self._robot= False
        return r
    
    def reserve(self):
        self._reservation += 1

    def cleanReservation(self):
        self._reservation= 0
    
    # Accessors: 
    def type(self):
        return self._type

    def robot(self):
        return self._robot

    def isObstacle(self):
        return self.type() == Cell.TYPE_OBSTACLE
    
    def isAvailable(self):
        return not ( self.isObstacle() or bool(self._robot) ) and self._reservation < 2

class Hexaboard(hg.PodInterface):
    DIRECTIONS= [ [(0, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
                    [ (0, 0), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (0, 1)] ]

    # Construction:
    def __init__(self, sizeLine= 8, numberLine= 6):
        self.reset( sizeLine, numberLine )

    def reset(self, sizeLine, numberLine):
        self._sizeLine= sizeLine
        self._nbLine= numberLine
        self._lines= [[ Cell() for i in range(self._sizeLine) ] for j in range(self._nbLine) ]

    # Pod interface:
    def asPod(self, family="Board"):
        pod= hg.Pod( family, "", [ self._sizeLine, self._nbLine ] )
        cellType= [ "FREE", "OBSTACLE" ]
        for line in self._lines :
            podLine= hg.Pod( "Line" )
            for cell in line :
                podLine.append( hg.Pod( "Cell", cellType[cell.type()] ) )
            pod.append( podLine )

        return pod
    
    def fromPod(self, aPod):
        self.reset( aPod.flag(1), aPod.flag(2) )
        iLine= 0
        for podLine in aPod.children() :
            iCell= 0
            for podCell in podLine.children() :
                if podCell.status() == "OBSTACLE" :
                    self.at(iCell, iLine).setObstacle()
                iCell+= 1
            iLine+= 1
        return self
    
    # Accessors: 
    def size(self):
        return (self._sizeLine, self._nbLine)

    def at(self, x, y):
        return self._lines[y][x]
    
    def at_dir(self, x, y, i):
        dx, dy= Hexaboard.DIRECTIONS[ y%2 ][i]
        return x+dx, y+dy

    def movesFrom(self, x, y):
        dirs= []
        for i in range(7) :
            targetX, targetY= self.at_dir( x, y, i )
            if self.isCoordinate( targetX, targetY ) and not self.at( targetX, targetY ).isObstacle() :
                dirs.append( i )
        return dirs

    def isCoordinate(self, x, y):
        return 0 <= x and x < self._sizeLine and 0 <= y and y < self._nbLine 

    def cellsType(self, aType ):
        options= []
        for y in range( self._nbLine ) :
            for x in range( self._sizeLine ) :
                if self.at(x, y).type() == aType :
                    options.append( (x, y) )
        return options
    
    def cellsEmpty( self ):
        options= []
        for y in range( self._nbLine ) :
            for x in range( self._sizeLine ) :
                if self.at(x, y).type() == Cell.TYPE_FREE and not self.at(x, y).robot() :
                    options.append( (x, y) )
        return options

    # Clear: free all cells:
    def clear(self):
        for y in range( self._nbLine ) :
            for x in range( self._sizeLine ) :
                self.at(x, y).setFree()
                self.at(x, y).removeRobot()
                
    # Robot Manipulation:
    def setRobot_at(self, robot, x, y):
        if self.at(x, y ).attachRobot( robot ) :
            robot.setPosition(x, y)
            return True
        return False
    
    def teleportRobot(self, x, y, tx, ty):
        robot= self.at( x, y ).robot()
        if robot and (x, y) == (tx, ty) :
            return True
        if robot and self.isCoordinate( tx, ty ) and self.at( tx, ty ).isAvailable() :
            self.at(tx, ty).attachRobot( robot )
            robot= self.at( x, y ).removeRobot()
            robot.setPosition(tx, ty)
            return True
        return False
    
    def cleanReservations(self):
        for line in self._lines :
            for cell in line :
                cell.cleanReservation()

    def reserveAt_dir(self, x, y, dir):
        targetX, targetY= self.at_dir( x, y, dir )
        if self.isCoordinate( targetX, targetY ) :
            self.at(targetX, targetY).reserve()
    
    def moveRobotAt_dir(self, x, y, dir):
        robot= self.at( x, y ).robot()
        if robot : 
            if random.random() < robot.error() :
                dir= random.choice( self.movesFrom(x, y) )
            targetX, targetY= self.at_dir( x, y, dir )
            if self.teleportRobot(x, y, targetX, targetY):
                return [targetX, targetY]
            robot.collide()
        return False

    def multiMove(self, moves):
        for m in moves :
            self.reserveAt_dir( m[0],  m[1], m[2] )
        for m in moves :
            self.moveRobotAt_dir( m[0],  m[1], m[2] )
        self.cleanReservations()
    
    # Print:
    def shell_coord(self, ix, iy):
        if iy%2 == 0 :
            return ix*10+5, iy*3+3
        return ix*10+10, iy*3+3
        
    def shell_freeCell(self, b, ix, iy):
        x, y= self.shell_coord(ix, iy)
        b[y+1][x-3],b[y+1][x-2], b[y+1][x+2], b[y+1][x+3]= "▖","▝","▘","▗"
        b[y][x-5], b[y][x+5]= "█", "█"
        b[y-1][x-5], b[y-1][x+5]= "█", "█"
        b[y-2][x-3],b[y-2][x-2], b[y-2][x+2], b[y-2][x+3]= "▘","▗","▖","▝"
        robot= self.at(ix, iy).robot()
        if robot :
            b[y+1][x-1], b[y+1][x], b[y+1][x+1]= '▁', '▁', '▁'
            b[y][x-2], b[y][x-1], b[y][x+2]=     "⎛", "R", "⎞"
            b[y-1][x-2], b[y-1][x], b[y-1][x+2]= "⎝", " ", "⎠"
            b[y-2][x-1], b[y-2][x], b[y-2][x+1]= '▔', '▔', '▔'
        
            num= str(robot.number())
            l= len(num)
            xg, yg= robot.goal()
            xg, yg= self.shell_coord( xg, yg )
            b[yg][xg-3], b[yg][xg+3]= '⎡', '⎤'
            b[yg-1][xg-3], b[yg-1][xg+3]= '⎣', '⎦'
            for i in range(l):
                b[y+l-i][x]= num[i]
                b[yg+l-i-2][xg+4]= num[i]

        return x, y
    
    def shell_obsCell(self, b, ix, iy):
        y, x= iy*3+3, ix*10+10
        if iy%2 == 0 :
            x = ix*10+5
        b[y+1][x-3],b[y+1][x-2], b[y+1][x+2], b[y+1][x+3]= "▄","▟","▙","▄"
        
        for l, c in [(y-2, x-3), (y-2, x+3) ]:
            if b[l][c] in ["▟","▙"] :
                b[l][c]= "█"
            else :
                b[l][c]= "▀"
        
        if b[y-2][x-2] == "▄" :
            b[y-2][x-2]= "█"
        else :
            b[y-2][x-2]= "▜"
        
        if b[y-2][x+2] == "▄" :
            b[y-2][x+2]= "█"
        else :
            b[y-2][x+2]= "▛"
        
        fill= [ (y-2, c) for c in range( x-1, x+2, 1 ) ]
        fill+= [ (y-1, c) for c in range( x-5, x+6, 1 ) ]
        fill+= [ (y, c) for c in range( x-5, x+6, 1 ) ]
        fill+= [ (y+1, c) for c in range( x-1, x+2, 1 ) ]
        for l, c in fill :
            b[l][c]= "█"
        return x, y

    def shell(self): 
        # Initialize the char buffer
        bufSize= 6 + self._sizeLine*10
        buffer= [ [ " " for c in range( bufSize ) ] for l in range( 3 + self._nbLine*3 ) ]
        
        iPlus= 0
        if self._nbLine %2 == 0 :
            iPlus= 5
        for i in range(5, bufSize-5, 10 ) :
            buffer[0][i]= "▔"
            buffer[-1][i+iPlus]= "▁"
        
        # Draw the grid
        obsCell= []
        for iL in range(self._nbLine) :
            for iC in range(self._sizeLine) :
                if self.at( iC, iL ).type() == Cell.TYPE_OBSTACLE :
                    obsCell.append( [iC, iL] )
                else:
                    self.shell_freeCell( buffer, iC, iL )

        for c in obsCell:
            self.shell_obsCell( buffer, c[0], c[1] )

        # Fill the cells
        # Send it
        return "\n".join( [ "".join( line ) for line in reversed(buffer) ] )