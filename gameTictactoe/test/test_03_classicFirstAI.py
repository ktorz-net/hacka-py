from gameEngine import GameTTT as Game
from classicFirstAI import PlayerRandom as Player

# ------------------------------------------------------------------------ #
#                   T E S T   T I C T A C T O E    G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_risky_play():
  game= Game()
  player1= Player()
  player2= Player()
  game.local( [player1, player2], 1 )
