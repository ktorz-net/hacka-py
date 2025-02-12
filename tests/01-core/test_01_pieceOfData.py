# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

import src.hacka.py.pod as pod

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_Pod_init():
    gamel= pod.Pod()
    assert gamel.wordAttributes() == []
    assert gamel.intAttributes() == []
    assert gamel.floatAttributes() == []
    assert gamel.children() == []

def test_Pod_init2():
    gamel= pod.Pod( ["Bob", "cool"], [1, 2, 3], [4.2, 6.9] )
    assert gamel.wordAttributes() == ["Bob", "cool"]
    assert gamel.intAttributes() == [1, 2, 3]
    assert gamel.floatAttributes() == [4.2, 6.9]
    assert gamel.children() == []

    for i in range(1,3):
        assert gamel.intAttribute(i) == i
    assert gamel.floatAttribute(1) == 4.2
    assert gamel.floatAttribute(2) == 6.9

def test_Pod_dump():
    gamel= pod.Pod()
    assert gamel.dump() == "0 0 0 0 0 :" # set: "pod-00 (0 0 0 0) state: attrs: values: cells:"
    # assert str(gamel) == "pod [] [] :" 
    gamel.setIntAttributes([3, 8])
    assert gamel.dump() == "0 0 2 0 0 : 3 8"

    newPod= pod.Pod( ['Bob', "happy"], [4], [0.6, 10.0] )
    assert len( newPod.children() ) == 0

    gamel.appendChild( newPod )
    
    assert len( newPod.children() ) == 0
    
    assert len(gamel.children()) == 1
    assert gamel.child() == newPod
    assert len( gamel.child().children() ) == 0
    assert gamel.child().dump() == "2 5 1 2 0 : Bob happy 4 0.6 10.0"

    print( gamel.dump()  )

    assert gamel.dump() == "0 0 2 0 1 : 3 8\n2 5 1 2 0 : Bob happy 4 0.6 10.0"
    gamel.appendChild( pod.Pod() )
    assert '\n'+ gamel.dump() +'\n' == """
0 0 2 0 2 : 3 8
2 5 1 2 0 : Bob happy 4 0.6 10.0
0 0 0 0 0 :
"""

def test_Pod_load():
    gamel=pod.Pod( ['SouriCity', 'fr'], integers=[3, 8] )
    assert gamel.dump() == "2 9 2 0 0 : SouriCity fr 3 8"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "2 9 2 0 0 : SouriCity fr 3 8"

def test_Pod_load2():
    gamel=pod.Pod( 'SouriCity', integers=[3, 8] )
    gamel.appendChild(pod.Pod( ['bob', 'happy'], integers=[4] ) )
    gamel.appendChild(pod.Pod( 'lucy', values=[10.0] ) )
    
    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump()  +'\n' == """
1 9 2 0 2 : SouriCity 3 8
2 5 1 0 0 : bob happy 4
1 4 0 1 0 : lucy 10.0
"""

def test_Pod_load3():
    gamel=pod.Pod( 'SouriCity', integers=[3, 8] )
    gamel.appendChild(pod.Pod( ['bob', 'happy'], integers=[4] ) )
    gamel.appendChild(pod.Pod( 'lucy', values=[10.0] ) )

    assert gamel.dump().splitlines() == [
        "1 9 2 0 2 : SouriCity 3 8",
        "2 5 1 0 0 : bob happy 4",
        "1 4 0 1 0 : lucy 10.0" ]

    gamel2=pod.Pod().load( gamel.dump().splitlines() )
    assert '\n'+ gamel2.dump()  +'\n' == """
1 9 2 0 2 : SouriCity 3 8
2 5 1 0 0 : bob happy 4
1 4 0 1 0 : lucy 10.0
"""

def test_Pod_deep():
    gamel=pod.Pod( 'SouriCity', integers=[3, 8] )
    bob=pod.Pod( 'bob', integers=[4] )
    bob.appendChild(pod.Pod( ['action', "Attack"], [10] ) )
    bob.appendChild(pod.Pod( ['action', "Move"], [], [2.0] ) )
    gamel.appendChild( bob )
    gamel.appendChild(pod.Pod( ['lucy', 'happy'] ) )
    print( gamel.dump() )
    assert '\n'+ gamel.dump() +'\n' == """
1 9 2 0 2 : SouriCity 3 8
1 3 1 0 2 : bob 4
2 6 1 0 0 : action Attack 10
2 6 0 1 0 : action Move 2.0
2 5 0 0 0 : lucy happy
"""

    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump() +'\n' == """
1 9 2 0 2 : SouriCity 3 8
1 3 1 0 2 : bob 4
2 6 1 0 0 : action Attack 10
2 6 0 1 0 : action Move 2.0
2 5 0 0 0 : lucy happy
"""

def test_Pod_str():
    gamel=pod.Pod( 'SouriCity', integers=[3, 8] )
    bob=pod.Pod( 'bob', integers=[4] )
    bob.appendChild( pod.Pod( ['action', "Attack"], [10] ) )
    bob.appendChild(pod.Pod( ['action', "Move"], [], [2.0] ) )
    gamel.appendChild( bob )
    gamel.appendChild(pod.Pod( ['lucy', 'happy'] ) )
    print( gamel )
    assert '\n'+ str(gamel) +'\n' == """
SouriCity: [3, 8]
- bob: [4]
  - action: Attack [10]
  - action: Move [2.0]
- lucy: happy
"""
