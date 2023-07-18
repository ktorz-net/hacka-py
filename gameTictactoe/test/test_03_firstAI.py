# Local HackaGame:
import sys

sys.path.insert(1, __file__.split('gameTictactoe')[0])
from gameTictactoe.gameEngine import GameTTT
from gameTictactoe.playerFirstAI import AutonomousPlayer as Player
#from gameTictactoe.playerUltimateFirstAI import PlayerRandom as PlayerU

# ------------------------------------------------------------------------ #
#                   T E S T   T I C T A C T O E    G A M E
# ------------------------------------------------------------------------ #


#------------------------------------------------------------------------------------------------
# Test Player Classic
#------------------------
def test_risky_playerClassic():
  game= GameTTT()
  pod= game.initialize()
  player= Player()
  assert "\n"+ str(player)  == """
 :
actions: """

  player.wakeUp(1, 2, pod)
  print( player )
  assert "\n"+ str(player)  == """
x: A B C
1       
2       
3       
actions: A:C-1:3"""

  player.perceive( game.playerHand(1) )
  assert "\n"+ str(player)  == """
x: A B C
1       
2       
3       
actions: A:C-1:3"""

  game.applyPlayerAction(1, "A-1")
  player.perceive( game.playerHand(1) )
  assert "\n"+ str(player)  == """
x: A B C
1  x    
2       
3       
actions: A:C-1:3"""

  game.applyPlayerAction(2, "B-3")
  game.applyPlayerAction(1, "C-2")
  player.perceive( game.playerHand(1) )
  assert "\n"+ str(player)  == """
x: A B C
1  x    
2      x
3    o  
actions: A:C-1:3"""


#------------------------------------------------------------------------------------------------
# Test action Classic
#------------------------------------------------------------------------------------------------
def test_risky_playerClassic():
  game= GameTTT()
  pod= game.initialize()
  player= Player()
  player.wakeUp(1, 2, pod)
  player.perceive( game.playerHand(1) )

  print( player )
  assert "\n"+ str(player)  == """
x: A B C
1       
2       
3       
actions: A:C-1:3"""

  assert player.listActions() == ['A-1', 'A-2', 'A-3', 'B-1', 'B-2', 'B-3', 'C-1', 'C-2', 'C-3']

  game.applyPlayerAction(1, "A-1")
  game.applyPlayerAction(2, "B-3")
  game.applyPlayerAction(1, "C-2")
  player.perceive( game.playerHand(1) )
  assert "\n"+ str(player)  == """
x: A B C
1  x    
2      x
3    o  
actions: A:C-1:3"""

  assert player.listActions() == ['A-2', 'A-3', 'B-1', 'B-2', 'C-1', 'C-3']

#------------------------------------------------------------------------------------------------
# Test Play Classic
#------------------------------------------------------------------------------------------------
def test_risky_playClassic():
  game= GameTTT()
  player1= Player()
  player2= Player()
  game.local( [player1, player2], 1 )

#------------------------------------------------------------------------------------------------
# Test Player Ultimate
#------------------------------------------------------------------------------------------------
def test_risky_playerUlitimate():
  game= GameTTT("ultimate")
  pod= game.initialize()
  player= Player()
  player.wakeUp(1, 2, pod)
  player.perceive( game.playerHand(1) )

  assert "\n"+ str(player)  == """
x: A B C   D E F   G H I
1        |       |      
2        |       |      
3        |       |      
  -------|-------|-------
4        |       |      
5        |       |      
6        |       |      
  -------|-------|-------
7        |       |      
8        |       |      
9        |       |      
actions: A:C-1:3, A:C-4:6, D:F-4:6"""

  assert player.listActions() == [
    'A-1', 'A-2', 'A-3', 'B-1', 'B-2', 'B-3', 'C-1', 'C-2', 'C-3',
    'A-4', 'A-5', 'A-6', 'B-4', 'B-5', 'B-6', 'C-4', 'C-5', 'C-6',
    'D-4', 'D-5', 'D-6', 'E-4', 'E-5', 'E-6', 'F-4', 'F-5', 'F-6'
  ]

  game.applyPlayerAction(1, "A-1")
  game.applyPlayerAction(2, "B-3")
  game.applyPlayerAction(1, "E-8")
  game.applyPlayerAction(2, "E-6")

  player.perceive( game.playerHand(1) )

  print( player )

  assert "\n"+ str(player)  == """
x: A B C   D E F   G H I
1  x     |       |      
2        |       |      
3    o   |       |      
  -------|-------|-------
4        |       |      
5        |       |      
6        |   o   |      
  -------|-------|-------
7        |       |      
8        |   x   |      
9        |       |      
actions: D:F-7:9"""

  assert player.listActions() == ['D-7', 'D-8', 'D-9', 'E-7', 'E-9', 'F-7', 'F-8', 'F-9']

#------------------------------------------------------------------------------------------------
# Test Play Ultimate
#------------------------------------------------------------------------------------------------
def test_risky_playUltimate():
  game= GameTTT("ultimate")
  player1= Player()
  player2= Player()
  game.local( [player1, player2], 1 )
