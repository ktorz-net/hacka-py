#!env python3
"""
HackaGames - Game - Single421 
"""
import os, sys
from . import engine

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import hackapy as hg

# TurnBasedGame:
class TurnBasedGame(hg.Game):

    # Constructor
    def __init__(self, port=1400):
        super().__init__(2, port)

    def newGameEngine(self) :
        pass

    def play(self, chance= 6):
        ttt= self.newGameEngine()
        self.wakeUpPlayers( ttt.name() )
        playerId= 1
        # player take turns :
        while not ttt.isEnded() :
            action= self.activatePlayer( playerId, ttt.status() )
            count= 1
            # give a chance to propose a better action :
            while not ttt.apply( playerId, action ) and count < chance :
                action= self.activatePlayer( playerId, ttt.status() )
                count+= 1
            # switch player :
            if playerId == 1 :
                playerId= 2
            else :
                playerId= 1
        # conclude the game :
        if ttt.isWinning(1) :
            self.sleepPlayer( 1, ttt.status(), 1 )
            self.sleepPlayer( 2, ttt.status(), -1 )
        elif ttt.isWinning(2) :
            self.sleepPlayer( 1, ttt.status(), -1 )
            self.sleepPlayer( 2, ttt.status(), 1 )
        else :
            self.sleepPlayer( 1, ttt.status(), 0 )
            self.sleepPlayer( 2, ttt.status(), 0 )

# Standard Game:
class GameStandard(TurnBasedGame) :
    def newGameEngine(self) :
        return engine.TTT()

# Ultimate Game:
class GameUltimate(TurnBasedGame) :
    def newGameEngine(self) :
        return engine.Ultimate()

# Commands:
class StartCmd( hg.StartCmd ) :
    def __init__(self) :
        super().__init__(
            "TicTacToe",
            ["standard", "ultimate"],
            parameters= { 
                "n": ["number of games", 2]
            }
        )
