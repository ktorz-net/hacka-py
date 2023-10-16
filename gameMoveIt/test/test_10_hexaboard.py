"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def test_Hexaboard():
    board= ge.Hexaboard()
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (8, 6) )
    print( board.shell() )
    test= [
"          ▁         ▁         ▁         ▁         ▁         ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         █         █         █         █         █         █         █         █",
"     █         █         █         █         █         █         █         █         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█         █         █         █         █         █         █         █         █     ",
"█         █         █         █         █         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔         ▔         ▔         ▔         ▔          "]

    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)


def test_Obstacles():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(2, 1).setObstacle()

    assert( board.at(0, 0).type() == ge.Cell.TYPE_FREE )
    assert( board.at(2, 1).type() == ge.Cell.TYPE_OBSTACLE )
    assert( board.at(2, 2).type() == ge.Cell.TYPE_FREE )
    assert( board.at(2, 0).type() == ge.Cell.TYPE_FREE )
    assert( board.at(3, 2).type() == ge.Cell.TYPE_FREE )

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗  ",
"     █         █         ███████████         █",
"     █         █         ███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

    board.at(0, 0).setObstacle()
    board.at(1, 0).setObstacle()
    board.at(1, 1).setObstacle()
    board.at(2, 1).setFree()

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗  ",
"     █         ███████████         █         █",
"     █         ███████████         █         █",
"  ▄▟███▙▄   ▄▟████████▛▀   ▘▗   ▖▝   ▘▗   ▖▝  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)
    
    board.at(0, 1).setObstacle()
    board.at(0, 2).setObstacle()
    board.at(1, 2).setObstacle()
    board.at(3, 1).setObstacle()
    
    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▄▟███▙▄   ▄▟███▙▄   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜██████████████████▙▄   ▖▝   ▘▗   ▄▟███▙▄  ",
"     █████████████████████         ███████████",
"     █████████████████████         ███████████",
"  ▄▟██████████████████▛▀   ▘▗   ▖▝   ▀▜███▛▀  ",
"█████████████████████         █         █     ",
"█████████████████████         █         █     ",
"  ▀▜███▛▀   ▀▜███▛▀   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2)

def test_Robot():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(2, 1).setObstacle()
    assert( board.at(1, 1).setRobot( ge.Robot(12) ) == True )
    assert( board.at(1, 1).setRobot( ge.Robot(1) ) == False )
    assert( board.at(2, 1).setRobot( ge.Robot(1) ) == False )

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄   ▖▝   ▘▗  ",
"     █         █  ⎛R  ⎞  ███████████         █",
"     █         █  ⎝ 12⎠  ███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█        1█         █         █         █     ",
"█        2█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    r8= ge.Robot(8)
    r8.setGoal(1,1)
    assert( board.at(3, 2).setRobot( r8 ) == True )

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  8⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄▔▔▔▖▝   ▘▗  ",
"     █         █  ⎛R  ⎞  ███████████         █",
"     █         █  ⎝ 12⎠ 8███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█        1█         █         █         █     ",
"█        2█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )
    
    board.at(1, 1).removeRobot()

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  8⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄▔▔▔▖▝   ▘▗  ",
"     █         █         ███████████         █",
"     █         █        8███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

def test_move():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(3, 1).setObstacle()
    board.at(1, 1).setRobot( ge.Robot(1) )
    
    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▄▟███▙▄  ",
"     █         █  ⎛R  ⎞  █         ███████████",
"     █         █  ⎝  1⎠  █         ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    dirs= []
    for i in range(7):
        dirs.append( board.at_dir( 0, 0, i ) )
    assert( dirs == [(0, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1)] )

    dirs= []
    for i in range(7):
        dirs.append( board.at_dir( 3, 2, i ) )
    assert( dirs == [(3, 2), (3, 3), (4, 2), (3, 1), (2, 1), (2, 2), (2, 3)] )

    dirs= []
    for i in range(7):
        dirs.append( board.at_dir( 1, 1, i ) )
    assert( dirs == [(1, 1), (2, 2), (2, 1), (2, 0), (1, 0), (0, 1), (1, 2)] )

    assert( board.at_dir(1, 1, 4) == (1, 0) )

    assert( board.movesFrom(1, 1) == [0, 1, 2, 3, 4, 5, 6] )
    assert( board.moveRobotAt_dir(1, 1, 4) == (1, 0) )
    assert( board.movesFrom(1, 0) == [0, 1, 2, 5, 6] )
    assert( board.moveRobotAt_dir(1, 0, 5) == (0, 0) )
    assert( board.movesFrom(0, 0) == [0, 1, 2] )

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗       ",
"█         █         █         █         █     ",
"█         █         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄  ",
"     █         █         █         ███████████",
"     █         █         █         ███████████",
"  ▖▝▁▁▁▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█  ⎛R  ⎞  █         █         █         █     ",
"█  ⎝  1⎠ 1█         █         █         █     ",
"  ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    assert( board.moveRobotAt_dir(0, 0, 5) == (0, 0) )
    assert( board.moveRobotAt_dir(1, 1, 5) == (1, 1) )

    robot= board.at(0, 0).removeRobot()
    board.at(3, 2).setRobot(robot)

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  1⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄  ",
"     █         █         █         ███████████",
"     █         █         █         ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    assert( board.at_dir(3, 2, 3) == (3, 1) )
    assert( board.at(3, 1).isObstacle() )
    assert( board.movesFrom(3, 2) == [0, 4, 5] )

def test_multi():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(3, 1).setObstacle()
    board.at(1, 1).setRobot( ge.Robot(1) )
    board.at(2, 2).setRobot( ge.Robot(2) )
    board.at(2, 2).robot().setGoal(3, 0)
    
    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗       ",
"█         █         █  ⎛R  ⎞  █         █     ",
"█         █         █  ⎝  2⎠  █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗▔▔▔▖▝   ▘▗   ▄▟███▙▄  ",
"     █         █  ⎛R  ⎞  █         ███████████",
"     █         █  ⎝  1⎠  █         ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █        2█     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    assert( board.movesFrom(1, 1) == [0, 1, 2, 3, 4, 5, 6] )
    assert( board.movesFrom(2, 2) == [0, 2, 3, 4, 5] )

    assert( board.moveRobotAt_dir(1, 1, 1) == (1, 1) )
    assert( board.moveRobotAt_dir(2, 2, 3) == (2, 1) )

    board.reserveAt_dir(1, 1, 1)
    board.reserveAt_dir(2, 1, 6)

    assert( board.moveRobotAt_dir(1, 1, 1) == (1, 1) )
    assert( board.moveRobotAt_dir(2, 1, 6) == (2, 1) )

    board.cleanReservations()

    assert( board.moveRobotAt_dir(1, 1, 1) == (2, 2) )
    assert( board.moveRobotAt_dir(2, 1, 6) == (2, 1) )
