# Play with HackaGames on Replit

[Replit](https://replit.com) is a kind off web-base IDE that allows developers to share and collaborate on the code edition.

After creating an account, create a replit (a replit working repository) on python for instance and clone **HackaGames** project.

In the 'shell' box:

```
git clone https://GuillaumeLozenguez@bitbucket.org/imt-mobisyst/hackagames.git
```

**HackaGames** is only dependent on ZeroMQ library to permit multi-processes to communicate together.
In the shell:

```
pip install zmq
```

However, _replit_ will not allow us to work on _client-server_ mode, so only _./local_ scripts will be used on replit environment.

## Try a game:

It is possible to execute python script in the Shell with the commands `python`...

```
python  hackagames/game-421/local
```

## Set up the main.py file:

From the `local` script of a game (`game-421/local` for instance).

```python
#!env python3
"""
HackaGame - Game - 421 
"""
import sys, os

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import gameEngine as g421
from hackapy.player import PlayerIHM as Player

def main():
    game= g421.GameSolo()
    game.local( [Player()], 1 )

# script
if __name__ == '__main__' :
    main()
```

Then configure correctly, the path  where to find the appropriate packages.
Concretely, change:

```python
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
```

to:

```python
sys.path.insert(1, os.path.join(sys.path[0], 'hackagames'))
sys.path.insert(1, os.path.join(sys.path[0], 'hackagames/game-421'))
```
