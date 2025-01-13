import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.artist as hka

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_support_load():
    sup= hka.SupportPNG()
    assert( type(sup) ) == hka.SupportPNG

# Test firstAI launch
def test_support_draw():
    sup= hka.SupportPNG()

    sup.save("./tests/outputs/shot-11-cairo-draw.png")

    shotFile= open( "tests/outputs/shot-11-cairo-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-draw-00.png", mode='rb' ).read()
    assert( shotFile == refsFile )
    
    sup.fillPolygon(
        [0, sup.width(), sup.width(), 0],
        [0, 0, sup.height(), sup.height()],
        0xF0F0F0
    )
    sup.traceLine( -40, 8, 240, 80, 0x25e3f2, 3 )
    
    sup.save("./tests/outputs/shot-11-cairo-draw.png")

    shotFile= open( "tests/outputs/shot-11-cairo-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-draw-01.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    sup.traceCircle( 50, 50, 32, 0x25e3f2, 3 )
    sup.fillCircle( 100, 50, 32, 0x25e302 )
    sup.drawCircle( 150, 50, 44, 0x25e302, 0x25e3f2, 8)
    
    sup.save("./tests/outputs/shot-11-cairo-draw.png")

    shotFile= open( "tests/outputs/shot-11-cairo-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-draw-02.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    sup.fillPolygon( [30, 140, 70], [130, 130, 200], 0x25e302 )
    sup.drawPolygon( [70, 190, 130], [130, 130, 200], 0x25e302, 0x25e3f2, 4 )
    sup.tracePolygon( [10, 10, 790, 790], [10, 590, 590, 10], 0x25e3f2, 6 )
    
    sup.save("./tests/outputs/shot-11-cairo-draw.png")

    shotFile= open( "tests/outputs/shot-11-cairo-draw.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-draw-03.png", mode='rb' ).read()
    assert( shotFile == refsFile )

def test_artist_flip():
    pablo= hka.Artist( hka.SupportPNG( filePath="tests/outputs/shot-11-cairo-flip.png" ) )

    assert( type( pablo ) ) == hka.Artist
    assert( type( pablo.support() ) ) == hka.SupportPNG

    assert( pablo.support().filePath() == "tests/outputs/shot-11-cairo-flip.png" )

    shotFile= open( "tests/outputs/shot-11-cairo-flip.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-flip-00.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    pablo.drawFrameGrid()
    pablo.drawFrameAxes()

    pablo.flip()
    
    shotFile= open( "tests/outputs/shot-11-cairo-flip.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-flip-01.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    pablo.flip()

    shotFile= open( "tests/outputs/shot-11-cairo-flip.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-flip-02.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    pablo.drawPolygon( [-1.26, -2.6, -0.4, 3.4], [-2.3, 0.3, 6, -1.7] )
    pablo.drawCircle( 1.26, 2.3, 3.2 )
    pablo.traceLine( -1.26, -2.3, 1.26, 2.3 )
    pablo.fillCircle( -1.26, -2.3, 0.2 )

    pablo.flip()

    shotFile= open( "tests/outputs/shot-11-cairo-flip.png", mode='rb' ).read()
    refsFile= open( "tests/outputs/refs-11-cairo-flip-03.png", mode='rb' ).read()
    assert( shotFile == refsFile )
