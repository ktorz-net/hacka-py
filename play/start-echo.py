#!python3
"""
HackaGames - Py421
"""
import sys
sys.path.insert( 1, __file__.split('play')[0] )

from src.hacka import SequentialGameMaster, PlayerShell as Player
from src.hacka.command import Command, Option

from src.hacka.echogame import EchoGame
from src.hacka.echogame import EchoGame

master= SequentialGameMaster( EchoGame() )
player= Player()
master.launchLocal( [player] )
