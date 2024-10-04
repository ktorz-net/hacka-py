# Local HackaGame:
import sys


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky

# Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

def test_draft():
    assert 1 == 1
