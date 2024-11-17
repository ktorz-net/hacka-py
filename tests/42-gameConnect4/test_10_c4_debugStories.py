import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

from src.hacka.games.py421 import GameSolo as Game

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1    G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_risky_play():
    assert True
