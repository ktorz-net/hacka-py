# Py421, an HackaGames game

**Py421** is a simple dice game where players try to optimize it dice combination after a maximum of 2 roll dice steps.

This tutorial is based only on **Python3**.

## Try the game:

The `start-interactive` script starts the game with an interactive interface in a shell.

```sh
python3 hackagames/gamePy421/start-interactive
```

**Py421** is a 3-dice game the player can roll several times to get a combination.
The player can perform one and only one action at it turns, and the game stops automatically after 2 turns.

The actions consist in keeping or rolling each of the 3 dices. So there are 8 actions:

- `keep-keep-keep`,  `keep-keep-roll`,  `keep-roll-keep`,  `keep-roll-roll`, `roll-keep-keep`,  `roll-keep-roll`,  `roll-roll-keep` and `roll-roll-roll`

The goal is to optimize the combination of dices before the end of the 2 turns.
The best combination ever is **4-2-1** for **800** points.
But you can explore other combinations.


## Initialize an Autonomous Player

Into your workspace, we encourage you to create a new directory for your experiences linked to our tutorials (`tutos` for instance, aside of `hackagames` directory),
and to create your new **Py421** player in this directory.

```
mkdir tutos
touch tutos/myPy421Player.py
```

You have now to edit `myPy421AI.py` script and create a **Py421** player.
The script must begin by importing hackagames elements (`hackapy`) and implement an `hackagames Abstract Player`.

To import `hackapy` you have first to modify the python path resource to add your workspace directory (i.e. the directory including tutos in which your AI in positioned).

```python
# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import hackagames.hackapy as hg
```

The first script we propose select a random action and also requires the adequate python tool:

```python
import random
```

Then your first player will inherit from hackay Abstract Player and and implement the `4` player methods `wakeUp`, `perceive`, `decide` and `sleep` required to play any Hackagames's game :

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

A first version of `myPy421AI.py` player could be a copy paste of the `hackagames/gamePy421/playerFirstAI`, 
and your final first script would be:

```python
# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import hackagames.hackapy as hg
import random

class AutonomousPlayer( hg.AbsPlayer ) :

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        print( f'---\nWake-up player-{playerId} ({numberOfPlayers} players)')
        print( gameConf )
    
    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].attribute(1)
        self.dices= elements[1].attributes()
        print( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll' ]
        action= random.choice( actions )
        print( f'Action: {action}' )
        return action
    
    def sleep(self, result):
        print( f'--- Results: {str(result)}' )
```

## Test your Player

_HackaGames_ is designed to work as a client-server architecture to make the game and the player completlly independant.
However, it is also possible start a python game in a test mode for a player in a single process with a simple script.
Aside to `hackagames` and your `tutos` directories create your own launcher:

```sh
touch launcherPy421.py
```

Edit the python script.
The code require to import the game and the player, 
then to instanciate them and to start `testPlayer` method:

```python
#!env python3
from hackagames.gamePy421.gameEngine import GameSolo as Game
from tutos.myPy421Player import AutonomousPlayer as Player

# Instanciate and start 100 games
game= Game()
player= Player()
results= game.testPlayer( player, 100 )
```

That it, you can execute your script: `python3 ./tutos/launcherPy421.py` which calls your player.
The second attribute in `testPlayer` method of `game` instance (`100` here) is the number of games the players will play before the process end.

The `game.testPlayer` method return the list game results.
We can now print and annalyse the reached results (compute the average score for instance): 

```python
# Annalisis
average= sum(results)/len(results)
print( f"Average score: {average}")
```

## Understand the first player

It is extected that an HackaGames Player would be informed at game start and game end events.
It is the purpose of methods `wakeUp` and `sleep`. 
The `wakeUp` method also provides the configuration of the game if require (so, nothing particular in `Py421`).
The `sleep` method provides the final result for the player.
In most of the games, it is a `-1`, `1` or `0` value, if the player lose, win or if there is a no winner.
In the solo version of `Py421`, it is a score to optimize.

The method `perceive` and `decide` are activated at turn during the game.
There inform the player about the evolution of the player hand (the 3 dice and the number of reminder re-roll steps)
and request him for the next action to perform. 


## A minimal Autonomous Player:

To notice that method parameters are referencing `hackapy` objects we will present later.
The perception already records the game variables `horizon` (the number of remaining roll-again) and `dices` (a list of the 3 dices values) into instance attributes.

Actually in `decide` method, an action is choosen randomly, the goal now is to propose heuristic choice of actions to optimize average score over `10000` games.
As a minimal start, it is possible to force a stop action (action `keep-keep-keep`) each time the player reach a good combinaison (`4-2-1` or `1-1-1` for instance).

- Return to the [Table Of Content](toc.md)

