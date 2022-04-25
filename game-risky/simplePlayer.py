#!env python3
import sys, os, random
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import hackagames as hg

STRENGTH= 0
ACTIVATED= 1

def main():
    hg.takeASeat('localhost', 14001, Player() )

class Player() :
    
    # HackaGames Interface :
    #-----------------------

    def wakeUp(self, numberOfPlayers, playerId, tabletop):
    # wakeUp methods is called at the begining of each game.
        self.turn= 0
        self.id= 0
        self.pieces= []
        self.scores= [0]
        self.numberOfPlayers= numberOfPlayers
        self.id= playerId
        self.tabletop= tabletop
        # Verbose:
        print( "Tabletop:"),
        for i in range( len(self.tabletop) ):
            print( '  ', str(i), ':\t', str(self.tabletop[i]) )
        
    def perceive(self, turn, scores, pieces):
    # perceive methods is called to update the game state, once before the call to decide method.
        self.turn= turn
        self.pieces= pieces
        self.scores= scores
        # Verbose:
        print( f'player-{self.id}" turn: {turn}' )
        print( 'Pieces:', ',\n\t'.join([ str(p) for p in self.pieces ]) )
        print( 'score:', scores)

    def decide(self):
    # asks the player for the action he aims to activate. Action is a coded as a string "action param1 param2 ..."
    # Here we get a random action.
        return self.randomAction()

    def sleep(self, result):
    # sleep methods is called once at the end of each games.
        # Verbose:
        print( "Final: ", result)

    # Risky basic AI:
    #----------------

    # Build a random actions :
    def randomAction(self):
        # Generate candidates:
        actions= [ ['sleep'] ]
        for piece in self.pieces :
            actions+= self.actionsFrom(self.id, piece)
        
        # Chose one:
        action= random.choice( actions )
        
        # Refine:
        if( action[0] == 'move' ): #then get a random strength:
            action[3]= random.randrange( action[3] )

        # Make it compatible (one unique string):
        actstr= ' '.join([str(x) for x in action])
        print( 'action:', actstr )
        return actstr
    
    # Generate possible actions :
    def actionsFrom( self, playerid, aPiece ):
        actions= []
        if aPiece.owner == playerid and aPiece.attributs[ACTIVATED] == 0 :
            actions.append( ['grow', aPiece.position] )
            for edge in self.tabletop[ aPiece.position ] :
                actions.append( ['move', aPiece.position, edge, aPiece.attributs[STRENGTH] ] )
        return actions

# Activate default interface :
if __name__ == '__main__':
    main()
