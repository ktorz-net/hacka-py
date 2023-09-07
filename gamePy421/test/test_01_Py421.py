import sys
sys.path.insert( 1, __file__.split('gamePy421')[0] )

from gamePy421.gameEngine.engine import Engine421 as Engine
from gamePy421.gameEngine import GameSolo as Game


# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1    E N G I N E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_Engine_actions():
    subject= Engine()
    assert subject.allActionsStr() == [
        'keep-keep-keep', 'keep-keep-roll',
        'keep-roll-keep', 'keep-roll-roll',
        'roll-keep-keep', 'roll-keep-roll',
        'roll-roll-keep', 'roll-roll-roll'
    ]
    assert subject.isActionStr('keep-keep-keep')
    assert subject.isActionStr('roll-keep-roll')
    assert subject.isActionStr('roll-keep-keep')
    assert subject.isActionStr('roll-roll-roll')
    assert not subject.isActionStr('')
    assert not subject.isActionStr('something')
    assert not subject.isActionStr('xxD431')
    assert not subject.isActionStr('111')
    assert not subject.isActionStr('kEep-keep-keep')
    assert subject.isActionStr('k-k-k')
    assert subject.isActionStr('r-k-r')
    assert subject.isActionStr('r-keep-k')
    assert subject.isActionStr('r-r-roll')

    assert subject.actionFromStr('keep-keep-keep') == { 'A1': "keep",  'A2': "keep",  'A3': "keep" }
    assert subject.actionFromStr('roll-keep-roll') == { 'A1': "roll",  'A2': "keep",  'A3': "roll" }
    assert subject.actionFromStr('roll-keep-keep') == { 'A1': "roll",  'A2': "keep",  'A3': "keep" }
    assert subject.actionFromStr('roll-roll-roll') == { 'A1': "roll",  'A2': "roll",  'A3': "roll" }
    assert subject.actionFromStr('r-k-r')          == { 'A1': "roll",  'A2': "keep",  'A3': "roll" }
    assert subject.actionFromStr('r-keep-k')       == { 'A1': "roll",  'A2': "keep",  'A3': "keep" }
    assert subject.actionFromStr('r-r-roll')       == { 'A1': "roll",  'A2': "roll",  'A3': "roll" }


# ------------------------------------------------------------------------ #
#                   T E S T   4 2 1    G A M E
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_risky_play():
    assert True
