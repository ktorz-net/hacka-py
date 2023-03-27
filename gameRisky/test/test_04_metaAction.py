# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('gameRisky')[0] )

from gameRisky.gameEngine import GameRisky

# Test move action ...
def test_risky_isExpenable():
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
    game.appendArmy( 1, 3, 8, 1 )
    print(game.board)
    assert game.isExpendable(1)
    assert game.isExpendable(2)
    assert not game.isExpendable(3)
    assert not game.isExpendable(4)
    assert game.contestableFrom(1) == [2]
    assert game.contestableFrom(2) == [1, 3]
    assert game.contestableFrom(3) == [2]
    assert game.contestableFrom(4) == []

def test_risky_contestable():
    game= GameRisky( 2, "board-4" )
    game.initialize()

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
