#!env python3
"""
HackaGame risky interface 
"""

import sys, os

sys.path.insert( 1, __file__.split('gameRisky')[0] )
import hackapy as hg

gamePath= __file__.split('gameRisky')[0] + "/gameRisky"

class ViewerTerminal:

    # Player interface :
    def __init__( self, aGame ):
        self.game= aGame
        self.generateGrid()
        mapFile= f"{gamePath}/resources/map-{self.game.map}.txt"
        if os.path.exists( mapFile ) :
            self.loadGridBackground( mapFile )

    # grid: 
    def generateGrid(self):
        maxLine= 4
        maxLenght= 1
        for cell in self.game.board.cells() :
            x, y = cell.coordinates()
            x= int(x)
            y= int(y)
            if x > maxLine :
                maxLine= x
            if y > maxLenght :
                maxLenght= y
        
        self.grid= [ [' ' for i in range(maxLenght+4) ] for line in range(maxLine+2) ]

    def loadGridBackground( self, mapFile ):
        f= open(mapFile)
        iLine= 0
        for line in f.readlines() :
            for iCol in range( len(line)-1 ) :
                self.grid[iLine][iCol]= line[iCol]
            iLine+= 1
    
    # Print: 
    def print(self, playerId, printFct= print):
        printFct( f'---\ngame state: player-{playerId} (turn { self.game.counter } over { self.game.duration })' )
        grid= [ [ x for x in line ] for line in self.grid ]
        for cell in self.game.board.cells() :
            cellId= str(cell.number())
            iLine, iCol = cell.coordinates()
            iLine= int(iLine)
            iCol= int(iCol)
            if len( cell.pieces() ) > 0 :
                self.printArmyOnGrid( cell.piece(1), grid, iLine, iCol )
            
            l= len(cellId)
            for i in range(l) :
                grid[iLine+1][iCol+3-l+i]=  cellId[i]

        for line in grid :
            printFct( '| '+ ''.join( line ) + ' |' )

    def printArmyOnGrid(self, army, grid, line, col):
        grid[line-1][col]= army.status()
        grid[line][col-2]= str(army.flag(1))
        grid[line][col-1]= '-'
        force= str(army.flag(2))
        while len( force ) < 3 :
            force= ' '+force
        grid[line][col]= force[0]
        grid[line][col+1]= force[1]
        grid[line][col+2]= force[2]
                
                