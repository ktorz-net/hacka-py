#!env python3
"""
HackaGame - Game - Single421 
"""
import os, sys
from . import modeSolo, mode2players

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import hackapy as hg

# Modes:
GameSolo= modeSolo.Game
Game2Players= mode2players.Game

# Commands:
class StartCmd( hg.StartCmd ) :

    def __init__(self) :
        super().__init__(
            "421",
            ["solo", "2-players"],
            parameters= { 
                "n": ["number of games", 2]
            }

#        super().__init__(
#            "421",
#            ["solo", "2-players"],
#            options= { 
#                "v": ["verbose"]
#            },
#            parameters= { 
#                "n": ["number of games", 2],
#                "s": ["random seed", 42]
#            }
        )
