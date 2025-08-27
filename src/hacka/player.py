#!env python3
"""
HackaGame player interface 
"""
import re

# Local HackaGame:
from . import pod, interprocess

class Player() :
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        pass

    def perceive(self, gameState):
        pass
    
    def decide(self):
        return "sleep"
    
    def sleep(self, result):
        pass

    # Player interface :
    def takeASeat(self, host='localhost', port=1400 ):
        client= interprocess.SeatClient(self)
        return client.takeASeat( host, port )

class PlayerShell(Player) :
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        print( gameConf )

    def perceive(self, gameState):
        print( f'---\ngame state\n' + str(gameState) )
    
    def decide(self):
        ok= 3
        while ok > 0 :
            action = input('Enter your action: ')
            if re.search("^(.*):( [0-9]*)*$", action) :
                elts= action.split(": ")
                return pod.Pod( elts[0], [ int(v) for v in elts[1].split(" ") ] )
            else :
                return pod.Pod( action )
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')


