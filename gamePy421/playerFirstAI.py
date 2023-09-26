#!env python3
"""
First 421 player 
"""
import random
# import matplotlib.pyplot as plt

import sys
sys.path.insert( 1, __file__.split('gamePy421')[0] )

# Local HackaGame:
import hackapy as hg

def main():
    print('let\'s go...')
    player= AutonomousPlayer()
    results= player.takeASeat()
    print( f"Average: { float(sum(results))/len(results) }" )
    #plotResults(results)

def log( aString ):
    #print( aString )
    pass

class AutonomousPlayer( hg.AbsPlayer ) :

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        log( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        log( gameConf )
        self.actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll' ]

    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].flag(1)
        self.dices= elements[1].flags()
        log( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        action= random.choice( self.actions )
        log( f'Action: {action}' )
        return action
    
    def sleep(self, result):
        log( f'--- Results: {str(result)}' )

# script :
if __name__ == '__main__' :
    player= AutonomousPlayer()
    results= player.takeASeat()
    print( f"\n## Statistics:\n\tAverage: { float(sum(results))/len(results) }" )
