# Local HackaGame:
import sys

sys.path.insert(1, __file__.split('tests')[0])
from src.hacka.games.tictactoe.engine import Classic, Ultimate

# ------------------------------------------------------------------------ #
#                   T E S T   T I C T A C T O E    G A M E
# ------------------------------------------------------------------------ #

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_ttt_initializeClassic():
  engine= Classic()

  assert type(engine) == Classic


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------
def test_ttt_initializeClassic():
  engine= Ultimate()

  assert type(engine) == Ultimate
