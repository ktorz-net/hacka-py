# TicTacToe, an HackaGames game

**TicTacToe** is simple two-player games where each player tries to align trees of their pieces.

It comes in two modes: _classic_ and _ultimate_.

## Try the game:

The `start-interactive` script starts the game in _classic_ mode with an interactive interface in a shell playing against an artificial player `playerFirstAI.py`.

The player can perform one and only one action at it turn, and the game stops automatically with a winner or when no more pieces can be set on the tabletop.

The actions consist in positionning a player's piece on the grid with the form: `coordinateLetter-coordinateNumber`. Their are 3 times 3 actions in _classic_ mode: `A-1`, `A-2`, `A-3`, `B-1`, `B-2`, `B-3`, `C-1`, `C-2` and `C-3`.

Exemple of grid at some point: 

```
x: A B C
1  x    
2    o  
3  o   x
```

The first player aligning 3 of its pieces win the game.

The _ultimate_ mode is a hierarchical 2-levels **TicTacToe**.
the grid is composed off 9 times 9 cells, so potentially 9 times 9 actions for the players: `A-1`, `A-2`, ... , `A-9`, `B-1`, ... , `I-9.
In practice, most of the time, only a sub-number of actions are available.
The particularity in hierarchical **TicTacToe** is that, the took position by a player in the _classic_ grid indicates the next grid to play for the next player turn.

The players have to win 3 aligned _classic_ grids to win an _ultimate_ **TicTacToe**.

Exemple of grid at some point: 

```
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
actions: D:F-7:9
```

The line `actions: D:F-7:9` indicate that it is possible to play in any free possition between `D` and `F` and `7` and `9`, so : `D-7`, `D-8`, `D-9`, `E-7`, `E-9`, `F-7`, `F-8` or `F-9`.
At the begining of the game it is possible to play in a corner grid, a side grid or the center grid. That for the action line indicate: `actions: A:C-1:3, A:C-4:6, D:F-4:6`





---------






**TicTacToe** is a standard **HackaGames** game, and it works with a client-server architecture.
The server is the game, the clients are the players.

First start the game server (from **HackaGames** repository) :

```sh
./gameTictactoe/start.py
```

This starts **TicTacToe** in classic mode for 2 games. Each player will take turns at starting. To start in ultimate mode with a different number of games: `./gameTictactoe/start.py ultimate -n 100`

Then, in a new terminal start the a **HackaGames** terminal player dedicated to **TicTacToe** (the basic **HackaGames** terminal player `./play.py` will work but with a less fancy interface):

```sh
./gameTictactoe/play.py
```


## Let an AI play:

The file `./gameTictactoe/firstAI.py` propose a first random-safe AI with the required structure to play **TicTacToe**.
The **firstAI** will win if possible, prevent the oponent to win if possible or play in a random manner.

to test the player, start the server and 2 players in 3 different terminals:

```sh
./gameTictactoe/start.py
```

then :
```sh
./gameTictactoe/firstAI.py
```

You have to launch `firstAI.py` 2 times or with `play.py` if you wana fight the AI.

To notice that, you can increase the numbers of games with the `-n` attribute:

```sh
./gameTictactoe/start.py -n 1000
```

### Your first AI:

In a directory dedicated to your work, you start an Ia from the proposed random player:

```bash
mkdir draft
cp gameTictactoe/firstAI.py draft/myTictactoeAI.py
```

If it is your first time with **HackaGames** AI, try the **421** game first.

The goal is to generate an AI beating the `firstAI.py` in _classic_ mode, then in _ultimate_ mode.
