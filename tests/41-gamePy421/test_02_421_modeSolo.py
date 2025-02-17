import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

from src.hacka.py import Pod, Pod256
from src.hacka.games.py421 import GameSolo as Game

# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1 - S O L O   G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_421solo_init():
    game= Game()
    aPod= game.initialize()
    assert str(aPod) == 'Game: 421-Solo'

    dices= game.engine.dices()

    assert dices[0] in [1, 2, 3, 4, 5, 6]
    assert dices[1] in [1, 2, 3, 4, 5, 6]
    assert dices[2] in [1, 2, 3, 4, 5, 6]

    diceCount= [ 0 for i in range(7) ]
    for i in range(100000) :
        game.initialize()
        for dValue in game.engine.dices() :
            diceCount[dValue]+= 1
    
    diceCount= [ round(x/100000.0, 1) for x in diceCount ]
    assert diceCount == [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    game.engine.setOnStateStr( "2-6-3-1" )
    assert game.engine.stateStr() == "2-6-3-1"

    print( game.playerHand(1) )
    
    assert str( game.playerHand(1) ).splitlines() == [
        "Game: 421-Solo",
        "- Horizon: [2]",
        "- Dices: [6, 3, 1] [106]"
    ]
