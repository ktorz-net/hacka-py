# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import os, json, random, hackagames.hackapy as hg


def log(txt):
    pass
    #print(txt)

class AutonomousPlayer( hg.AbsPlayer ) :

    def __init__(self, data= '.json'):
        self.qvalues= {}
        self.learningRate= 0.1
        self.epsilon= 0.1
        if os.path.exists(data) :
            dataFile= open(data, 'r')
            self.qvalues= json.load( dataFile )
            dataFile.close()
        self.dataFile= 'data-Q-Values.json'
        self.stats= {'explo': []}

    # Learner :
    def stateStr(self):
        if self.action == 'keep-keep-keep' :
            self.horizon= 0 # If we already keep all dice the game is ended
        state= str(self.horizon)
        for d in self.dices :
            state += '-' + str(d)
        return state

    def updateQValues( self, lastState, lastaction, nextState, reward ):
        oldValue= self.qvalues[lastState][lastaction]
        newValue= reward + 0.999 * self.qvalues[nextState][ self.bestAction( nextState ) ]
        self.qvalues[lastState][lastaction]= (1-self.learningRate)*oldValue + self.learningRate*newValue
    
    def bestAction(self, state):
        action= list(self.qvalues[state].keys())[0]
        value= self.qvalues[state][action]
        for a in self.qvalues[state] :
            if self.qvalues[state][a] > value :
                action= a
                value= self.qvalues[state][a]
        return action

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        log( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        log( gameConf )
        self.actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll' ]
        self.action= 'go'
        self.value= 0
        self.first= True

    def perceive(self, gameState):
        #get elements:
        elements= gameState.children()
        self.horizon= elements[0].flag(1)
        self.dices= elements[1].flags()
        #get reward:
        lastValue= self.value
        self.value= elements[2].value(1)
        self.reward= self.value - lastValue
        #print:
        log( f'H: {self.horizon} DICES: {self.dices} REWARD: {self.reward}' )
        #learn stat reward:
        reachedState= self.stateStr()
        if reachedState not in self.qvalues :
            self.qvalues[reachedState]= {"keep-keep-keep": 0}
        if not self.first : #i.e. it is not the first time we pass here from the last wakeUp.
            self.updateQValues(self.state, self.action, reachedState, self.reward)
        self.first= False
        #switch state:
        self.state= reachedState

    def decide(self):
        #random action:
        self.action= random.choice( self.actions )
        if self.action not in self.qvalues[self.state] :
            self.qvalues[self.state][self.action]= 0.0
        #epsilon chose:
        elif random.random() > self.epsilon :
            self.action= self.bestAction(self.state)
        log( f'Action: {self.action}' )
        return self.action

    def sleep(self, result):
        dataFile= open(self.dataFile, 'w')
        dataFile.write( json.dumps(self.qvalues, sort_keys=True, indent=4) )
        dataFile.close()
        self.stats['explo'].append( len(self.qvalues) )
        log( f'--- Results: {str(result)}' )

def main():
    print('let\'s go...')
    player= AutonomousPlayer()
    results= player.takeASeat()
    print( f"Average: { float(sum(results))/len(results) }" )

# script
if __name__ == '__main__' :
    main()
