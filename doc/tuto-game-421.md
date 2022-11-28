# 421, an HackaGames game

- Return to the [Table Of Content](toc.md)

**421** is a simple dice game where players try to optimize it dice combination after a maximum of 2 roll dice steps.

This tutorial is based only on **Python3**.

## Try the game:

The `start-local` script starts the game with interactive interface in a shell.

```sh
python3 hackagames/game421/start-local
```

The **421** is a tree dice game the player can roll several times to get a combinaison.
The player can perform one and only one action at it turns, and the game stops automatically after 2 turns.

The actions consist in keeping or rolling each of the 3 dices. So there are 8 actions:

- `keep-keep-keep`,  `keep-keep-roll`,  `keep-roll-keep`,  `keep-roll-roll`, `roll-keep-keep`,  `roll-keep-roll`,  `roll-roll-keep` and `roll-roll-roll`

The goal is to optimize the combination of dices before the end of the 2 turns.
The best combination ever is **421** for **800** points.
But you can explore other combinations.


## Let an AI play:

In python, the file `./game421/firstAI.py` propose a first random AI with the required structure to play **421**.
The `firstAI` is configured to works as a client. So in tow diferent terminal you have to start the game server then the `firstAI`.

```sh
# Into a first terminal
python3 ./hackagames/game421/start-server
# Into a second terminal
python3 ./hackagames/game421/firstAI.py
```

Here the goal is to get the maximal average score, and it is possble to configure the server to play more games with parameter `-n`:

```sh
# Into a first terminal
python3 ./hackagames/game421/start-server -n 2000
# Into a second terminal
python3 ./hackagames/game421/firstAI.py
```

The `firstAI` play randomly and get an average around $160$ points ($+/-5$).

**Optional**

In local test, it is possible to modify the script `start-local` to include `firstIA`, modify the imported player to get the `firstAI` rather than the `PlayerIHM`.


## Configure your onw Workspace:

The simplest way is to start from `firstIA` to create out onw `AI`.
Into your workspace, we encourage you to create a new directory for your experiences linked to ours tutorials (`tutos` for instance, asinde of `hackagames` directory),
and to create your **421** player in this directory.

```
mkdir tutos
cp hackagames/game421/firstAI.py tutos/my421Player.py
```

You can already test the AI: 

```sh
# Into a first terminal
python3 ./hackagames/game421/start-server -n 2000
# Into a second terminal
python3 ./tutos/my421Player.py
```

However it is also possible to copy the `start-local` script to generate your local `test-421AI.py` script by skiping the client-server architecture.

aside to `hackagames` directory, create your own launcher:

```sh
cp hackagamtest es/game421/start-local test-421AI.py
```

Then modify the import instructions to get your own AI.

```python
from hackagames.game421.gameEngine import GameSolo as Game
from tutos.my421Player import AutonomousPlayer as Player
```

The final `test-421AI.py` should be :

```python
#!env python3
from hackagames.game421.gameEngine import GameSolo as Game
from tutos.my421Player import AutonomousPlayer as Player

def main():
  game= Game()
  player1= Player()
  game.local( [player1], 1 )

# script
if __name__ == '__main__' :
    main()
```

That it, you can execute your script: `python3 test-421AI.py` which call your player.
To notice that the second attribut in `local` method of `game` instance ($1$) represent the number of games the player will play.


## Your first AI:

Well, you can finally edit and modify the behavior of your **421** player.
`my421AI.py` script must begin by importing hackagames elements and implement an `hackagames Abstract Player`.
The intermediat functions `main` and `log` permit to connect a 421 server and rerouting the log to the standard output respectivelly.


```python
# Local HackaGame:
import hackagames.hackapy as hg

[...]

class AutonomousPlayer( hg.AbsPlayer ) :
```

An *HackaGames** player is composed by 4 main methods: `wakeUp`, `perceive`, `decide` and `sleep`.
The `waheUp` and the `sleep` methods are called respectivelly wen a game start and end, to differentiate a game to another.
The  `perceive` then `decide`methods are called at player turn turns to provide the informaton about the games state and ask for the player action.

The random 421 player in python looklike: 

```python
    # Player interface :
    def wakeUp(self, playerId, numberOfPlayers, gameConf):
        log( f'---\nwake-up player-{playerId} ({numberOfPlayers} players)')
        log( gameConf )
        self.actions= ['keep-keep-keep', 'keep-keep-roll', 'keep-roll-keep', 'keep-roll-roll',
            'roll-keep-keep', 'roll-keep-roll', 'roll-roll-keep', 'roll-roll-roll' ]

    def perceive(self, gameState):
        elements= gameState.children()
        self.horizon= elements[0].attribute(1)
        self.dices= elements[1].attributes()
        if len(elements) == 3 : # ie in duo mode
            self.reference= elements[2].attribute(1)
            log( f'H: {self.horizon} DICES: {self.dices} REF: {self.reference}' )
        else :
            log( f'H: {self.horizon} DICES: {self.dices}' )

    def decide(self):
        action= random.choice( self.actions )
        log( f'Action: {action}' )
        return action
    
    def sleep(self, result):
        log( f'--- Results: {str(result)}' )
```

To notice that methode parameters is referencing `hackalib` objects we will present later.
The important elements to see is that possible `actions` are listed once for all in wakeUp method.
Then perception record the game state in instance variables `horizon` the number of remainding rerolls and `dices` a list of the 3 dices values.

The goal now, is to propose heuristic choise of action in `decide` method regarding `self.horizon` and `self.dices` values.
The bigest average score you can get the better is your heuristic AI.