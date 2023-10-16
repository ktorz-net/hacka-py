"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def test_Robot():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(2, 1).setObstacle()
    assert( board.setRobot_at( ge.Robot(12), 1, 1) == True )
    assert( board.setRobot_at( ge.Robot(1), 1, 1) == False )
    assert( board.setRobot_at( ge.Robot(1), 2, 1) == False )

    #print( board.shell() )
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
    assert( board.setRobot_at( r8, 3, 2) == True )

    #print( board.shell() )
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

    #print( board.shell() )
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
    board.setRobot_at(ge.Robot(1), 1, 1)
    
    #print( board.shell() )
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
    assert( board.moveRobotAt_dir(1, 1, 4) == [1, 0] )
    assert( board.at(1, 0).robot().dommage() == 0 )
    assert( board.movesFrom(1, 0) == [0, 1, 2, 5, 6] )
    assert( board.moveRobotAt_dir(1, 0, 5) == [0, 0] )
    assert( board.at(0, 0).robot().dommage() == 0 )
    assert( board.movesFrom(0, 0) == [0, 1, 2] )

    #print( board.shell() )
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

    assert( board.moveRobotAt_dir(0, 0, 0) == [0, 0] )
    assert( board.moveRobotAt_dir(0, 0, 5) == False )
    assert( board.at(0, 0).robot().dommage() == 1 )
    assert( board.moveRobotAt_dir(1, 1, 5) == False )

    robot= board.at(0, 0).removeRobot()
    board.setRobot_at(robot, 3, 2)

    #print( board.shell() )
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
    board.setRobot_at( ge.Robot(1), 1, 1 )
    board.setRobot_at( ge.Robot(2), 2, 2 )
    board.at(2, 2).robot().setGoal(3, 0)
    
    #print( board.shell() )
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

    assert( board.moveRobotAt_dir(1, 1, 1) == False )
    assert( board.at(1, 1).robot().dommage() == 1 )
    assert( board.moveRobotAt_dir(2, 2, 3) == [2, 1] )
    assert( board.at(2, 1).robot().dommage() == 0 )

    board.reserveAt_dir(1, 1, 1)
    board.reserveAt_dir(2, 1, 6)

    assert( board.moveRobotAt_dir(1, 1, 1) == False )
    assert( board.at(1, 1).robot().dommage() == 2 )
    assert( board.moveRobotAt_dir(2, 1, 6) == False )
    assert( board.at(2, 1).robot().dommage() == 1 )

    board.cleanReservations()

    assert( board.moveRobotAt_dir(1, 1, 1) == [2, 2] )
    assert( board.moveRobotAt_dir(2, 1, 6) == False )

    
    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗       ",
"█         █         █  ⎛R  ⎞  █         █     ",
"█         █         █  ⎝  1⎠  █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝▁▁▁▘▗   ▄▟███▙▄  ",
"     █         █         █  ⎛R  ⎞  ███████████",
"     █         █         █  ⎝  2⎠  ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █        2█     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )
    
    board.multiMove( [[2, 2, 4], [2, 1, 1]] )

    #print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  2⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄  ",
"     █         █  ⎛R  ⎞  █         ███████████",
"     █         █  ⎝  1⎠  █         ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █        2█     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    board.multiMove( [[1, 1, 1], [3, 2, 5]] )

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  2⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▖▝   ▘▗▔▔▔▄▟███▙▄  ",
"     █         █  ⎛R  ⎞  █         ███████████",
"     █         █  ⎝  1⎠  █         ███████████",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▘▗   ▖▝   ▀▜███▛▀  ",
"█         █         █         █         █     ",
"█        1█         █         █        2█     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

def test_error():
    board= ge.Hexaboard(4, 3)
    assert( type( board ) is ge.Hexaboard  )
    assert( board.size() == (4, 3) )

    board.at(3, 1).setObstacle()
    r1= ge.Robot(1)
    board.setRobot_at(r1, 1, 1)
    
    #print( board.shell() )
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
    
    r1.setError(0.2)
    reach= {}
    for i in range(10000) :
        x, y= r1.position()
        board.teleportRobot(x, y, 1, 1)
        coord= board.moveRobotAt_dir(1, 1, 4)
        coord= coord[0]*100+coord[1]
        if coord not in reach :
            reach[coord]= 0
        reach[coord]+= 1
    
    print(reach)
    assert( len(reach) == 7 )
    for g in reach :
        if g == 100 :
            assert( round(reach[g]/10000, 1) == 0.8 )
        else :
            assert( 240 < reach[g] and reach[g] < 340 )
