import sys
sys.path.insert( 1, __file__.split('gamePy421')[0] )

from gamePy421.gameEngine import GameDuo as Game


# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1 - D U O   G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_421duo_init():
    subject= Game()
    aPod= subject.initialize()
    assert str(aPod) == 'Game: 421-Duo'

    assert subject.refDices() == [0, 0 ,0]
    assert subject._lastPlayer == 0

    dices= subject.engine.dices()

    assert dices[0] in [1, 2, 3, 4, 5, 6]
    assert dices[1] in [1, 2, 3, 4, 5, 6]
    assert dices[2] in [1, 2, 3, 4, 5, 6]

    diceCount= [ 0 for i in range(7) ]
    for i in range(100000) :
        subject.initialize()
        for dValue in subject.engine.dices() :
            diceCount[dValue]+= 1
    

    diceCount= [ round(x/100000.0, 1) for x in diceCount ]
    assert diceCount == [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    subject.engine.setOnStateStr( "2-6-3-1" )
    assert subject.engine.stateStr() == "2-6-3-1"

    assert str( subject.playerHand(1) ).splitlines() == [
        "Game: 421-Duo",
        "- Horizon: [2]",
        "- Dices: [6, 3, 1]",
        "- Opponent: [0, 0, 0]"]

    assert str( subject.playerHand(2) ).splitlines() == [
        "Game: 421-Duo",
        "- Horizon: [0]",
        "- Dices: [0, 0, 0]",
        "- Opponent: [6, 3, 1]"]

def test_421duo_play():

    subject= Game()
    aPod= subject.initialize()
    subject.engine.setOnStateStr( "2-6-3-1" )

    assert subject.applyPlayerAction( 1, "roll-keep-keep" ) == False
    assert subject._lastPlayer == 0
    assert subject.applyPlayerAction( 1, "roll-keep-keep" ) 
    assert subject._lastPlayer == 1
    assert subject.applyPlayerAction( 2, "r-r-r" ) == False
    assert subject._lastPlayer == 1
    assert subject.applyPlayerAction( 2, "keep-keep-keep" ) 
    assert subject._lastPlayer == 2

# Test firstAI launch
def test_421duo_score():
    subject= Game()
    subject.initialize()
    subject._refDices= [1, 1 ,1]

    subject.engine.setOnStateStr( "0-4-2-1" )
    assert subject.playerScore( 1 ) == -1
    assert subject.playerScore( 2 ) == 1

    subject.engine.setOnStateStr( "0-6-2-1" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-6-1-1" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-6-5-4" )
    assert subject.playerScore( 1 ) == 1
    assert subject.playerScore( 2 ) == -1

    subject.engine.setOnStateStr( "0-1-1-1" )
    assert subject.playerScore( 1 ) == 0
    assert subject.playerScore( 2 ) == 0
