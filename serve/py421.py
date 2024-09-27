#!env python3
"""
HackaGame - Game - 421 
"""
from hacka.pylib.command import Command, Option
import hacka.games.py421 as g421

# Commands:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server fo gamePy421 on your machine. "
            "ARGUMENTS refers to game mode: solo or duo."
        ))

cmd.process()
if cmd.ready() :
    if cmd.argument() == "duo" :
        game= g421.GameDuo()
    else :
        game= g421.GameSolo()
else :
    print( cmd.help() )
    exit()

# start:
game.start( cmd.option("number"), cmd.option("port") )
