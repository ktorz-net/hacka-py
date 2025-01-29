#!env python3
"""
HackaGame - Game - Risky 
"""
from . import GameRisky
from ...py.command import Command, Option

# Commands:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server fo gameRisky on your machine. "
            "ARGUMENTS refers to game mode: map-4, map-10, ..."
        ))
cmd.process()
mode= "map-4"
if cmd.ready() :
    if cmd.argument() != "" :
        mode= cmd.argument()
else :
    print( cmd.help() )
    exit()

# start:
game= GameRisky( 2, mode )
game.start( cmd.option("number"), cmd.option("port") )
