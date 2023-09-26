#!env python3
"""
HackaGame player interface 
"""
import sys, random
sys.path.insert(1, __file__.split('hackagames')[0])

import hackagames.hackapy.player as pl
from gameEngine import Grid

def main():
    player= PlayerRandom()
    player.takeASeat()

class PlayerRandom( pl.AbsPlayer ):

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
        print( f'---\ngame end on result: {result}')

# script
if __name__ == '__main__' :
    main()