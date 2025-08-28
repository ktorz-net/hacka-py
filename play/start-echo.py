#!python3
"""
HackaGames - Py421
"""

from hacka import SequentialGameMaster, PlayerShell as Player
from src.hacka.echogame import EchoGame

master= SequentialGameMaster( EchoGame() )
player= Player()
master.launchLocal( [player] )
