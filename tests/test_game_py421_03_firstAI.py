import sys
sys.path.insert( 1, __file__.split('test')[0] )

from src.hacka.games.py421 import GameSolo as Game
from src.hacka.games.py421.firstBot import Bot

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1    G A M E
# ------------------------------------------------------------------------ #

def verbose(aString):
  print(aString)

def test_py421_firstBot():
  pass

# Test firstAI launch
def test_py421_play():
  game= Game()
  bot= Bot()
  game.local( [bot], 1 )
