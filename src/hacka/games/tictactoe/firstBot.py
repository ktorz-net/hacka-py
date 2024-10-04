#!env python3
"""
HackaGame player interface 
"""
from ... import pylib as hk
from .grid import Grid

import random

class Bot(hk.AbsPlayer) :
    def __init__(self):
        self.grid= Grid()
        self.playerId= 0
        self.targets= [0]
    
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod ):
        assert( gamePod.family() == 'TicTacToe')
        assert( gamePod.status() in ['Classic', 'Ultimate'] )
        self.playerId= playerId
        # Initialize the grid
        self.grid= Grid( gamePod.status() )
        self.targets= [1]

    def perceive(self, gameState):
        # Update the grid:
        self.grid.update( gameState.children()[:-1] )
        self.targets= gameState.children()[-1].flags()

    def decide(self):
        # Get all actions
        actions= self.listActions()
        # Select one 
        return random.choice( actions )
    
    #def sleep(self, result):
        #print( f'---\ngame end\nresult: {result}')
    
    # TTT player :
    def listActions(self) :
        actions= []
        tAbss= [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        tOrds= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for iGrids in self.targets :
            for abs in tAbss[ (iGrids-1)%3 ] :
                for ord in tOrds[ (iGrids-1)//3 ] :
                    if self.grid.at(abs, ord) == 0 :
                        actions.append( f"{abs}-{ord}" )
        return actions
    
    def __str__(self):
        targetStr=[ "", "A:C-1:3", "D:F-1:3", "G:I-1:3",
            "A:C-4:6", "D:F-4:6", "G:I-4:6",
            "A:C-7:9", "D:F-7:9", "G:I-7:9"]
        
        # print the grid:
        s= self.grid.__str__(self.playerId)

        # print autorized actions:
        s+= "actions: "+ targetStr[ self.targets[0] ]
        for iGrid in self.targets[1:] :
            s+= ", "+ targetStr[iGrid]
        return s

# script
if __name__ == '__main__' :
    player= Bot()
    player.takeASeat()
