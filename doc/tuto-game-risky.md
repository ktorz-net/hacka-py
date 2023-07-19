# Risky, an HackaGames Game

**Risky** is a strategic turn-based game where two armies (or more) fights for a territory.

## Try the game:

The `start-interactive` script starts the game with an interactive interface in a shell playing against an artificial player `playerFirstAI.py`.

```sh
python3 hackagames/gameRisky/start-interactive
```

The world is composed by interconnected nodes forming a tabletop as, for instance:

```
       .' '.
      |     |
       '. .3
      /     \
 .' '.       .' '.
|     |-----|     |
 '. .1       '. .2 
      \     /
       .' '.
      |     |
       '. .4
```

The 2 players are referenced as a player _A_ and player _B_ ; starting respectively in positions 1 and 2.
When an army is on a node, the information is presented as below:

```
 .'A'.    # Player ID
|1- 12|   # army action and force
 '. .4    # node ID
```

In this example, an army of player _A_ is on node `4`. The army has `1` action-point and is composed by `12` soldiers. 

Each army has 2 main attributes:

- its action counter (the number of action it can perform - max 2)
- its force (the size of the army - max 24)

At its turn the player can make several actions (in the limit of action counters):

- Moving: `move X Y FORCE` to move `FORCE` units from cell `X` to cell `Y`
- Growing: `grow X` to grow the army on nodes `X`. The increase of the army is depending on the initial army size and the connections to occupied friend nodes.
- Sleeping: `sleep` to increase the action counter by one for all the armies.

To notice that a moving action that will move an army toward an adversarial node trigger a fight.
Iteratively, each force point of the attack and the defense has a chance to deal one damage.
Defenses have an increased chance than attack.
However if the attack is greater than the defense than each extra point count double.
The fight is running until one of the army is destroyed.

For instance, with a `move 1 2 10` with a defense of `8` on the node `2`, the fight will start by considering an attack force of `12` ($2\times 10-8$) times 1 chance over 2 against a defense of `8` times 2 chances over 3.
The exact amount of damages at the end of the fight remains uncertain.


## Initialize an Autonomous Player

Into your workspace, we encourage you to create a new directory for your experiences linked to our tutorials (`tutos` for instance, aside of `hackagames` directory),
and to create your new **Risky** player in this directory.

```
mkdir tutos
touch tutos/myRiskyPlayer.py
```

You now have to edit `myRiskyPlayer.py` script and create a **Risky** player.
The script must begin by importing hackagames elements (`hackapy` and the `Risky` `gameEngine`) and implement an `hackagames Abstract Player`.

To import `hackapy` and the `gameEngine` you have first to modify the python path resource to add your workspace directory (i.e. the directory including tutos in which your AI in positioned).

```python
# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import hackagames.hackapy as hg
import hackagames.gameRisky.gameEngine as game
```

The first script we propose selects a random action and also requires the adequate python tool:

```python
import random
```

Then your first player will inherit from hackay Abstract Player and implement the `4` player methods `wakeUp`, `perceive`, `decide` and `sleep` required to play any Hackagames's game :

```python
class AutonomousPlayer( hg.AbsPlayer ) :

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        [...]

    def perceive(self, gameState):
        [...]
    
    def decide(self):
        [...]
    
    def sleep(self, result):
        [...]
```

A first version of `myRiskyPlayer.py` player could be a copy-paste of the `hackagames/gameRisky/playerFirstAI`, 
and your final first script would be:

```python
# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import hackagames.hackapy as hg
import hackagames.gameRisky.gameEngine as game
import random

class AutonomousPlayer(hg.AbsPlayer) :
    
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{iPlayer} ({numberOfPlayers} players)')
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky().fromPod( gameConf )
        self.viewer= game.ViewerTerminal( self.game )

    def perceive(self, gameState):
        self.game.fromPod( gameState )
        self.viewer.print( self.playerId )
    
    def decide(self):
        actions= self.game.searchActions( self.playerId )
        action= random.choice( actions )
        if action[0] == 'move':
            action[3]= random.randint(1, action[3])
        action= ' '.join( [ str(x) for x in action ] )
        print( "Do: "+ action )
        return action
    
    def sleep(self, result):
        print( f'---\ngame end\nresult: {result}')
```

Here the gameEngine permit the player to instantiate a copy `self.game` of the game at the reached configuration.
It is first used to search for available actions in `decide` method and to get one at random.


## Test your Player

_HackaGames_ is designed to work as a client-server architecture to make the game and the player completely independent.
However, it is also possible start a python game in a test mode for a player in a single process with a simple script.
Aside to `hackagames` and your `tutos` directories create your own launcher:

```sh
touch launcherRisky.py
```

Edit the python script.
The code requires to import the game and the player and an opponent to your player.
then to instantiate them and to start `testPlayer` method:

```python
#!env python3
from hackagames.gameRisky.gameEngine import GameRisky
from hackagames.gameRisky.playerFirstAI import AutonomousPlayer as Opponent
from tutos.myRiskyPlayer import AutonomousPlayer as Player

# Instanciate and start 1 games
game= GameRisky( 2, "board-4" )
player= Player()
opponent1= Opponent()
results= game.testPlayer( player, 100, [opponent1] )

print(results)
```

That it, you can execute your script: `python3 ./launcherRisky.py` which calls your player.
The second attribute in `testPlayer` method of `game` instance (`100` here) is the number of games the players will play before the process end.

The `game.testPlayer` method return the list game results.
We can now print and analyze the reached results (compute the average score for instance): 

```python
# Analysis
average= sum(results)/len(results)
print( f"Average score: {average}")
```

The result should be very close to zero. It is the same AI...


## Customaize your AI: 

To customize your AI you can use the game engine copy (cf. [risky.py](../gameRisky/gameEngine/risky.py))

Somme of the available methods:

```python
def update( self, board ): # Update the board from the perception.

def searchActions(self, playerId): # List all the current possible actions from the configuration of the armies

def cellIds(self): # return the list of cell identifiers

def edgesFrom(self, iCell): # return the list of connected cell identifiers from the iCell cell.
     
def armyOn(self, iCell) : # return an army as a Pod object, if an army is on the iCell cell (and False otherwise).

def playerLetter(self, iPlayer): # return the player letter (A, B, C ...) of the ith player (1, 2, ...)
```

An army is a `Pod` object where the owner is recorded in the status and the 2 attributes is for action counter and force :

```python
for iCell in self.game.cellIds() :
    army= self.game.armyOn(iCell) # The army on the cell 1
    if army :
        owner= army.status()
        action= army.flag(1)
        force= army.flag(2)
        print( f"Army-{owner} ({action}, {force}) on {iCells}" )
```

The goal now is to compute that information in order to propose an AI winning the PlayerFirstAI.

## Confront your AI:

In the launcher script, you can replace the imported `opponent` AI to an interactive interface.

```python
from hackagames.gameRisky.gameEngine.players import PlayerShell as Opponent
```
