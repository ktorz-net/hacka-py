import sys
workDir= __file__.split('/tests/')[0]
sys.path.insert( 1, workDir )

import src.hacka.artist as hka

# ------------------------------------------------------------------------ #
#                 T E S T   I N T E R F A C E    A R T I S T
# ------------------------------------------------------------------------ #

# Test firstAI launch
def test_artist_svg_load():
    shotImg= "shot-test.svg"
    pablo= hka.Artist().initializeSVG( filePath= shotImg )

    shape= [(-0.5, -0.5),  (0.5, -0.5),  (0.5, 0.5),  (-0.5, 0.5)]
    pablo.drawShape( shape, 1 )
    pablo.flip()
    
    shotFile= open( shotImg ).read() 
    refsFile= open( "tests/refs/11.04-artist-panel-01.svg" ).read()
    assert( shotFile == refsFile )

    pablo.drawShape( shape, 0, -2.2, 0 )
    pablo.drawShape( shape, 1, -1.1, 0 )
    pablo.drawShape( shape, 2, 0, 0 )
    pablo.drawShape( shape, 3, 1.1, 0 )
    pablo.drawShape( shape, 4, 2.2, 0 )
    pablo.drawShape( shape, 5, -0.55, 1.1 )
    pablo.drawShape( shape, 6, 0.55, 1.1 )
    pablo.drawShape( shape, 7, -0.55, -1.1 )
    pablo.drawShape( shape, 8, 0.55, -1.1 )
    pablo.flip()
    

    shotFile= open( shotImg ).read() 
    refsFile= open( "tests/refs/11.04-artist-panel-02.svg" ).read()
    assert( shotFile == refsFile )

def test_artist_png_load():
    shotImg= "shot-test.png"
    pablo= hka.Artist().initializePNG( filePath= shotImg )

    shape= [(-0.5, -0.5),  (0.5, -0.5),  (0.5, 0.5),  (-0.5, 0.5)]
    pablo.drawShape( shape, 1 )
    pablo.flip()
    
    shotFile= open( shotImg, mode='rb' ).read() 
    refsFile= open( "tests/refs/11.04-artist-panel-01.png", mode='rb' ).read()
    assert( shotFile == refsFile )

    pablo.drawShape( shape, 0, -2.2, 0 )
    pablo.drawShape( shape, 1, -1.1, 0 )
    pablo.drawShape( shape, 2, 0, 0 )
    pablo.drawShape( shape, 3, 1.1, 0 )
    pablo.drawShape( shape, 4, 2.2, 0 )
    pablo.drawShape( shape, 5, -0.55, 1.1 )
    pablo.drawShape( shape, 6, 0.55, 1.1 )
    pablo.drawShape( shape, 7, -0.55, -1.1 )
    pablo.drawShape( shape, 8, 0.55, -1.1 )
    pablo.flip()
    
    shotFile= open( shotImg, mode='rb' ).read() 
    refsFile= open( "tests/refs/11.04-artist-panel-02.png", mode='rb' ).read()
    assert( shotFile == refsFile )
