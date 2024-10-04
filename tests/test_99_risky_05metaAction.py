# Local HackaGame:
import sys


sys.path.insert(1, __file__.split('gameRisky')[0])
from gameRisky.gameEngine import GameRisky
import gameRisky.gameEngine.players as pl

# Army Attributes
ACTION= 1
FORCE=  2

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_expenableVsContestable():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    assert game.isExpendable(1)
    assert game.isExpendable(2)
    assert not game.isExpendable(3)
    assert not game.isExpendable(4)
    assert game.contestableFrom(1) == [2]
    assert game.contestableFrom(2) == [1]
    assert game.contestableFrom(3) == []
    assert game.contestableFrom(4) == []
    game.popArmy( 1, 3, 1, 8 )
    print(game.board)
    assert game.isExpendable(1)
    assert game.isExpendable(2)
    assert not game.isExpendable(3)
    assert not game.isExpendable(4)
    assert game.contestableFrom(1) == [2]
    assert game.contestableFrom(2) == [1, 3]
    assert game.contestableFrom(3) == [2]
    assert game.contestableFrom(4) == []


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_defend():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    assert game.cellArmyAction(1) == 1
    assert game.cellArmyForce(1) == 12
    assert game.playerNum
    game.applyPlayerAction(1, "defend")
    assert game.cellArmyAction(1) == 1
    assert game.cellArmyForce(1) == 16
    game.popArmy( 1, 3, 1, 8)
    game.applyPlayerAction(1, "defend")
    assert game.cellArmyAction(1) == 1
    assert game.cellArmyForce(1) == 23
    assert game.cellArmyAction(3) == 1
    assert game.cellArmyForce(3) == 12
    game.initialize()
    game.popArmy( 1, 3, 0, 8 )
    game.applyPlayerAction(1, "defend")
    assert game.cellArmyAction(1) == 1
    assert game.cellArmyForce(1) == 17
    assert game.cellArmyAction(3) == 1
    assert game.cellArmyForce(3) == 8


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_expend():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    assert game.cellIsFree(3)
    assert game.cellIsFree(4)
    game.applyPlayerAction(1, "expend 1")
    assert game.cellArmyOwner(3) == "A"
    assert game.cellArmyAction(3) == 0
    assert game.cellArmyForce(3) == 6
    assert game.cellArmyOwner(4) == "A"
    assert game.cellArmyAction(4) == 0
    assert game.cellArmyForce(4) == 5
    assert game.cellArmyOwner(1) == "A"
    assert game.cellArmyAction(1) == 1
    assert game.cellArmyForce(1) == 1


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_fight():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    assert str(game.cellArmy(1)) == "Army: A [1, 12]"
    assert str(game.cellArmy(2)) == "Army: B [1, 12]"
    assert str(game.cellArmy(3)) == "False"
    assert str(game.cellArmy(4)) == "False"
    game.setRandomSeed(42)
    game.applyPlayerAction(1, "fight 2")
    assert str(game.cellArmy(1)) == "Army: A [1, 1]"
    assert str(game.cellArmy(2)) == "Army: B [1, 3]"
    assert str(game.cellArmy(3)) == "False"
    assert str(game.cellArmy(4)) == "False"
    game.initialize()
    game.popArmy( 1, 3, 1, 8 )
    assert str(game.cellArmy(1)) == "Army: A [1, 12]"
    assert str(game.cellArmy(2)) == "Army: B [1, 12]"
    assert str(game.cellArmy(3)) == "Army: A [1, 8]"
    assert str(game.cellArmy(4)) == "False"
    game.applyPlayerAction(1, "fight 2")
    assert str(game.cellArmy(1)) == "Army: A [1, 1]"
    assert str(game.cellArmy(2)) == "Army: B [1, 2]"
    assert str(game.cellArmy(3)) == "Army: A [1, 8]"
    assert str(game.cellArmy(4)) == "False"
    game.initialize()
    game.popArmy( 1, 3, 1, 13 )
    game.applyPlayerAction(1, "fight 2")
    assert str(game.cellArmy(1)) == "Army: A [1, 12]"
    assert str(game.cellArmy(2)) == "Army: A [0, 5]"
    assert str(game.cellArmy(3)) == "Army: A [1, 1]"
    assert str(game.cellArmy(4)) == "False"
    game.initialize()
    game.popArmy( 1, 3, 0, 13 )
    game.applyPlayerAction(1, "fight 2")
    assert str(game.cellArmy(1)) == "Army: A [1, 1]"
    assert str(game.cellArmy(2)) == "Army: B [1, 5]"
    assert str(game.cellArmy(3)) == "Army: A [0, 13]"
    assert str(game.cellArmy(4)) == "False"


#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_searchMetaActions():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    actions= game.searchActions("A")
    assert actions == [
        ['sleep'], ['grow', 1], ['move', 1, 2, 12],
        ['move', 1, 3, 12], ['move', 1, 4, 12]
    ]
    actions= game.searchMetaActions("A")
    assert actions == [
        ['defend'], ['expend', 1], ['fight', 2]
    ]
    game.popArmy( 1, 3, 1, 8 )
    actions= game.searchMetaActions("A")
    assert actions == [
        ['defend'], ['expend', 1], ['fight', 2]
    ]
    game.popArmy( 2, 4, 1, 8 )
    actions= game.searchMetaActions("A")
    assert actions == [
        ['defend'], ['fight', 2], ['fight', 4]
    ]

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------
def test_risky_play():
  game= GameRisky( 2, "board-4" )
  player1= pl.PlayerBasicRandom()
  player2= pl.PlayerMetaRandom()
  game.local( [player1, player2], 100 )

def test_risky_debug1():
    game= GameRisky( 2, "board-4" )
    game.initialize()
    assert str(game.cellArmy(1)) == "Army: A [1, 12]"
    assert str(game.cellArmy(2)) == "Army: B [1, 12]"
    assert str(game.cellArmy(3)) == "False"
    assert str(game.cellArmy(4)) == "False"

    game.board.cell(1).clear()
    game.board.cell(2).clear()
    
    game.popArmy( 1, 1, 1, 8 )
    game.popArmy( 2, 3, 1, 1 )

    print( f"<<\n{game.playerHand(2)}\n>>" )
    assert f"\n{game.playerHand(2)}\n" == """
Risky: board-4 [1, 4]
- Board:
  - Cell: [1, 2, 3, 4] [5.0, 3.0]
    - Army: A [1, 8]
  - Cell: [2, 1, 3, 4] [5.0, 15.0]
  - Cell: [3, 1, 2] [1.0, 9.0]
    - Army: B [1, 1]
  - Cell: [4, 1, 2] [9.0, 9.0]
"""

    actions= game.searchMetaActions("B")
    print(actions)
    assert actions == [['defend']]
