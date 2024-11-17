import os, sys, pathlib
workdir= __file__.split('/tests/')[0]
sys.path.insert( 1, workdir )

# ------------------------------------------------------------------------ #
#                   T E S T   R I S K Y   G A M E
# ------------------------------------------------------------------------ #

import src.hacka.pylib as hk
from src.hacka.games.risky import GameRisky
from src.hacka.games.risky.viewer import ViewerTerminal

gamePath= workdir + "/src/hacka/games/risky"

# Army Attributes
ACTION= 1
FORCE=  2

#------------------------------------------------------------------------------------------------
# Test Initialize
#------------------------------------------------------------------------------------------------

def test_risky_init():
    game= GameRisky(2)
    game.initialize()
    game.map= "risk-4"

    viewer= ViewerTerminal( game )

    assert len(viewer.grid) == 11

    for line in viewer.grid :
        assert len(line) == 19
        assert line == [' ' for i in range(19)]

buffer= ""

def clearBuffer():
    global buffer
    buffer= ""

def printBuffer(aString):
    global buffer
    buffer+= "\n"+ aString

def test_risky_loadMap():
    global buffer

    game= GameRisky(2)
    game.initialize()

    assert game.map == "board-4"
    mapFile= f"{gamePath}/resources/map-{game.map}.txt"
    assert os.path.exists( mapFile )
    
    f= open(mapFile)
    countLine= 0
    for line in f.readlines() :
        assert len(line) <= 20
        countLine+= 1
    assert countLine == 11

    viewer= ViewerTerminal( game )

    viewer.print( 1, printBuffer)

    print( f"<\n{buffer}\n>" )
#     assert buffer  == """
# ---
# game state: player-1 (turn 1 over 4)
# |        .' '.        |
# |       |     |       |
# |        '. .3        |
# |       /     \       |
# |  .'A'.       .'B'.  |
# | |1- 12|-----|1- 12| |
# |  '. .1       '. .2  |
# |       \     /       |
# |        .' '.        |
# |       |     |       |
# |        '. .4        |"""
