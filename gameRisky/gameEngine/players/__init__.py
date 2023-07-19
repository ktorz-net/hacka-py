#!env python3
"""
HackaGame players for Risky 
"""
import sys, os, random

sys.path.insert( 1, __file__.split('gameRisky')[0] )

import hackapy as hg
import gameRisky.gameEngine as game

class PlayerShell(hg.AbsPlayer) :
    # Conscructor :
    def __init__(self, clear= False):
        self.clear= clear

    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{iPlayer} ({numberOfPlayers} players)')
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky().fromPod( gameConf )
        self.viewer= game.ViewerTerminal( self.game )

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

class PlayerBasicRandom(hg.AbsPlayer) :
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky().fromPod( gameConf )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        
    def decide(self):
        actions= self.game.searchActions( self.playerId )
        action= random.choice( actions )
        if action[0] == 'move':
            action[3]= random.randint(1, action[3])
        action= ' '.join( [ str(x) for x in action ] )
        return action

class PlayerMetaRandom(hg.AbsPlayer) :
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky().fromPod( gameConf )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        
    def decide(self):
        actions= self.game.searchMetaActions( self.playerId )
        action= random.choice( actions )
        action= ' '.join( [ str(x) for x in action ] )
        return action
