#!env python3
"""
HackaGame player interface 
"""
import sys, random

sys.path.insert(1, __file__.split('gameTictactoe')[0])
import hackapy as hg
#import gameTictactoe.gameEngine as game

def main():
    player= AutonomousPlayer()
    player.takeASeat()

class Grid() :
    def __init__(self):
        self._= {}

    def initialize(self, letters, numbers):
        self._= {
            line: [0]+ [0 for i in numbers ]
            for line in letters
        }
    
    def update( self, pods ):
        for elt in pods :
            self._[elt.status()]= [0] + elt.flags()
        return self
    
    def at(self, abs, ord):
        return self._[abs][ord]

    def at_set(self, abs, ord, value):
        self._[abs][ord]= value
        return self._[abs][ord]

    def __str__(self, playerId= 0):
        abss= self._.keys()
        ords= range(1, len(abss)+1)
        sign= [ ' ', 'x', 'o' ]
        # print player sign:
        s= f"{ sign[playerId] }:"

        # print letters references:
        for abs in abss :
            if abs in ['D', 'G']:
                s+= '  '
            s+= ' '+ abs
        s+= "\n"

        # print each lines:
        for ord in ords :
            if ord in [4, 7] :
                s+= "  -------|-------|-------\n"
            s+= str(ord) +' '
            for abs in abss :
                if abs in ['D', 'G']:
                    s+= ' |'
                s+= ' '+ sign[ self.at(abs, ord) ]
            s+= "\n"
        return s


class AutonomousPlayer(hg.AbsPlayer) :

    def __init__(self):
        super().__init__()
        self.grid= Grid()
        self.playerId= 0
        self.targets= [0] # The target area where the player can play. A list of number from 1 to 9
    
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod ):
        print( f"<<{type(gamePod)}\n{gamePod}\n>>" )
        #game, mode= tuple( gamePod.status().split("-"))
        assert( gamePod.family() == 'TicTacToe')
        assert( gamePod.status() in ['Classic', 'Ultimate'] )
        self.playerId= playerId
        # ranges
        letters= ["A", "B", "C"]
        numbers= range(1, 4)
        self.targets= [1]
        if gamePod.status() == 'Ultimate' :
            letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
            numbers= range(1, 10)
        # Initialize the grid
        self.grid= Grid()
        self.grid.initialize(letters, numbers)

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
    main()
