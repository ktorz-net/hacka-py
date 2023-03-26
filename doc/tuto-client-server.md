# Client-Server architecture:

**Work-In-Progress**

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





...


In python, the file `./gamePy421/playerFirstAI.py` propose a first random AI with the required structure to play **Py421**.
The `playerFirstAI` is configured to works as a client. So in two different terminals you have to start the game server then the `firstAI`.

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






## Risky

As for all `hackagames`, it is possible to separate the game-engine and the players by using a client/server architecture.

First start a risky game server in a first terminal then tow players into tow different terminals.

```sh
# Into a first terminal
python3 hackagames/gameRisky/start-server
# Into a second terminal
./hackagames/gameRisky/player-firstAI
# Into a third terminal
python3 ./hackagames/gameRisky/player-firstAI
```

The risky server (`start-server [board-name] [-n NNN]`) can be configured with a different board and the option `-n` set the number of game for the enconter. 
Actually, only their is only `board-4` and `board-10` for the board-name.
For instance for a serie of 100 games on `board-10`:

```sh
# Into a first terminal
./hackagames/gameRisky/start-server board-10 -n 100
```

To notice that it is still possible to seat to the game with the shell interface.

```sh
# Into anotherterminal
python3 hackagames/gameRisky/player-interactive
```















## Let an AI play:

In python, the file `./gamePy421/playerFirstAI.py` propose a first random AI with the required structure to play **Py421**.
The `playerFirstAI` is configured to works as a client. So in two different terminals you have to start the game server then the `firstAI`.

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












