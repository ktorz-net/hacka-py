#!env python3
"""
HackaGame - Game - Risky
"""
from hacka.games.risky import GameRisky
from hacka.pylib.command import Command, Option
from hacka.games.risky.shell import Bot as Player
from hacka.games.risky.firstBot import Bot as Oponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "start-interactive",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Start interactive gameRisky. ARGUMENTS ..." )
# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

board= "board-4"
if cmd.argument() in ["board-6", "board-10", "board-12"] :
    board= cmd.argument()

game= GameRisky( 2, board )
player= Player()
game.launch( [player, Oponent()], cmd.option("number") )

