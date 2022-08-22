#!env python3
"""
HackaGame - Game - 421 
"""
from re import S
import sys, os, random
import gameEngine as g421

# Local HackaGame:
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from hackapy.cmd import StartCmd

cmd= g421.StartCmd()

print( cmd )

if cmd.mode == "solo" :
    game= g421.GameSolo()
elif cmd.mode == "2-players" :
    game= g421.Game2Players()
else :
    print("/!\ Unreconized mode")

game.start( (int)(cmd.parameter("n")) )
