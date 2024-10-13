#!env python3
"""
HackaGame player interface
"""
import sys

sys.path.insert(1, __file__.split('gameRisky')[0])
from .players import PlayerShell

Bot= PlayerShell

def main():
    player= Bot()
    player.takeASeat()

# script
if __name__ == '__main__' :
    main()
