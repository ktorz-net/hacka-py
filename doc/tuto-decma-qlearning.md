# Q-Learning

**Q-Learning** is quite a simple first algorithm permitting an agent (a player in HackaGames) to optimize its curse of actions.
By continually acting in it environment (a game in HackaGame) the player improves its knowledge about its interest of each state and each action regarding the reached situation.
We aim to implement this algorithm for learning to play to first **Py421** game then **Risky**.

## Prerequisite

This tutorial suppose that you already performed the **Initiation to AI - tutorials** and specially the **Reinforcement Learning** tutorial. 
You already confident with the notion of _Learning Rate_ and _Exploration/Exploitation Trade-off_.

We will start from the `myPy421RLearner.py` to create our `myPy421QLearner.py`.

```sh
cp tutos/myPy421RLearner.py tutos/myPy421QLearner.py
```

However, we want to learn Q-values of the states instead of statistical rewards. 
So we have to change the attribute name `statreward` to `qvalues`, and modify your `launcher` to import your new player and get a working environment ready.


## State definition

As for the `myPy421RLearner` player, the learning requires a dictionary built over state and action defined on a string format, with for instance the following method:

```python
# State Machine :
def stateStr(self):
    if self.action == 'keep-keep-keep' :
        self.horizon= 0 # If we already keep all dice the game is ended
    state= str(self.horizon)
    for d in self.dices :
        state += '-' + str(d)
    return state
```

The previous method permit to filter terminal state if the player decides to keep all the 3 dice.
In fact _Q-Value_ is a recursive evaluation of state that for it is important to clearly determine terminal states in finite game.
In terminal state, the player will not be queried for a new decision and we expect that all terminal states will keep _Q-Value_ equals to _0_.

Adapt the player to include this proposed `stateStr` method.

## Update the Q value

Actually, your _Q-Values_ update only compute the statistical reward for each tuple of states and actions and should lookalike: 

```python
self.qvalues[self.state][self.action]= self.qvalues[self.state][self.action]*(1-self.learningRate)
self.qvalues[self.state][self.action]+= self.reward*self.learningRate
```

It is time to implement the update of **Q** value for the last visited state
accordingly to the _Q-Value_ equation (cf. [wikipedia](https://fr.wikipedia.org/wiki/Q-learning)).


### Test

We will consider that a certain number of games match an episode in the learning process.
$1000$  games for instance.
The goal is to play several episodes and observe increase in the *Q-values*.

You can also print the number of entrances in the dictionary, the average of the best values of states (the average over the states, by considering the best action to perform) etc...


## Test a more complicated games:

Let’s apply Q-Learning to Risky game.
Risky suffer from a double complexity, both the number of states and the number of actions are exponential on the size of the board.
Potentially, there are as many armies as the number of cells, and each army can have different forces size and action points.
There are as many possible move actions as the number of edges, and each move action can be parametrized with different force sizes. 
The potential number of entrances in the resulting QValue function prevents for a basic usage of this algorithm.

A simple heuristic approach consists in designed meta-actions and meta-states (a smallest number of states and actions with a more abstract level) to apply Q-Learning on a higher level of abstraction.
In fact, **Risky** already propose a set of 3 meta-actions:

1. `fight X` - where `X` is a reachable opponent’s position. This action will send the biggest attackant army it can find.
2. `expend X` - where `X` is a expendable player position, position with free neighbors. This action will send a egal force army on each reachable free position from `X`.
3. `defend`. This action grows all available armies before to sleep.

This way, the number of possible actions at each turn is considerably smallest (but also more restricted). A simple AI based on a random selection of Meta-Action would lookalike:

```python
class PlayerMetaRandom(hg.AbsPlayer) :
    # Player interface :
    def wakeUp(self, iPlayer, numberOfPlayers, gameConf):
        self.playerId= chr( ord("A")+iPlayer-1 )
        self.game= game.GameRisky()
        self.game.update(gameConf)

    def perceive(self, gameState):
        self.game.update( gameState )
        
    def decide(self):
        actions= self.game.searchMetaActions( self.playerId )
        action= random.choice( actions )
        action= ' '.join( [ str(x) for x in action ] )
        return action
```

Starting from this `PlayerMetaRandom`, the goal is to apply Q-Learning on a new `tutos/myRiskyQLearner.py`.

1. Propose a `stateStr` method returning string destription of the game configuration.
2. Initialize `qvalues` dictionary, and update its values after each transition.
3. Use the `qvalues` to choose a 'good' action to perform.


<!--

## Going further:

Do not forget 
You ~~can~~ must test your code at each development step by executing the code for few games and validate that the output is as expected.

Update our PlayerQ:

1. *PlayerQ* constructor permits users to customize the algorithms parameters $\epsilon$, $\gamma$ ... Let’s do it in the `__init__` method with default parameters value.
   - Handle default parameters value in python with [w3schools](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp).
2. *PlayerQ* save its learned **Q-values** on a file. To notice that with [json module](https://docs.python.org/fr/3/library/json.html), you can easily read and write a dictionary from a file.
3. *PlayerQ* initialize its **Q-values** by loading a file.
4. A new *PlayerBestQ* simply play the best action always from a given **Q-values** dictionary (without upgrading **Q**).
5. You are capable of plotting the sum over **Q** with one point per episode (with [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) for instance).

-->
