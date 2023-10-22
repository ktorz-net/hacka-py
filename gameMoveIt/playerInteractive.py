#!env python3
"""
HackaGame player interface 
"""
import sys, os
sys.path.insert( 1, __file__.split('gameMoveIt')[0] )

import hackapy.command as cmd
import hackapy.player as pl
import gameMoveIt.gameEngine as ge

def main():
    player= PlayerShell()
    player.takeASeat()

class PlayerShell( pl.AbsPlayer ):

    def __init__(self):
        super().__init__()
        self._board= ge.Hexaboard()
        self._mobiles= []
        self._id= 0
        
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gamePod):
        # Initialize from gamePod:
        self._id= playerId
        assert( gamePod.family() == 'MoveIt')
        self._board.fromPod( gamePod )
        nbRobots, nbMobiles= gamePod.flag(3), gamePod.flag(4)
        self._mobiles= ge.defineMobiles( nbRobots, nbMobiles )
        self._board.dropMobiles( self._mobiles )

        # Initialize state variable:
        self._countTic= 0
        self._countCycle= 0
        self._score= 0

        # Reports:
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        self.report(False)

    def perceive(self, statePod):
        # update the game state:
        self._countTic= statePod.flag(1)
        self._countCycle= statePod.flag(2)
        self._score= statePod.value(1)
        self._board.mobilesFromPod( statePod )
        self.report(False)

    def decide(self):
        action = input('Enter your action (move x OR sleep): ')
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')
    
    # Reports:
    def report(self, clear=True):
        if clear :
            os.system("clear")
        print( f"counters{(self._countTic, self._countCycle)}, score({self._score})" )
        print( self._board.shell() )
        for mobile in self._mobiles :
            print( mobile )

# script
if __name__ == '__main__' :
    main()