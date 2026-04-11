# HackaGames UnitTest - `pytest`
import sys
sys.path.insert( 1, __file__.split('tests')[0] )

from src.hacka import DataTree

# ------------------------------------------------------------------------ #
#         T E S T   H A C K A G A M E S - P I E C E  O F  D A T A
# ------------------------------------------------------------------------ #

def test_DataTree_init():
    datatree= DataTree()

    assert datatree.label() == "DataTree"
    assert datatree.digits() == []
    assert datatree.values() == []
    assert datatree.children() == []

    assert datatree.asDico() == { "label": "DataTree", "digits": [], "values": [], "children": [] }

def test_DataTree_init2():
    datatree= DataTree( "Bob", [1, 2, 3], [4.2, 6.9] )
    assert datatree.label() == "Bob"
    assert datatree.digits() == [1, 2, 3]
    assert datatree.values() == [4.2, 6.9]
    assert datatree.children() == []

    for i in range(1,3):
        assert datatree.digit(i) == i
    assert datatree.value(1) == 4.2
    assert datatree.value(2) == 6.9

    assert datatree.asDico() == { "label": "Bob", "digits": [1, 2, 3], "values": [4.2, 6.9], "children": [] }

def test_DataTree_init3():
    datatreeDico=  { "label": "Bob", "digits": [1, 2, 3], "values": [4.2, 6.9], "children": [] }

    datatree1= DataTree()
    datatree1.fromDico( datatreeDico )
    assert datatree1.asDico() == datatreeDico
    
    datatree2= DataTree()
    datatree2.fromDataTree( datatree1 )
    assert not ( datatree1 is datatree2 )
    assert datatree2.asDico() == datatreeDico

    datatree3= DataTree()
    datatree3= datatree1.asDataTree()
    assert not ( datatree1 is datatree3 )
    assert datatree3.asDico() == datatreeDico

def test_DataTree_str():
    datatree1= DataTree()
    print( f"---\n{datatree1}." )
    assert str(datatree1) == "DataTree : :"

    datatree2= DataTree().initialize( "Bob", [1, 2, 3], [4.2, 6.9] )
    print( f"---\n{datatree2}." )
    assert str(datatree2) == "Bob : 1 2 3 : 4.2 6.9"

    datatree3= DataTree().initialize( "Master, cool, ChOcoLa", [18, -3, 0], [] )
    datatree1.append( DataTree().initialize( "Caro", values=[10.5] ) )
    datatree3.append( datatree1 )
    datatree3.append( datatree2 )
    print( f"---\n{datatree3}." )
    assert "\n"+str(datatree3) == """
Master, cool, ChOcoLa : 18 -3 0 :
- DataTree : :
  - Caro : : 10.5
- Bob : 1 2 3 : 4.2 6.9"""

def test_DataTree_construction():
    datatree= DataTree()
    
    p= datatree.setLabel( "Bob cool" )
    assert p is datatree
    
    p= datatree.setIntegers( [1, 2, 3] )
    assert p is datatree
    
    p= datatree.setValues( [4.2, 6.9] )
    assert p is datatree
    
    datatree2= DataTree().initialize( "Caro", values=[10.5] )
    p= datatree.setChildren( [datatree2] )
    assert p is datatree
    
    assert datatree.label() == "Bob cool"
    assert datatree.digits() == [1, 2, 3]
    assert datatree.values() == [4.2, 6.9]
    assert datatree.children() == [datatree2]
    assert datatree.child() is datatree2

def test_DataTree_dump():
    datatree= DataTree()
    assert datatree.dump_txt() == "8 0 0 0 : DataTree" # set: "datatree-00 (0 0 0 0) state: attrs: values: cells:"
    
    # assert str(gamel) == "datatree [] [] :" 
    datatree.setIntegers([3, 8])
    assert datatree.dump_txt() == "8 2 0 0 : DataTree 3 8"

    newDataTree= DataTree().initialize( "Bob happy", [4], [0.6, 10.0] )
    assert len( newDataTree.children() ) == 0

    datatree.append( newDataTree )
    
    assert len( newDataTree.children() ) == 0
    
    assert len(datatree.children()) == 1
    assert datatree.child() == newDataTree
    assert len( datatree.child().children() ) == 0
    assert datatree.child().dump_txt() == "9 1 2 0 : Bob happy 4 0.6 10.0"

    print( datatree.dump_txt()  )

    assert datatree.dump_txt() == "8 2 0 1 : DataTree 3 8\n9 1 2 0 : Bob happy 4 0.6 10.0"
    datatree.append( DataTree() )
    
    print( datatree.dump_txt()  )

    assert '\n'+ datatree.dump_txt() +'\n' == """
8 2 0 2 : DataTree 3 8
9 1 2 0 : Bob happy 4 0.6 10.0
8 0 0 0 : DataTree
"""

def test_DataTree_load():
    datatree= DataTree().initialize( 'SouriCity fr', digits=[3, 8] )
    dump= datatree.dump_txt()
    assert dump == "12 2 0 0 : SouriCity fr 3 8"
    datatree2= DataTree().load_txt( dump )
    
    print( f"> {datatree2.label()}" )
    assert datatree2.label() == 'SouriCity fr'
    print( f"> {datatree2.digits()}" )
    assert datatree2.digits() == [3, 8]
    print( f"> {datatree2.values()}" )
    assert datatree2.values() == []
    
    assert datatree2.dump_txt() == "12 2 0 0 : SouriCity fr 3 8"

    datatree3= DataTree().fromDataTree( datatree2 )
    
    print( f"> {datatree3.label()}" )
    assert datatree3.label() == 'SouriCity fr'
    print( f"> {datatree3.digits()}" )
    assert datatree3.digits() == [3, 8]
    print( f"> {datatree3.values()}" )
    assert datatree3.values() == []
    
    assert datatree3.dump_txt() == "12 2 0 0 : SouriCity fr 3 8"

def test_DataTree_load2():
    datatree=DataTree().initialize( 'SouriCity', digits=[3, 8] )
    datatree.append( DataTree().initialize( 'bob happy', digits=[4] ) )
    datatree.append( DataTree().initialize( 'lucy', values=[10.0] ) )
    
    gamel2=DataTree().load_txt( datatree.dump_txt() )
    assert '\n'+ gamel2.dump_txt()  +'\n' == """
9 2 0 2 : SouriCity 3 8
9 1 0 0 : bob happy 4
4 0 1 0 : lucy 10.0
"""

def test_DataTree_load3():
    datatree=DataTree().initialize( 'SouriCity', digits=[3, 8] )
    datatree.append(DataTree().initialize( 'bob happy', digits=[4] ) )
    datatree.append(DataTree().initialize( 'lucy', values=[10.0] ) )

    assert datatree.dump_txt().splitlines() == [
        "9 2 0 2 : SouriCity 3 8",
        "9 1 0 0 : bob happy 4",
        "4 0 1 0 : lucy 10.0" ]

    datatree2=DataTree().load_txt( datatree.dump_txt().splitlines() )
    assert '\n'+ datatree2.dump_txt()  +'\n' == """
9 2 0 2 : SouriCity 3 8
9 1 0 0 : bob happy 4
4 0 1 0 : lucy 10.0
"""

def test_DataTree_deep():
    datatree=DataTree().initialize( 'SouriCity', digits=[3, 8] )
    bob=DataTree().initialize( 'bob', digits=[4] )
    bob.append(DataTree().initialize( 'action Attack', [10] ) )
    bob.append(DataTree().initialize( 'action Move', [], [2.0] ) )
    datatree.append( bob )
    datatree.append(DataTree().initialize( 'lucy happy' ) )
    print( datatree.dump_txt() )
    assert '\n'+ datatree.dump_txt() +'\n' == """
9 2 0 2 : SouriCity 3 8
3 1 0 2 : bob 4
13 1 0 0 : action Attack 10
11 0 1 0 : action Move 2.0
10 0 0 0 : lucy happy
"""

    datatree2=DataTree().load_txt( datatree.dump_txt() )
    assert '\n'+ datatree2.dump_txt() +'\n' == """
9 2 0 2 : SouriCity 3 8
3 1 0 2 : bob 4
13 1 0 0 : action Attack 10
11 0 1 0 : action Move 2.0
10 0 0 0 : lucy happy
"""

def test_DataTree_decode():
    datatree= DataTree()

    datatree.decode("aDataTree")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [], "values": [], "children": [] }

    datatree.decode("aDataTree : 1 2 3")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [1, 2, 3], "values": [], "children": [] }

    datatree.decode("aDataTree :")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [], "values": [], "children": [] }

    datatree.decode("aDataTree : 43 5 : 7.8 9")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [43, 5], "values": [7.8, 9.0], "children": [] }

    datatree.decode("aDataTree : 43 5 : 7.8 9 ")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [43, 5], "values": [7.8, 9.0], "children": [] }

    datatree.decode("aDataTree : 43 5 : 7.8 9 weds")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [43, 5], "values": [7.8, 9.0], "children": [] }

    datatree.decode("aDataTree : : 7.8 9")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [], "values": [7.8, 9.0], "children": [] }

    datatree.decode("aDataTree : 1 2 3 :")
    assert datatree.asDico() == { "label": "aDataTree", "digits": [1, 2, 3], "values": [], "children": [] }

    datatree.decode("aDataTree : bob : 1 2 3 : 6.5")
    assert datatree.asDico() == { "label": "aDataTree : bob", "digits": [1, 2, 3], "values": [6.5], "children": [] }

def test_DataTree_serialize_bin():
    datatree1= DataTree().initialize( 'SouriCity fr', digits=[3, 8] )
    dump= datatree1.dump_bin()
    
    print( dump )
    assert bytes(dump) == b'\x0c\x00\x02\x00\x00\x00\x00\x00SouriCity fr\x03\x00\x08\x00'
    
    cpy= DataTree().load_bin( dump )
    
    print( f"> {cpy.label()}" )
    assert cpy.label() == 'SouriCity fr'
    print( f"> {cpy.digits()}" )
    assert cpy.digits() == [3, 8]
    print( f"> {cpy.values()}" )
    assert cpy.values() == []
    
    datatree2 = DataTree().initialize( 'tadam', [3, 8], [3.008, -8.7, 0.001] )
    dump= datatree2.dump_bin()
    cpy= DataTree().load_bin( dump )
    
    print( f"> {cpy.label()}" )
    assert cpy.label() == 'tadam'
    print( f"> {cpy.digits()}" )
    assert cpy.digits() == [3, 8]
    print( f"> {cpy.values()}" )
    assert cpy.values() == [3.008, -8.7, 0.001]

    datatree3 = DataTree().initialize(
        'goal', [4], [0.0, 1.01],
         [datatree1, datatree2]
    )
    dump= datatree3.dump_bin()
    print( bytes(dump) )
    cpy= DataTree().load_bin( dump )
    
    assert str(cpy) == """goal : 4 : 0.0 1.01
- SouriCity fr : 3 8 :
- tadam : 3 8 : 3.008 -8.7 0.001"""

    datatree4 = DataTree().initialize(
        'final', children= [datatree3]
    )
    dump= datatree4.dump_bin()
    print( bytes(dump) )
    cpy= DataTree().load_bin( dump )
    
    print( f"> {cpy}" )
    assert str(cpy) == """final : :
- goal : 4 : 0.0 1.01
  - SouriCity fr : 3 8 :
  - tadam : 3 8 : 3.008 -8.7 0.001"""