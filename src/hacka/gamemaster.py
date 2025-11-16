
# Local HackaGame:
import warnings
from tqdm import tqdm
from . import interprocess

class AbsGame():
    # Game interface :
    def initialize(self):
        # Initialize a new game
        # Return the game configuration (as a Pod object)
        # The returned Pod is given to player's wake-up method
        assert( "Should be implemented..." == None )
    
    def playerHand( self, iPlayer ):
        # Return the game elements in the player vision (as a Pod object)
        assert( "Should be implemented..." == None )

    def applyAction( self, iPlayer, action ):
        # Apply the action choosen by the player iPlayer.
        # return a boolean at True if the player terminate its actions for the current turn.
        pass

    def tic( self ):
        # called function at turn end, after all player played its actions. 
        pass

    def isEnded( self ):
        # must return True when the game end, and False the rest of the time.
        assert( "Should be implemented..." == None )

    def playerScore( self, iPlayer ):
        # return the player score for the current game (usefull at game ending)
        assert( "Should be implemented..." == None )

class AbsGameMaster():
    # Constructor
    def __init__(self, game, numberOfPlayers= 1 ):
        self._game= game
        self._numberOfPlayers= numberOfPlayers

    # Game interface :
    def numberOfPlayers(self):
        return self._numberOfPlayers
    
    # Accessor : 
    def game(self):
        return self._game
    
    # Process :
    def launchWithTabletop(self, tabletop, numberOfGames, maxAction= 100, maxTurn= 1000):
        print( f'HackaGame: wait for {self._numberOfPlayers} players' )
        tabletop.waitForPlayers( self._numberOfPlayers )
        print( f'HackaGame: process {numberOfGames} games' )
        for i in tqdm(range(numberOfGames)) :
            self.play(tabletop, maxAction, maxTurn)
            tabletop.changePlayerOrder()
        print( f'HackaGame: stop player-clients' )
        for i in range(1, self._numberOfPlayers+1) :
            tabletop.stopPlayer( i )

    def launchOnNet(self, numberOfGames= 1, port=1400, maxAction= 100, maxTurn= 1000 ):
        tabletop= interprocess.TabletopNet(port)
        self.launchWithTabletop(tabletop, numberOfGames, maxAction, maxTurn)

    def launchLocal(self, players, numberOfGames= 1, maxAction= 100, maxTurn= 1000):
        print( f" local games ({numberOfGames})" )
        assert( len(players) == self._numberOfPlayers )
        tabletop= interprocess.TabletopLocal( players )
        self.launchWithTabletop(tabletop, numberOfGames, maxAction, maxTurn)
        return tabletop.results()
    
    def play( self, aDealer, maxAction= 100, maxTurn= 1000 ):
        # Depend on how the players are handled: cf. AbsSequentialGame and AbsSimultaneousGame
        pass

class SequentialGameMaster(AbsGameMaster):
    def play(self, tabletop, maxAction= 100, maxTurn= 1000):
        gameConf= self._game.initialize()
        tabletop.wakeUpPlayers( gameConf )
        iPlayer= 1
        iTurn= 0
        # player take turns :
        while (not self._game.isEnded()) and iTurn < maxTurn :
            action= tabletop.activatePlayer( iPlayer, self._game.playerHand(iPlayer) )
            # give a chance to propose a better action :
            iAction= 1
            while (not self._game.applyAction( iPlayer, action )) and iAction < maxAction :
                action= tabletop.activatePlayer( iPlayer, self._game.playerHand(iPlayer) )
                iAction= iAction + 1
            assert iAction < maxAction
            iTurn= iTurn + 1
            # switch player :
            iPlayer+= 1
            if iPlayer > self._numberOfPlayers :
                self._game.tic()
                iPlayer= 1
        assert iTurn < maxTurn
        
        # conclude the game :
        iPlayer= 1
        while iPlayer <= self._numberOfPlayers :
            tabletop.sleepPlayer( iPlayer, self._game.playerHand(iPlayer), self._game.playerScore(iPlayer) )
            iPlayer+= 1

class SimultaneousGameMaster(AbsGame):
    pass
