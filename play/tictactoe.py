#!env python3
"""
HackaGame - Game - TicTacToe 
"""

import hacka.games.tictactoe as gttt
from hacka.command import Command, Option
from hacka.games.tictactoe.shell import Interface as Player
from hacka.games.tictactoe.firstBot import Bot as Oponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "start-interactive",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Start interactive gamePy421. ARGUMENTS can be: solo or duo" )
# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

mode= "classic"
if cmd.argument() == "ultimate" :
    mode= "ultimate"

game= gttt.GameTTT( mode )
player= Player()
game.launch( [player, Oponent()], cmd.option("number") )
