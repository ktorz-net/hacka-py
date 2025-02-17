# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka.py import Pod, Pod256

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_Pod_init():
    pod= Pod()
    assert pod.words() == []
    assert pod.integers() == []
    assert pod.values() == []
    assert pod.children() == []

def test_Pod_init2():
    pod= Pod().fromLists( ["Bob", "cool"], [1, 2, 3], [4.2, 6.9] )
    assert pod.words() == ["Bob", "cool"]
    assert pod.integers() == [1, 2, 3]
    assert pod.values() == [4.2, 6.9]
    assert pod.children() == []

    for i in range(1,3):
        assert pod.integer(i) == i
    assert pod.value(1) == 4.2
    assert pod.value(2) == 6.9

def test_Pod_str():
    pod1= Pod()
    print( f"---\n{pod1}." )
    assert str(pod1) == "Pod:"

    pod2= Pod().fromLists( ["Bob", "cool"], [1, 2, 3], [4.2, 6.9] )
    print( f"---\n{pod2}." )
    assert str(pod2) == "Bob: cool [1, 2, 3] [4.2, 6.9]"

    pod3= Pod().fromLists( ["Master", "cool", "ChOcoLa"], [18, -3, 0], [] )
    pod1.append( Pod().fromLists( ["Caro"], values=[10.5] ) )
    pod3.append( pod1 )
    pod3.append( pod2 )
    print( f"---\n{pod3}." )
    assert "\n"+str(pod3) == """
Master: cool, ChOcoLa [18, -3, 0]
- Pod:
  - Caro: [10.5]
- Bob: cool [1, 2, 3] [4.2, 6.9]"""

def test_Pod_construction():
    pod= Pod()
    
    p= pod.setWords( ["Bob", "cool"] )
    assert p is pod
    
    p= pod.setIntegers( [1, 2, 3] )
    assert p is pod
    
    p= pod.setValues( [4.2, 6.9] )
    assert p is pod
    
    pod2= Pod().fromLists( ["Caro"], values=[10.5] )
    p= pod.setChildren( [pod2] )
    assert p is pod
    
    assert pod.words() == ["Bob", "cool"]
    assert pod.integers() == [1, 2, 3]
    assert pod.values() == [4.2, 6.9]
    assert pod.children() == [pod2]
    assert pod.child() is pod2

def test_Pod256_dump():
    pod= Pod256()
    assert pod.dump_str() == "0 0 0 0 0 :" # set: "pod-00 (0 0 0 0) state: attrs: values: cells:"
    
    # assert str(gamel) == "pod [] [] :" 
    pod.setIntegers([3, 8])
    assert pod.dump_str() == "0 0 2 0 0 : 3 8"

    newPod= Pod256().fromLists( ['Bob', "happy"], [4], [0.6, 10.0] )
    assert len( newPod.children() ) == 0

    pod.append( newPod )
    
    assert len( newPod.children() ) == 0
    
    assert len(pod.children()) == 1
    assert pod.child() == newPod
    assert len( pod.child().children() ) == 0
    assert pod.child().dump_str() == "2 5 1 2 0 : Bob happy 4 0.6 10.0"

    print( pod.dump_str()  )

    assert pod.dump_str() == "0 0 2 0 1 : 3 8\n2 5 1 2 0 : Bob happy 4 0.6 10.0"
    pod.append( Pod256() )
    assert '\n'+ pod.dump_str() +'\n' == """
0 0 2 0 2 : 3 8
2 5 1 2 0 : Bob happy 4 0.6 10.0
0 0 0 0 0 :
"""

def test_Pod256_load():
    pod=Pod().fromLists( ['SouriCity', 'fr'], integers=[3, 8] )
    dump= Pod256(pod).dump_str()
    assert dump == "2 9 2 0 0 : SouriCity fr 3 8"
    pod2= Pod256().load_str( dump )
    
    print( f"> {pod2.words()}" )
    assert pod2.words() == ['SouriCity', 'fr']
    print( f"> {pod2.integers()}" )
    assert pod2.integers() == [3, 8]
    print( f"> {pod2.values()}" )
    assert pod2.values() == []
    
    assert pod2.dump_str() == "2 9 2 0 0 : SouriCity fr 3 8"

    pod3= Pod().fromPod( pod2 )
    
    print( f"> {pod3.words()}" )
    assert pod3.words() == ['SouriCity', 'fr']
    print( f"> {pod3.integers()}" )
    assert pod3.integers() == [3, 8]
    print( f"> {pod3.values()}" )
    assert pod3.values() == []
    
    assert Pod256(pod3).dump_str() == "2 9 2 0 0 : SouriCity fr 3 8"

def test_Pod256_load2():
    pod=Pod256().fromLists( ['SouriCity'], integers=[3, 8] )
    pod.append( Pod256().fromLists( ['bob', 'happy'], integers=[4] ) )
    pod.append( Pod256().fromLists( ['lucy'], values=[10.0] ) )
    
    gamel2=Pod256().load_str( pod.dump_str() )
    assert '\n'+ gamel2.dump_str()  +'\n' == """
1 9 2 0 2 : SouriCity 3 8
2 5 1 0 0 : bob happy 4
1 4 0 1 0 : lucy 10.0
"""

def test_Pod256_load3():
    pod=Pod256().fromLists( ['SouriCity'], integers=[3, 8] )
    pod.append(Pod256().fromLists( ['bob', 'happy'], integers=[4] ) )
    pod.append(Pod256().fromLists( ['lucy'], values=[10.0] ) )

    assert pod.dump_str().splitlines() == [
        "1 9 2 0 2 : SouriCity 3 8",
        "2 5 1 0 0 : bob happy 4",
        "1 4 0 1 0 : lucy 10.0" ]

    pod2=Pod256().load_str( pod.dump_str().splitlines() )
    assert '\n'+ pod2.dump_str()  +'\n' == """
1 9 2 0 2 : SouriCity 3 8
2 5 1 0 0 : bob happy 4
1 4 0 1 0 : lucy 10.0
"""

def test_Pod256_deep():
    pod=Pod256().fromLists( ['SouriCity'], integers=[3, 8] )
    bob=Pod256().fromLists( ['bob'], integers=[4] )
    bob.append(Pod256().fromLists( ['action', "Attack"], [10] ) )
    bob.append(Pod256().fromLists( ['action', "Move"], [], [2.0] ) )
    pod.append( bob )
    pod.append(Pod256().fromLists( ['lucy', 'happy'] ) )
    print( pod.dump_str() )
    assert '\n'+ pod.dump_str() +'\n' == """
1 9 2 0 2 : SouriCity 3 8
1 3 1 0 2 : bob 4
2 6 1 0 0 : action Attack 10
2 6 0 1 0 : action Move 2.0
2 5 0 0 0 : lucy happy
"""

    pod2=Pod256().load_str( pod.dump_str() )
    assert '\n'+ pod2.dump_str() +'\n' == """
1 9 2 0 2 : SouriCity 3 8
1 3 1 0 2 : bob 4
2 6 1 0 0 : action Attack 10
2 6 0 1 0 : action Move 2.0
2 5 0 0 0 : lucy happy
"""

