#!env python3
"""
First 421 player 
"""
import sys, os, random
import matplotlib.pyplot as plt

# Local HackaGame:
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hackapy as hg

def log( aString ):
    print( aString )

def main():
    actions= []
    for a1 in ['keep', 'roll']:
        for a2 in ['keep', 'roll']:
            for a3 in ['keep', 'roll']:
                actions.append( a1+'-'+a2+'-'+a3 )
    print('let\'s go...')
    player= PlayerRandom(actions)
    results= player.takeASeat()
    print( f"Average: { float(sum(results))/len(results) }" )
    plotResults(results)

class PlayerRandom( hg.AbsPlayer ) :

    def __init__(self, actions):
        super().__init__()
        self.actions= actions
    
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        log( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        log( gameConf )

    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].attribute(0)
        self.dices= elements[1].attributes()
        if len(elements) == 3 : # ie in duo mode
            self.reference= elements[2].attribute(0)
            log( f'H: {self.horizon} DICES: {self.dices} REF: {self.reference}' )
        else :
            log( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        action= random.choice( self.actions )
        log( f'Action: {action}' )
        return action
    
    def sleep(self, result):
        log( f'--- Results: {str(result)}' )

def plotResults(results, scope= 100):
    # Calibrate the scope:    
    if len(results) <= scope :
        scope= 1
    # Compute averages avery scope results:    
    averageScores= []
    for i in range( scope, len(results)+1 ) :
        averageScores.append( sum(results[ i-scope:i ])/scope )
    # And plot it:
    plt.plot( averageScores )
    plt.ylabel( "scores" )
    plt.show()

# script
if __name__ == '__main__' :
    main()
