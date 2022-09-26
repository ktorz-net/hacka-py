# Play with HackaGames on Replit

[Replit](https://replit.com) is a kind off web-base IDE that allows developers to share and collaborate on the code edition.

After creating an account, create a replit (a replit working repertory) on python for instance and import **HackaGames** files.

**HackaGames** is only dependent on ZeroMQ library to permit multi-processes to communicate together.
In the shell:

```
pip install zmq
```

However, _replit_ will not allow us to work on _client-server_ mode, so only _local_ will be used on replit environment.

## Set up the main.py file:

First you have to configure the python environment to consider the game you  wanna play with (TicTacToe for instance).

```python
#!env python3
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], 'game-tictactoe'))
```

Then you can import a game engine and 2 players. In the example the game TicTacToe with a terminal IHM for a human player versus the first IA: 

```python
import gameEngine as gttt
from terminalIHM import TTTPlayer as Player1
from classicFirstAI import PlayerRandom as Player2
```

Then generate a new games and launch it in local mode with an array of players:

```python
game = gttt.GameTTT("classic")
game.local([Player1(), Player2()], 1)
```

That it. the final `main.py` file for TicTacToe will look-like:

```python
#!env python3
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], 'game-tictactoe'))

import gameEngine as gttt
from terminalIHM import TTTPlayer as Player1
from classicFirstAI import PlayerRandom as Player2

def main():
    game = gttt.GameTTT("classic")
    game.local([Player1(), Player2()], 1)

# script
if __name__ == '__main__':
    main()
```

Another example with _game-421_ and basic IHM player:

```python
#!env python3
#!env python3
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], 'game-421'))

import gameEngine as g421
from hackapy.player import PlayerIHM as Player

def main():
    game = g421.GameSolo()
    game.local([Player()], 1)

# script
if __name__ == '__main__':
    main()
```


## Edit your player:

In fact, the Player edition works the same in _replit_ or anywhere else, in _local_ mode or in default _client-server_ mode.
Therefore, refer to the games `README.md` file for more instructions...
The only thing you have to keep in mind is that the player must be imported and instantiated in `main.py` file, before to run the XP...
