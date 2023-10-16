
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

    def setRobot(self, aRobot):
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

class Hexaboard:
    DIRECTIONS= [ [(0, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
                    [ (0, 0), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (0, 1)] ]

    # Construction:
    def __init__(self, sizeLine= 8, numberLine= 6):
        self.reset( sizeLine, numberLine )

    def reset(self, sizeLine, numberLine):
        self._sizeLine= sizeLine
        self._nbLine= numberLine
        self._lines= [[ Cell() for i in range(self._sizeLine) ] for j in range(self._nbLine) ]

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

    # Robot Manipulation:
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
        targetX, targetY= self.at_dir( x, y, dir )
        if robot and self.isCoordinate( targetX, targetY ) and self.at( targetX, targetY ).isAvailable() :
            self.at(targetX, targetY).setRobot( robot )
            robot= self.at( x, y ).removeRobot()
            return targetX, targetY
        return x, y

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
            for i in range(l):
                b[y-1][x-l+i+2]= num[i]
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