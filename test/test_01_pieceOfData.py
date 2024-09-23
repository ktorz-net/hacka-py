# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('hackapy')[0] )

import hackapy.pod as pod

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_Pod_init():
    gamel= pod.Pod()
    assert gamel.family() == "Pod"
    assert gamel.flags() == []
    assert gamel.values() == []
    assert gamel.status() == ""
    assert gamel.children() == []
    assert gamel.status() == ""

def test_Pod_init2():
    gamel= pod.Pod( "Bob", "cool", [1, 2, 3], [4.2, 6.9] )
    assert gamel.family() == "Bob"
    assert gamel.status() == "cool"
    assert gamel.flags() == [1, 2, 3]
    assert gamel.values() == [4.2, 6.9]
    assert gamel.children() == []
    for i in range(1,3):
        assert gamel.flag(i) == i
    assert gamel.value(1) == 4.2
    assert gamel.value(2) == 6.9

def test_Pod_dump():
    gamel= pod.Pod()
    assert gamel.dump() == "Pod - 0 0 0 0 :" # set: "pod-00 (0 0 0 0) state: attrs: values: cells:"
    # assert str(gamel) == "pod [] [] :" 
    gamel.setFlags([3, 8])
    assert gamel.dump() == "Pod - 0 2 0 0 : 3 8"
    gamel.append( pod.Pod( 'Bob',  "happy", [4], [0.6, 10.0] ) )
    assert gamel.dump() == "Pod - 0 2 0 1 : 3 8\nBob - 5 1 2 0 : happy 4 0.6 10.0"
    gamel.append( pod.Pod() )
    assert '\n'+ gamel.dump() +'\n' == """
Pod - 0 2 0 2 : 3 8
Bob - 5 1 2 0 : happy 4 0.6 10.0
Pod - 0 0 0 0 :
"""

def test_Pod_load():
    gamel=pod.Pod( 'SouriCity', flags=[3, 8] )
    assert gamel.dump() == "SouriCity - 0 2 0 0 : 3 8"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "SouriCity - 0 2 0 0 : 3 8"

def test_Pod_load2():
    gamel=pod.Pod( 'SouriCity', flags=[3, 8] )
    gamel.append(pod.Pod( 'bob', flags=[4], status='happy' ) )
    gamel.append(pod.Pod( 'lucy', values=[10.0] ) )
    
    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump()  +'\n' == """
SouriCity - 0 2 0 2 : 3 8
bob - 5 1 0 0 : happy 4
lucy - 0 0 1 0 : 10.0
"""

def test_Pod_load3():
    gamel=pod.Pod( 'SouriCity', flags=[3, 8] )
    gamel.append(pod.Pod( 'bob', flags=[4], status='happy' ) )
    gamel.append(pod.Pod( 'lucy', values=[10.0] ) )

    assert gamel.dump().splitlines() == [
        "SouriCity - 0 2 0 2 : 3 8",
        "bob - 5 1 0 0 : happy 4",
        "lucy - 0 0 1 0 : 10.0" ]

    gamel2=pod.Pod().load( gamel.dump().splitlines() )
    assert '\n'+ gamel2.dump()  +'\n' == """
SouriCity - 0 2 0 2 : 3 8
bob - 5 1 0 0 : happy 4
lucy - 0 0 1 0 : 10.0
"""

def test_Pod_deep():
    gamel=pod.Pod( 'SouriCity', flags=[3, 8] )
    bob=pod.Pod( 'bob', flags=[4] )
    bob.append(pod.Pod( 'action', "Attack", [10] ) )
    bob.append(pod.Pod( 'action', "Move", [], [2.0] ) )
    gamel.append( bob )
    gamel.append(pod.Pod( 'lucy', 'happy' ) )
    print( gamel.dump() )
    assert '\n'+ gamel.dump() +'\n' == """
SouriCity - 0 2 0 2 : 3 8
bob - 0 1 0 2 : 4
action - 6 1 0 0 : Attack 10
action - 4 0 1 0 : Move 2.0
lucy - 5 0 0 0 : happy
"""

    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump() +'\n' == """
SouriCity - 0 2 0 2 : 3 8
bob - 0 1 0 2 : 4
action - 6 1 0 0 : Attack 10
action - 4 0 1 0 : Move 2.0
lucy - 5 0 0 0 : happy
"""

def test_Pod_str():
    gamel=pod.Pod( 'SouriCity', flags=[3, 8] )
    bob=pod.Pod( 'bob', flags=[4] )
    bob.append(pod.Pod( 'action', "Attack", [10] ) )
    bob.append(pod.Pod( 'action', "Move", [], [2.0] ) )
    gamel.append( bob )
    gamel.append(pod.Pod( 'lucy', 'happy' ) )
    print( gamel )
    assert '\n'+ str(gamel) +'\n' == """
SouriCity: [3, 8]
- bob: [4]
  - action: Attack [10]
  - action: Move [2.0]
- lucy: happy
"""
