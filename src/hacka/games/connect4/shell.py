"""
HackaGame player interface 
"""
import os
from ... import pylib as hk
from .grid import Grid

# Script
def main() :
    player= Interface()
    player.takeASeat()

class Interface(hk.AbsPlayer) :

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
        print( "You: " + ["-", "O", "X"][self.playerId] )

    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')
