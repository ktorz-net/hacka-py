import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.interface as hki

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_support_load():
    sup= hki.SupportPNG()
    assert( type(sup) ) == hki.SupportPNG

# Test firstAI launch
def test_support_draw():
    sup= hki.SupportPNG()

    sup.save("./tests/outputs/shot-supportPNG-draw.png")

    shotFile= open( "tests/outputs/shot-supportPNG-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-supportPNG-draw-00.png", mode='rb' ).read()
    assert( shotFile == refsFile )


    sup.fillPolygon(
        [0, sup.width(), sup.width(), 0],
        [0, 0, sup.height(), sup.height()],
        0xF0F0F0
    )
    sup.traceLine( -40, 8, 240, 80, 0x25e3f2, 3 )
    
    sup.save("./tests/outputs/shot-supportPNG-draw.png")

    shotFile= open( "tests/outputs/shot-supportPNG-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-supportPNG-draw-01.png", mode='rb' ).read()

    assert( shotFile == refsFile )

    sup.traceCircle( 50, 50, 32, 0x25e3f2, 3 )
    sup.fillCircle( 100, 50, 32, 0x25e302 )
    sup.drawCircle( 150, 50, 44, 0x25e302, 0x25e3f2, 8)
    
    sup.save("./tests/outputs/shot-supportPNG-draw.png")

    shotFile= open( "tests/outputs/shot-supportPNG-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-supportPNG-draw-02.png", mode='rb' ).read()

    sup.fillPolygon( [30, 140, 70], [130, 130, 200], 0x25e302 )
    sup.drawPolygon( [70, 190, 130], [130, 130, 200], 0x25e302, 0x25e3f2, 4 )
    sup.tracePolygon( [10, 10, 790, 790], [10, 590, 590, 10], 0x25e3f2, 6 )
    
    sup.save("./tests/outputs/shot-supportPNG-draw.png")

    shotFile= open( "tests/outputs/shot-supportPNG-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-supportPNG-draw-03.png", mode='rb' ).read()


def test_artist_load():
    pablo= hki.Artist( hki.SupportSVG() )

    assert( type( pablo ) ) == hki.Artist
    assert( type( pablo.support() ) ) == hki.SupportSVG

    assert( pablo.render() == """<svg width="800" height="600">
<polygon points="0,0 0,600 800,600 800,0" fill="#ffbb55" />
</svg>""" )

    pablo.drawFrameGrid()
    pablo.drawFrameAxes()

    #pablo.support().save( "shot-test.svg" )

    assert( pablo.render() == """<svg width="800" height="600">
<polygon points="0,0 0,600 800,600 800,0" fill="#ffbb55" />
<line x1="100.0" y1="10" x2="100.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="200.0" y1="10" x2="200.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="300.0" y1="10" x2="300.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="400.0" y1="10" x2="400.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="500.0" y1="10" x2="500.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="600.0" y1="10" x2="600.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="700.0" y1="10" x2="700.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="800.0" y1="10" x2="800.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="900.0" y1="10" x2="900.0" y2="590" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="100.0" x2="790" y2="100.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="200.0" x2="790" y2="200.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="300.0" x2="790" y2="300.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="400.0" x2="790" y2="400.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="500.0" x2="790" y2="500.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="600.0" x2="790" y2="600.0" style="stroke:#080800;stroke-width:2"/>
<line x1="10" y1="700.0" x2="790" y2="700.0" style="stroke:#080800;stroke-width:2"/>
<line x1="400.0" y1="300.0" x2="500.0" y2="300.0" style="stroke:#e26060;stroke-width:4"/>
<line x1="400.0" y1="300.0" x2="400.0" y2="200.0" style="stroke:#60e260;stroke-width:4"/>
<circle r="4" cx="400.0" cy="300.0" fill="#0606e2" />
</svg>""" )


def test_artist_flip():
    pablo= hki.Artist( hki.SupportSVG( filePath="tests/outputs/shot-artistSVG-flip.svg" ) )

    assert( pablo.support().filePath() == "tests/outputs/shot-artistSVG-flip.svg" )

    shotFile= open( "tests/outputs/shot-artistSVG-flip.svg" ) 
    refsFile= open( "tests/outputs/refs-artistSVG-flip-00.svg" ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )

    pablo.drawFrameGrid()
    pablo.drawFrameAxes()

    pablo.flip()

    shotFile= open( "tests/outputs/shot-artistSVG-flip.svg" ) 
    refsFile= open( "tests/outputs/refs-artistSVG-flip-01.svg" ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )

    pablo.flip()

    shotFile= open( "tests/outputs/shot-artistSVG-flip.svg" ) 
    refsFile= open( "tests/outputs/refs-artistSVG-flip-02.svg" ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )

    pablo.drawPolygon( [-1.26, -2.6, -0.4, 3.4], [-2.3, 0.3, 6, -1.7] )
    pablo.drawCircle( 1.26, 2.3, 3.2 )
    pablo.traceLine( -1.26, -2.3, 1.26, 2.3 )
    pablo.fillCircle( -1.26, -2.3, 0.2 )

    pablo.flip()

    shotFile= open( "tests/outputs/shot-artistSVG-flip.svg" ) 
    refsFile= open( "tests/outputs/refs-artistSVG-flip-03.svg" ) 
    for lineShot, lineRef in zip( shotFile, refsFile ):
        assert( lineShot == lineRef )
    
"""
def test_artist_tile():
    pablo= hki.Artist()
    suppo= hki.SupportSVG()
    
    tile= Tile()

    assert tile.number() == 0
    assert tile.center() == (0.0, 0.0)
    assert tile.limits() == [(-0.5, 0.5), (0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]
    assert tile.adjacencies() == []
    assert tile.pieces() == []
    
    tile= Tile( 3, (10.3, 9.7), 42.0 )

    assert tile.number() == 3
    assert tile.stamp() == 0
    assert tile.center() == (10.3, 9.7)
    assert tile.limits() == [(-10.7, 30.7), (31.3, 30.7), (31.3, -11.3), (-10.7, -11.3)]
    assert tile.adjacencies() == []
    assert tile.pieces() == []
"""
 