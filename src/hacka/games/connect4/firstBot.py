"""
HackaGame player interface 
"""
import random
from ... import pylib as hk
from .grid import Grid

# Script
def main() :
    player= Bot()
    results= player.takeASeat()
    print( f"Average: {sum(results)/len(results)}" )

def log( anStr ):
    #print( anStr )
    pass

class Bot( hk.AbsPlayer ):

    def __init__(self):
        super().__init__()
        self.grid= Grid()
        self.playerId= 0
        
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod):
        self.playerId= playerId
        assert( gamePod.family() == 'Connect4')
        
    def perceive(self, gameState):
        # update the game state:
        self.grid.fromPod( gameState )
        
    def decide(self):
        options = self.grid.possibilities()
        action = random.choice( options )
        return action
    
    def sleep(self, result):
        log( f'---\ngame end on result: {result}')

# Script :
if __name__ == '__main__' :
    main()