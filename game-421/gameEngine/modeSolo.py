# Local HackaGame:
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hackapy as hg
from . import engine as ge

class Game(hg.Game) :

    def play(self):
        engine= ge.Engine421()
        score= 0.0
        engine.initialize()
        self.wakeUpPlayers('Single421')
        while not engine.isEnd() :
            action= self.activatePlayer( 1, self.hackaState(engine) )
            score= engine.step( action )
        self.sleepPlayer( 1, self.hackaState(engine), score )
    
    def hackaState(self, engine):
        return f'H: {engine.turn()} DICES: '+ ' '.join([ str(d) for d in engine.dices() ])

# test the game:
def main():
    print('Let\'s go')
    game= Game()
    game.start(2)

# go:
if __name__ == '__main__' :
    main()
