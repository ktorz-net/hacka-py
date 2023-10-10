#!env python3
"""
HackaGame - Game - MoveIt 
"""
from gameEngine import GameMoveIt
from hackapy.command import Command, Option

# Define a command interpreter: 2 options: host address and port:
cmd= Command(
        "start-server",
        [
            Option( "port", "p", default=1400 ),
            Option( "number", "n", 2, "number of games" )
        ],
        (
            "star a server of gameMoveIt on your machine. "
            "gameMoveIt do not take ARGUMENT."
        ))
# Process the command line: 
cmd.process()
if not cmd.ready() :
    print( cmd.help() )
    exit()


game= GameMoveIt()
game.start( cmd.option("number"), cmd.option("port") )
