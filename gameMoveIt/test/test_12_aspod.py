"""
Test - MoveIt Games Class
"""
import sys

sys.path.insert( 1, __file__.split('gameMoveIt')[0] )
import hackapy as hg
import gameMoveIt.gameEngine as ge

def test_robotAsPod():
    board= ge.Hexaboard(4, 3)
    board.at(2, 1).setObstacle()

    board.setRobot_at( ge.Robot(1), 1, 1)
    board.setRobot_at( ge.Robot(2), 3, 2)
    board.at( 3, 2 ).robot().setGoal(1,1)

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  2⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄▔▔▔▖▝   ▘▗  ",
"     █         █ ⎡⎛R  ⎞⎤ ███████████         █",
"     █         █ ⎣⎝  1⎠⎦2███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█ ⎡     ⎤ █         █         █         █     ",
"█ ⎣     ⎦1█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )
    
    assert( str(board.at( 1, 1 ).robot().asPod()) == "Robot: 1 [1, 1, 0, 0, 0]" )
    assert( str(board.at( 3, 2 ).robot().asPod()) == "Robot: 2 [3, 2, 1, 1, 0]" )

    assert( str(board.at( 3, 2 ).robot().asPod()) == "Robot: 2 [3, 2, 1, 1, 0]" )

def test_RobotFromPod():
    r12= ge.Robot(12, 3, 4)
    r12.setGoal(2, 7)

    assert( str(r12) == "Robot-12[on(3, 4), goal(2, 7)-False, error(0.0)]" )
    assert( str(r12.asPod()) == "Robot: 12 [3, 4, 2, 7, 0]" )
    r12.fromPod( hg.Pod( "Robot", "21", [1, 9, 5, 8, 1] ) )
    assert( str(r12.asPod()) == "Robot: 21 [1, 9, 5, 8, 1]" )

    r12.setError(0.1)
    assert( str(r12) == "Robot-21[on(1, 9), goal(5, 8)-True, error(0.1)]" )
    r12.fromPod( hg.Pod( "Robot", "12", [3, 4, 2, 7, 0] ) )
    assert( str(r12) == "Robot-12[on(3, 4), goal(2, 7)-False, error(0.1)]" )

def test_boardAsPod():
    board= ge.Hexaboard(4, 3)
    board.at(2, 1).setObstacle()

    board.setRobot_at( ge.Robot(1), 1, 1)
    board.setRobot_at( ge.Robot(2), 3, 2)
    board.at( 3, 2 ).robot().setGoal(1, 1)

    print( board.shell() )
    test= [
"     ▁         ▁         ▁         ▁          ",
"  ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗       ",
"█         █         █         █  ⎛R  ⎞  █     ",
"█         █         █         █  ⎝  2⎠  █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝▁▁▁▘▗   ▄▟███▙▄▔▔▔▖▝   ▘▗  ",
"     █         █ ⎡⎛R  ⎞⎤ ███████████         █",
"     █         █ ⎣⎝  1⎠⎦2███████████         █",
"  ▖▝   ▘▗   ▖▝   ▘▗▔▔▔▖▝   ▀▜███▛▀   ▘▗   ▖▝  ",
"█ ⎡     ⎤ █         █         █         █     ",
"█ ⎣     ⎦1█         █         █         █     ",
"  ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝   ▘▗   ▖▝       ",
"     ▔         ▔         ▔         ▔          "]
    
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )

    print( board.asPod() )
    test= [
"Board: [4, 3]",
"- Line:",
"  - Cell: FREE",
"  - Cell: FREE",
"  - Cell: FREE",
"  - Cell: FREE",
"- Line:",
"  - Cell: FREE",
"  - Cell: FREE",
"  - Cell: OBSTACLE",
"  - Cell: FREE",
"- Line:",
"  - Cell: FREE",
"  - Cell: FREE",
"  - Cell: FREE",
"  - Cell: FREE" ]

    for l1, l2 in zip( str(board.asPod()).split("\n"), test ) :
        assert( l1 == l2 )


def test_boardFromPod():
    board= ge.Hexaboard()

    pod= hg.Pod( "Board", "", [3, 2] )
    podLine= hg.Pod( "Line" )
    podLine.append( hg.Pod( "Cell", "FREE" ) )
    podLine.append( hg.Pod( "Cell", "OBSTACLE" ) )
    podLine.append( hg.Pod( "Cell", "FREE" ) )
    pod.append(podLine)
    podLine= hg.Pod( "Line" )
    podLine.append( hg.Pod( "Cell", "FREE" ) )
    podLine.append( hg.Pod( "Cell", "FREE" ) )
    podLine.append( hg.Pod( "Cell", "OBSTACLE" ) )
    pod.append(podLine)

    board.fromPod( pod )

    print( board.shell() )
    test= [
"          ▁         ▁         ▁     ",
"       ▖▝   ▘▗   ▖▝   ▘▗   ▄▟███▙▄  ",
"     █         █         ███████████",
"     █         █         ███████████",
"  ▖▝   ▘▗   ▄▟███▙▄   ▖▝   ▀▜███▛▀  ",
"█         ███████████         █     ",
"█         ███████████         █     ",
"  ▘▗   ▖▝   ▀▜███▛▀   ▘▗   ▖▝       ",
"     ▔         ▔         ▔          "]
    
    for l1, l2 in zip( board.shell().split("\n"), test ) :
        assert( l1 == l2 )
