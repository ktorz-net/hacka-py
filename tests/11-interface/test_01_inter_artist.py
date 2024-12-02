import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

from src.hacka.interface import artist

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_artist_load():
    assert True
