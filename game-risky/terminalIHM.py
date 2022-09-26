#!env python3
"""
HackaGame player interface 
"""
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import hackapy.cmd as cmd
import hackapy.player as pl
import gameEngine as game

class RiskyPlayer(pl.AbsPlayer) :
    # Conscructor :
    def __init__(self, clear= False):
        self.clear= clear

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        self.viewer= game.ViewerTerminal( gameConf )

    def perceive(self, gameState):
        if self.clear :
            os.system("clear")
        self.viewer.update( gameState )
        self.viewer.print()
    
    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')
