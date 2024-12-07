import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.interface as hki

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_support_load():
    sup= hki.SupportSVG()
    assert( type(sup) ) == hki.SupportSVG

    print( sup.render() )
    assert( sup.render() == """<svg width="800" height="600">
</svg>""" )

# Test firstAI launch
def test_support_draw():
    suppo= hki.SupportSVG()

    print( suppo.render() )
    assert( suppo.render() == """<svg width="800" height="600">
</svg>""" )

# Test firstAI launch
def test_support_draw():
    suppo= hki.SupportSVG()
    
    assert( suppo.render() == """<svg width="800" height="600">
</svg>""" )

    suppo.traceLine( -40, 8, 240, 80, 0x25e3f2, 3 )

    print( "---\n" + suppo.render() )
    assert( suppo.render() == """<svg width="800" height="600">
<line x1="-40" y1="8" x2="240" y2="80" style="stroke:#25e3f2;stroke-width:3"/>
</svg>""" )

    suppo.traceCircle( 50, 50, 32, 0x25e3f2, 3 )
    suppo.fillCircle( 100, 50, 32, 0x25e302 )
    suppo.drawCircle( 150, 50, 44, 0x25e302, 0x25e3f2, 8)
    
    assert( suppo.render() == """<svg width="800" height="600">
<line x1="-40" y1="8" x2="240" y2="80" style="stroke:#25e3f2;stroke-width:3"/>
<circle r="32" cx="50" cy="50" fill="none" stroke="#25e3f2" stroke-width="3" />
<circle r="32" cx="100" cy="50" fill="#25e302" />
<circle r="44" cx="150" cy="50" fill="#25e302" stroke="#25e3f2" stroke-width="8" />
</svg>""" )

    suppo.fillPolygon( [30, 140, 70], [130, 130, 200], 0x25e302 )
    suppo.drawPolygon( [70, 190, 130], [130, 130, 200], 0x25e302, 0x25e3f2, 4 )
    suppo.tracePolygon( [10, 10, 790, 790], [10, 590, 590, 10], 0x25e3f2, 6 )

    print( "---\n" + suppo.render() )
    assert( suppo.render() == """<svg width="800" height="600">
<line x1="-40" y1="8" x2="240" y2="80" style="stroke:#25e3f2;stroke-width:3"/>
<circle r="32" cx="50" cy="50" fill="none" stroke="#25e3f2" stroke-width="3" />
<circle r="32" cx="100" cy="50" fill="#25e302" />
<circle r="44" cx="150" cy="50" fill="#25e302" stroke="#25e3f2" stroke-width="8" />
<polygon points="30,130 140,130 70,200" fill="#25e302" />
<polygon points="70,130 190,130 130,200" style="fill:#25e302;stroke:#25e3f2;stroke-width:4" />
<polygon points="10,10 10,590 790,590 790,10" style="fill:none;stroke:#25e3f2;stroke-width:6" />
</svg>""" )