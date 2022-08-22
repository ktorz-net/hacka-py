#!env python3
"""
First 421 player 
"""
import sys, os, random
import matplotlib.pyplot as plt

# Local HackaGame:
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hackapy as hg

def main():
    print('let\'s go...')
    player= PlayerRandom()
    results= player.takeASeat()
    print( f"Average: { float(sum(results))/len(results) }" )
    plotResults(results)

actions= []
for a1 in ['keep', 'roll']:
    for a2 in ['keep', 'roll']:
        for a3 in ['keep', 'roll']:
            actions.append( a1+'-'+a2+'-'+a3 )

class PlayerRandom( hg.Player ) :
    # PLayer interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConfigurationMsg):
        self.scores= [ 0 for i in range(numberOfPlayers+1) ]
        self.id= playerId
        print( '> ' + '\n'. join([ str(line) for line in gameConfigurationMsg ]) )

    def perceive(self, gameStatusMsg):
        gameStatus= gameStatusMsg[0].split(' ')
        self.horizon= int(gameStatus[1])
        self.dices= [ int(gameStatus[3]), int(gameStatus[4]), int(gameStatus[5]) ]
        print( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        action= random.choice( actions )
        print( f'Action: {action}' )
        return action
    
    def sleep(self, result):
      print( f'--- Results: {str(result)}' )

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
