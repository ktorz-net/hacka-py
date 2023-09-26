#!env python3
"""
HackaGame - Game - Risky 
"""
import sys, os
from gameEngine import GameRisky

# Local HackaGame:
sys.path.insert(1, __file__.split('gameRisky')[0])
from hackapy.command import Command, Option

# Commands:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server fo gameRisky on your machine. "
            "ARGUMENTS refers to game mode: board-4, board-10, ..."
        ))
cmd.process()
mode= "board-4"
if cmd.ready() :
    if cmd.argument() != "" :
        mode= cmd.argument()
else :
    print( cmd.help() )
    exit()

# start:
game= GameRisky( 2, mode )
game.start( cmd.option("number"), cmd.option("port") )
