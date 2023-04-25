# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('hackapy')[0] )

import hackapy.pieceOfData as pod

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_Pod_init():
    gamel= pod.Pod()
    assert gamel.status() == "pod"
    assert gamel.attributes() == []
    assert gamel.values() == []
    assert gamel.children() == []

def test_Pod_init2():
    gamel= pod.Pod( "Bob cool", [1, 2, 3], [4.2, 6.9] )
    assert gamel.status() == "Bob cool"
    assert gamel.attributes() == [1, 2, 3]
    assert gamel.values() == [4.2, 6.9]
    assert gamel.children() == []
    for i in range(1,3):
        assert gamel.attribute(i) == i
    assert gamel.value(1) == 4.2
    assert gamel.value(2) == 6.9

def test_Pod_dump():
    gamel= pod.Pod()
    assert gamel.dump() == "3 0 0 0 : pod" # set: "pod-00 (0 0 0 0) state: attrs: values: cells:"
    # assert str(gamel) == "pod [] [] :" 
    gamel.setAttributes([3, 8])
    assert gamel.dump() == "3 2 0 0 : pod 3 8"
    gamel.append( pod.Pod( 'bob happy', [4], [0.6, 10.0] ) )
    assert gamel.dump() == "3 2 0 1 : pod 3 8\n- 9 1 2 0 : bob happy 4 0.6 10.0"
    gamel.append( pod.Pod() )
    assert '\n'+ gamel.dump() +'\n' == """
3 2 0 2 : pod 3 8
- 9 1 2 0 : bob happy 4 0.6 10.0
- 3 0 0 0 : pod
"""

def test_Pod_load():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    assert gamel.dump() == "9 2 0 0 : SouriCity 3 8"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "9 2 0 0 : SouriCity 3 8"

def test_Pod_loadVoid():
    gamel=pod.Pod( '' )
    assert gamel.dump() == "0 0 0 0 :"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "0 0 0 0 :"

def test_Pod_loadVoidStatus():
    gamel=pod.Pod( '', [3, 8] )
    assert gamel.dump() == "0 2 0 0 : 3 8"
    gamel2=pod.Pod().load( gamel.dump() )
    assert gamel2.dump() == "0 2 0 0 : 3 8"

def test_Pod_load2():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    gamel.append(pod.Pod( 'bob, happy', [4] ) )
    gamel.append(pod.Pod( 'lucy', values=[10.0] ) )
    
    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump()  +'\n' == """
9 2 0 2 : SouriCity 3 8
- 10 1 0 0 : bob, happy 4
- 4 0 1 0 : lucy 10.0
"""

def test_Pod_deepDump():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    bob=pod.Pod( 'bob', [4] )
    bob.append(pod.Pod( 'action Attack', [10]) )
    bob.append(pod.Pod( 'action Move', [], [2.0]) )
    gamel.append( bob )
    gamel.append(pod.Pod( 'lucy happy' ) )
    print( gamel.dump() )
    assert '\n'+ gamel.dump() +'\n' == """
9 2 0 2 : SouriCity 3 8
- 3 1 0 2 : bob 4
  - 13 1 0 0 : action Attack 10
  - 11 0 1 0 : action Move 2.0
- 10 0 0 0 : lucy happy
"""

def test_Pod_deepLoad():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    bob=pod.Pod( 'bob', [4] )
    bob.append(pod.Pod( 'action Attack', [10]) )
    bob.append(pod.Pod( 'action Move', [], [2.0]) )
    gamel.append( bob )
    gamel.append(pod.Pod( 'lucy happy' ) )
    gamel2=pod.Pod().load( gamel.dump() )
    assert '\n'+ gamel2.dump() +'\n' == """
9 2 0 2 : SouriCity 3 8
- 3 1 0 2 : bob 4
  - 13 1 0 0 : action Attack 10
  - 11 0 1 0 : action Move 2.0
- 10 0 0 0 : lucy happy
"""

def test_Pod_str():
    gamel=pod.Pod( 'SouriCity', [3, 8] )
    bob=pod.Pod( 'bob', [4] )
    bob.append(pod.Pod( 'action Attack', [10]) )
    bob.append(pod.Pod( 'action Move', [], [2.0]) )
    gamel.append( bob )
    gamel.append(pod.Pod( 'lucy happy' ) )
    print( gamel )
    assert '\n'+ str(gamel) +'\n' == """
SouriCity [3, 8]
- bob [4]
  - action Attack [10]
  - action Move (2.0]
- lucy happy
"""