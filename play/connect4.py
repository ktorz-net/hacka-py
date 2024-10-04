#!env python3
"""
HackaGame - Game - Connect4
"""
import sys

import gameEngine as connect
from hackapy.command import Command, Option
from playerInteractive import PlayerShell as Player
from playerFirstAI import AutonomousPlayer as Oponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "start-interactive",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Start interactive gameConnect4. gameConnect4 do not take ARGUMENT." )
# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

game= connect.GameConnect4()
player= Player()
game.local( [player, Oponent()], cmd.option("number") )
