#!env python3
"""
HackaGame - Game - Hello 
"""
import sys

# Local HackaGame:
sys.path.insert( 1, __file__.split('gameConnect4')[0] )
from gameEngine import GameConnect4
from hackapy.command import Command, Option

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server fo gameConnect4 on your machine. "
            "gameConnect4 do not take ARGUMENT."
        ))
# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

# Start the player the command line: 
game= GameConnect4()

game.start( cmd.option("number"), cmd.option("port") )
