#!env python3
"""
HackaGame - Game - Risky
"""
from gameEngine import GameRisky
from hackapy.command import Command, Option
#from gameEngine.players import PlayerShell as Player
#from gameEngine.players import PlayerMetaRandom as Oponent
from playerInteractive import PlayerShell as Player
from playerFirstAI import AutonomousPlayer as Oponent

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

game= GameRisky( 2, "board-4" )
player= Player()
game.local( [player, Oponent], cmd.option("number") )

