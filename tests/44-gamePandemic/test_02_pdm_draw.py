import sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

"""
Test - Connect4.Engine
"""

import src.hacka.py as hk
import src.hacka.games.pandemic as pdm

def test_initialize_full():
    game= pdm.GameEngine()
    game.initGridFull( 3, 4, 20 )
    game.initialize()

    print( "<----:\n"+"\n".join( game.drawSupport() ) )
    
    assert "\n".join( [""] + game.drawSupport() ) == """
          01      02      03      04 
    ┏━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓
A : ┃       ┃       ┃       ┃       ┃
    ┃       ┃       ┃       ┃       ┃
    ┗━━━┳━━━┻━━━┳━━━┻━━━┳━━━┻━━━┳━━━┻━━━┓
B :     ┃       ┃       ┃       ┃       ┃
        ┃       ┃       ┃       ┃       ┃
    ┏━━━┻━━━┳━━━┻━━━┳━━━┻━━━┳━━━┻━━━┳━━━┛
C : ┃       ┃       ┃       ┃       ┃
    ┃       ┃       ┃       ┃       ┃
    ┗━━━━━━━┻━━━━━━━┻━━━━━━━┻━━━━━━━┛"""
