#!env python3
"""
HackaGame player interface 
"""
import sys, os
sys.path.insert(1, __file__.split('gameTicTacToe')[0])

import hackapy.command as cmd
import hackapy.player as pl

def main():
    player= PlayerShell()
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

class PlayerShell(pl.AbsPlayer) :

    def __init__(self):
        super().__init__()
        self.grid= Grid()
        self.playerId= 0
        self.targets= [0] # The target area where the player can play. A list of number from 1 to 9
    
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod):
        game= gamePod.family()
        mode= gamePod.status()
        assert( game == 'TicTacToe')
        assert( mode in ['Classic', 'Ultimate'] )
        # Reports:
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        print( game + ' ' + mode )
        # Attributes:
        self.mode= mode
        self.playerId= playerId
        self.end= 0              ## ???
        # Size
        letters= ["A", "B", "C"]
        numbers= range(1, 4)
        self.targets= [1]
        if mode == 'Ultimate' :
            letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
            numbers= range(1, 10)
        # Initialize the grid
        self.grid= Grid()
        self.grid.initialize(letters, numbers)
    
    def perceive(self, gameState):
        # update the game state:
        self.grid.update( gameState.children()[:-1] )
        self.targets= gameState.children()[-1].flags()
        # Reports:
        os.system("clear")
        print( self )

    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')

    # Output :
    def __str__(self):
        targetStr=[ "", "ABC-123", "DEF-123", "GHI-123",
            "ABC-456", "DEF-456", "GHI-456",
            "ABC-789", "DEF-789", "GHI-789"]
        
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