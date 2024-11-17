#!env python3
"""
HackaGame player interface
"""
import os
from ... import core as hk
from . import GameRisky, ViewerTerminal

class Bot(hk.AbsPlayer) :
    # Conscructor :
    def __init__(self, clear= False):
        self.clear= clear

    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{iPlayer} ({numberOfPlayers} players)')
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= GameRisky().fromPod( gameConf )
        print( f'{self.game.map}')
        self.viewer= ViewerTerminal( self.game )

    def perceive(self, gameState):
        if self.clear :
            os.system("clear")
        self.game.fromPod( gameState )
        self.viewer.print(self.playerId)
    
    def decide(self):
        action = input('Enter your action: ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')

def main():
    player= Bot()
    player.takeASeat()

# script
if __name__ == '__main__' :
    main()
