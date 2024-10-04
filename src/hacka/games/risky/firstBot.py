#!env python3
"""
HackaGame player interface 
"""
import sys, random

sys.path.insert(1, __file__.split('gameRisky')[0])
import hackapy as hg
import gameRisky.gameEngine as game

def main():
    player= AutonomousPlayer()
    player.takeASeat()

class AutonomousPlayer(hg.AbsPlayer) :
    
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        #print( f'---\nwake-up player-{iPlayer} ({numberOfPlayers} players)')
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky().fromPod( gameConf )
        #self.viewer= game.ViewerTerminal( self.game )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        #self.viewer.print( self.playerId )
    
    def decide(self):
        actions= self.game.searchActions( self.playerId )
        #print( f"Actions: { ', '.join( [ str(a) for a in actions ] ) }" )
        action= random.choice( actions )
        if action[0] == 'move':
            action[3]= random.randint(1, action[3])
        action= ' '.join( [ str(x) for x in action ] )
        #print( "Do: "+ action )
        return action
    
    #def sleep(self, result):
        #print( f'---\ngame end\nresult: {result}')

# script
if __name__ == '__main__' :
    main()
