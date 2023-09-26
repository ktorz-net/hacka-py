#!env python3
"""
HackaGame player interface 
"""
import sys, os
sys.path.insert(1, __file__.split('hackagames')[0])

import hackagames.hackapy.command as cmd
import hackagames.hackapy.player as pl
from gameEngine import Grid

def main():
    player= PlayerShell()
    player.takeASeat()

class PlayerShell( pl.AbsPlayer ):

    def __init__(self):
        super().__init__()
        self.grid= Grid()
        self.playerId= 0
        
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod):
        self.playerId= playerId
        assert( gamePod.family() == 'Connect4')
        # Reports:
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players) - dimention: {gamePod.flags()}')

    def perceive(self, gameState):
        # update the game state:
        self.grid.fromPod( gameState )
        os.system("clear")
        print( self.grid )

    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')

# script
if __name__ == '__main__' :
    main()