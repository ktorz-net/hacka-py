#!python3
"""
HackaGames - Py421
"""
import sys
sys.path.insert( 1, __file__.split('play')[0] )

from src.hacka.py.player import PlayerIHM as Player
from src.hacka.command import Command, Option

from src.hacka.games.py421 import GameSolo, GameDuo
from src.hacka.games.py421.firstBot import Bot as Opponent

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
    "play",
    [
        Option( "number", "n", 1, "number of games" )
    ],
    "Play to hackagames py421. ARGUMENTS can be: solo or duo" )

# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()

# Start the player the command line: 
if cmd.argument() == "duo" :
  game= GameDuo()
  player1= Player()
  game.launch( [player1, Opponent()], cmd.option("number") )  
else :
  game= GameSolo()
  player1= Player()
  game.launch( [player1], cmd.option("number") )
