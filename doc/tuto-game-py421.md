# Py421, an HackaGames game

- Return to the [Table Of Content](toc.md)

**Py421** is a simple dice game where players try to optimize it dice combination after a maximum of 2 roll dice steps.

This tutorial is based only on **Python3**.

## Try the game:

The `start-interactive` script starts the game with an interactive interface in a shell.

```sh
python3 hackagames/gamePy421/start-interactive
```

The **421** is a tree dice game the player can roll several times to get a combination.
The player can perform one and only one action at it turns, and the game stops automatically after 2 turns.

The actions consist in keeping or rolling each of the 3 dices. So there are 8 actions:

- `keep-keep-keep`,  `keep-keep-roll`,  `keep-roll-keep`,  `keep-roll-roll`, `roll-keep-keep`,  `roll-keep-roll`,  `roll-roll-keep` and `roll-roll-roll`

The goal is to optimize the combination of dices before the end of the 2 turns.
The best combination ever is **421** for **800** points.
But you can explore other combinations.


## Let an AI play:

In python, the file `./gamePy421/firstAI.py` propose a first random AI with the required structure to play **421**.
The `firstAI` is configured to works as a client. So in two different terminals you have to start the game server then the `firstAI`.

```sh
# Into a first terminal
python3 ./hackagames/gamePy421/start-server
# Into a second terminal
python3 ./hackagames/gamePy421/player-firstAI
```

Here the goal is to get the maximal average score, and it is possible to configure the server to play more games with parameters `-n`:

```sh
# Into a first terminal
python3 ./hackagames/gamePy421/start-server -n 2000
# Into a second terminal
python3 ./hackagames/gamePy421/player-firstAI
```

The `firstAI` play randomly and get an average around $160$ points ($+/-5$).

## Configure your onw workspace:

Into your workspace, we encourage you to create a new directory for your experiences linked to our tutorials (`tutos` for instance, aside of `hackagames` directory),
and to create your **Py421** player in this directory.

```
mkdir tutos
touch tutos/myPy421Player.py
```

Well, you can finally edit and create your **Py421** player.
`myPy421AI.py` script must begin by importing hackagames elements (`hackapy`) and implement an `hackagames Abstract Player`.

To import `hackapy` you have first to modify the python path resource to add your workspace directory (i.e. the directory including tutos in wihich your AI in positionned).

```python
# Local HackaGame:
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

import hackagames.hackapy as hg
```

Then your first player will inherit from hackay Abstract player and look like :

```python
class AutonomousPlayer( hg.AbsPlayer ) :

    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        print( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        print( gameConf )
        self.actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll' ]

    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].attribute(1)
        self.dices= elements[1].attributes()
        print( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        action= random.choice( self.actions )
        print( f'Action: {action}' )
        return action
    
    def sleep(self, result):
        print( f'--- Results: {str(result)}' )
```

Finally, we have to seat a player at a game when the python script is executed:

```python
def main():
    print('let\'s go...')
    player= AutonomousPlayer()
    results= player.takeASeat()
    print( f"Average: { float(sum(results))/len(results) }" )
    #plotResults(results)

# script
if __name__ == '__main__' :
    main()
```

That it you can now test your AI (on 2000 games for instance): 

```sh
# Into a first terminal
python3 ./hackagames/gamePy421/start-server -n 2000
# Into a second terminal
python3 ./tutos/myPy421Player.py
```


## Local start:

However it is also possible to copy the `start-local` script aside of your AI to generate your local `test-421AI.py` script by skipping the client-server architecture.

aside to `hackagames` directory create your own launcher:

```sh
cp hackagamtest es/gamePy421/start-local test-421AI.py
```

Then modify the import instructions to have a clean python path and get your own AI.

```python
from hackagames.gamePy421.gameEngine import GameSolo as Game
from myPy421Player import AutonomousPlayer as Player
```

The final `test-421AI.py` should be :

```python
#!env python3
import sys
sys.path.insert( 1, __file__.split('tutos')[0] )

from hackagames.gamePy421.gameEngine import GameSolo as Game
from myPy421Player import AutonomousPlayer as Player

def main():
  game= Game()
  player1= Player()
  game.local( [player1], 1 )

# script
if __name__ == '__main__' :
    main()
```

That it, you can execute your script: `python3 ./tutos/test-421AI.py` which calls your player.
To notice that the second attribute in `local` method of `game` instance ($1$) represent the number of games the player will play.

## Let go:

To notice that method parameters are referencing `hackapy` objects we will present later.
The important element to see is that possible `actions` are listed once for all in wakeUp method.
Then perception records the game state in instance variables `horizon` (the number of remaining rerolls) and `dices` (a list of the 3 dices values).

The goal now is to propose heuristic choise of action in `decide` method regarding `self.horizon` and `self.dices` values.
The highest average score you can get the better is your heuristic AI.

