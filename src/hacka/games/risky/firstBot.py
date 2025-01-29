"""
HackaGame player interface 
"""
import random

from ... import py as hk
from . import GameRisky

def main():
    player= Bot()
    player.takeASeat()

class Bot(hk.AbsPlayer) :
    
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self._playerId= chr( ord("A")+iPlayer-1 )
        self._game= GameRisky().fromPod( gameConf )

    def perceive(self, gameState):
        self._game.fromPod( gameState )
    
    def decide(self):
        actions= self._game.buildActionDescritors( self._playerId )
        action= random.choice( actions )
        if action[0] == 'move':
            action[3]= random.randint(1, action[3])
        action= ' '.join( [ str(x) for x in action ] )
        return action

class MetaBot(hk.AbsPlayer) :
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= GameRisky().fromPod( gameConf )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        
    def decide(self):
        actions= self.game.searchMetaActions( self.playerId )
        action= random.choice( actions )
        #action= ' '.join( [ str(x) for x in action ] )
        return action
  

class ReadyBot(hk.AbsPlayer) :
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= GameRisky().fromPod( gameConf )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        
    def decide(self):
        actions= self.game.searchReadyActions( self.playerId )
        action= random.choice( actions )
        return action
  
# script
if __name__ == '__main__' :
    main()
