#!env python3
"""
First Bot for 421
"""
import random

from ... import py as hkpy

def log( aString ):
    #print( aString )
    pass

class Bot( hkpy.AbsPlayer ) :

    def __init__(self):
        self.horizon= -1
        self.dices= [0, 0, 0]

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        self.actions= [
            'keep-keep-keep', 'keep-keep-roll',
            'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll',
            'roll-roll-keep', 'roll-roll-roll'
        ]

    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].flag(1)
        self.dices= elements[1].flags()

    def decide(self):
        return random.choice( self.actions )

    def sleep(self, result):
        self.horizon= -1

# script :
if __name__ == '__main__' :
    bot= Bot()
    results= bot.takeASeat()
    print( f"\n## Statistics:\n\tAverage: { float(sum(results))/len(results) }" )
