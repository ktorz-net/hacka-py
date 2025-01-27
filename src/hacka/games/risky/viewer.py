import sys, os, pathlib

"""
HackaGame risky interface 
"""

from ... import pylib as hk

gamePath= str( pathlib.Path( __file__ ).parent )

class ViewerTerminal:

    # Player interface :
    def __init__( self, aGame ):
        self.game= aGame
        self.generateGrid()
        mapFile= f"{gamePath}/resources/map-{self.game.mapName}.txt"
        if os.path.exists( mapFile ) :
            self.loadGridBackground( mapFile )

    # grid: 
    def generateGrid(self):
        maxLine= 4
        maxLenght= 1
        for tile in self.game.map.tiles() :
            x, y = tile.center().tuple()
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
        for tile in self.game.map.tiles() :
            tileId= str(tile.number())
            iLine, iCol = tile.center().tuple()
            iLine= int(iLine)
            iCol= int(iCol)
            if len( tile.pieces() ) > 0 :
                self.printArmyOnGrid( tile.piece(1), grid, iLine, iCol )
            
            l= len(tileId)
            for i in range(l) :
                grid[iLine+1][iCol+3-l+i]=  tileId[i]

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
                
                