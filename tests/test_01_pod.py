# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka import Pod

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_Pod_init():
    pod= Pod()

    assert pod.label() == "Pod"
    assert pod.integers() == []
    assert pod.values() == []
    assert pod.children() == []

    assert pod.asDico() == { "label": "Pod", "integers": [], "values": [], "children": [] }

def test_Pod_init2():
    pod= Pod( "Bob", [1, 2, 3], [4.2, 6.9] )
    assert pod.label() == "Bob"
    assert pod.integers() == [1, 2, 3]
    assert pod.values() == [4.2, 6.9]
    assert pod.children() == []

    for i in range(1,3):
        assert pod.integer(i) == i
    assert pod.value(1) == 4.2
    assert pod.value(2) == 6.9

    assert pod.asDico() == { "label": "Bob", "integers": [1, 2, 3], "values": [4.2, 6.9], "children": [] }

def test_Pod_init3():
    podDico=  { "label": "Bob", "integers": [1, 2, 3], "values": [4.2, 6.9], "children": [] }

    pod1= Pod()
    pod1.fromDico( podDico )
    assert pod1.asDico() == podDico
    
    pod2= Pod()
    pod2.fromPod( pod1 )
    assert not ( pod1 is pod2 )
    assert pod2.asDico() == podDico

    pod3= Pod()
    pod3= pod1.asPod()
    assert not ( pod1 is pod3 )
    assert pod3.asDico() == podDico

def test_Pod_str():
    pod1= Pod()
    print( f"---\n{pod1}." )
    assert str(pod1) == "Pod : :"

    pod2= Pod().initialize( "Bob", [1, 2, 3], [4.2, 6.9] )
    print( f"---\n{pod2}." )
    assert str(pod2) == "Bob : 1 2 3 : 4.2 6.9"

    pod3= Pod().initialize( "Master, cool, ChOcoLa", [18, -3, 0], [] )
    pod1.append( Pod().initialize( "Caro", values=[10.5] ) )
    pod3.append( pod1 )
    pod3.append( pod2 )
    print( f"---\n{pod3}." )
    assert "\n"+str(pod3) == """
Master, cool, ChOcoLa : 18 -3 0 :
- Pod : :
  - Caro : : 10.5
- Bob : 1 2 3 : 4.2 6.9"""

def test_Pod_construction():
    pod= Pod()
    
    p= pod.setLabel( "Bob cool" )
    assert p is pod
    
    p= pod.setIntegers( [1, 2, 3] )
    assert p is pod
    
    p= pod.setValues( [4.2, 6.9] )
    assert p is pod
    
    pod2= Pod().initialize( "Caro", values=[10.5] )
    p= pod.setChildren( [pod2] )
    assert p is pod
    
    assert pod.label() == "Bob cool"
    assert pod.integers() == [1, 2, 3]
    assert pod.values() == [4.2, 6.9]
    assert pod.children() == [pod2]
    assert pod.child() is pod2

def test_Pod_dump():
    pod= Pod()
    assert pod.dump_str() == "3 0 0 0 : Pod" # set: "pod-00 (0 0 0 0) state: attrs: values: cells:"
    
    # assert str(gamel) == "pod [] [] :" 
    pod.setIntegers([3, 8])
    assert pod.dump_str() == "3 2 0 0 : Pod 3 8"

    newPod= Pod().initialize( "Bob happy", [4], [0.6, 10.0] )
    assert len( newPod.children() ) == 0

    pod.append( newPod )
    
    assert len( newPod.children() ) == 0
    
    assert len(pod.children()) == 1
    assert pod.child() == newPod
    assert len( pod.child().children() ) == 0
    assert pod.child().dump_str() == "9 1 2 0 : Bob happy 4 0.6 10.0"

    print( pod.dump_str()  )

    assert pod.dump_str() == "3 2 0 1 : Pod 3 8\n9 1 2 0 : Bob happy 4 0.6 10.0"
    pod.append( Pod() )
    
    print( pod.dump_str()  )

    assert '\n'+ pod.dump_str() +'\n' == """
3 2 0 2 : Pod 3 8
9 1 2 0 : Bob happy 4 0.6 10.0
3 0 0 0 : Pod
"""

def test_Pod_load():
    pod= Pod().initialize( 'SouriCity fr', integers=[3, 8] )
    dump= pod.dump_str()
    assert dump == "12 2 0 0 : SouriCity fr 3 8"
    pod2= Pod().load_str( dump )
    
    print( f"> {pod2.label()}" )
    assert pod2.label() == 'SouriCity fr'
    print( f"> {pod2.integers()}" )
    assert pod2.integers() == [3, 8]
    print( f"> {pod2.values()}" )
    assert pod2.values() == []
    
    assert pod2.dump_str() == "12 2 0 0 : SouriCity fr 3 8"

    pod3= Pod().fromPod( pod2 )
    
    print( f"> {pod3.label()}" )
    assert pod3.label() == 'SouriCity fr'
    print( f"> {pod3.integers()}" )
    assert pod3.integers() == [3, 8]
    print( f"> {pod3.values()}" )
    assert pod3.values() == []
    
    assert pod3.dump_str() == "12 2 0 0 : SouriCity fr 3 8"

def test_Pod_load2():
    pod=Pod().initialize( 'SouriCity', integers=[3, 8] )
    pod.append( Pod().initialize( 'bob happy', integers=[4] ) )
    pod.append( Pod().initialize( 'lucy', values=[10.0] ) )
    
    gamel2=Pod().load_str( pod.dump_str() )
    assert '\n'+ gamel2.dump_str()  +'\n' == """
9 2 0 2 : SouriCity 3 8
9 1 0 0 : bob happy 4
4 0 1 0 : lucy 10.0
"""

def test_Pod_load3():
    pod=Pod().initialize( 'SouriCity', integers=[3, 8] )
    pod.append(Pod().initialize( 'bob happy', integers=[4] ) )
    pod.append(Pod().initialize( 'lucy', values=[10.0] ) )

    assert pod.dump_str().splitlines() == [
        "9 2 0 2 : SouriCity 3 8",
        "9 1 0 0 : bob happy 4",
        "4 0 1 0 : lucy 10.0" ]

    pod2=Pod().load_str( pod.dump_str().splitlines() )
    assert '\n'+ pod2.dump_str()  +'\n' == """
9 2 0 2 : SouriCity 3 8
9 1 0 0 : bob happy 4
4 0 1 0 : lucy 10.0
"""

def test_Pod_deep():
    pod=Pod().initialize( 'SouriCity', integers=[3, 8] )
    bob=Pod().initialize( 'bob', integers=[4] )
    bob.append(Pod().initialize( 'action Attack', [10] ) )
    bob.append(Pod().initialize( 'action Move', [], [2.0] ) )
    pod.append( bob )
    pod.append(Pod().initialize( 'lucy happy' ) )
    print( pod.dump_str() )
    assert '\n'+ pod.dump_str() +'\n' == """
9 2 0 2 : SouriCity 3 8
3 1 0 2 : bob 4
13 1 0 0 : action Attack 10
11 0 1 0 : action Move 2.0
10 0 0 0 : lucy happy
"""

    pod2=Pod().load_str( pod.dump_str() )
    assert '\n'+ pod2.dump_str() +'\n' == """
9 2 0 2 : SouriCity 3 8
3 1 0 2 : bob 4
13 1 0 0 : action Attack 10
11 0 1 0 : action Move 2.0
10 0 0 0 : lucy happy
"""

def test_Pod_decode():
    pod= Pod()

    pod.decode("aPod")
    assert pod.asDico() == { "label": "aPod", "integers": [], "values": [], "children": [] }

    pod.decode("aPod : 1 2 3")
    assert pod.asDico() == { "label": "aPod", "integers": [1, 2, 3], "values": [], "children": [] }

    pod.decode("aPod :")
    assert pod.asDico() == { "label": "aPod", "integers": [], "values": [], "children": [] }

    pod.decode("aPod : 43 5 : 7.8 9")
    assert pod.asDico() == { "label": "aPod", "integers": [43, 5], "values": [7.8, 9.0], "children": [] }

    pod.decode("aPod : 43 5 : 7.8 9 ")
    assert pod.asDico() == { "label": "aPod", "integers": [43, 5], "values": [7.8, 9.0], "children": [] }

    pod.decode("aPod : 43 5 : 7.8 9 weds")
    assert pod.asDico() == { "label": "aPod", "integers": [43, 5], "values": [7.8, 9.0], "children": [] }

    pod.decode("aPod : : 7.8 9")
    assert pod.asDico() == { "label": "aPod", "integers": [], "values": [7.8, 9.0], "children": [] }

    pod.decode("aPod : 1 2 3 :")
    assert pod.asDico() == { "label": "aPod", "integers": [1, 2, 3], "values": [], "children": [] }

    pod.decode("aPod : bob : 1 2 3 : 6.5")
    assert pod.asDico() == { "label": "aPod : bob", "integers": [1, 2, 3], "values": [6.5], "children": [] }

