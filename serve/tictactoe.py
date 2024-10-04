#!env python3
"""
HackaGame - Game - TicTacToe 
"""
import hacka.games.tictactoe as gttt
from hacka.pylib.command import Command, Option

# Commands:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server fo gameTicTactoe on the machin. "
            "ARGUMENTS refers to game mode: classic or ultimate."
        )
    )
cmd.process()

if cmd.ready() :
    if cmd.argument() == "ultimate" :
        game= gttt.GameTTT( "ultimate" )
    else :
        game= gttt.GameTTT( "classic" )
else :
    print( cmd.help() )
    exit()

game.start( cmd.option("number"), cmd.option("port") )
