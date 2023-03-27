# Q-Learning

**Q-Learning** is a quite simple first algorythm permiting an agent (a player in HackaGames) to optimize its curse of actions.
By continouslly acting in it environment (a game in HackaGame) the player improves its kwoledge about its interest of each state and each action re garding the reached situation.
We aim to implement this algorythm for learning to play to first **Py421** game then **Risky**.

## Prerequisite

This tutorial supose that you already permormed the **Initiation to AI - tutorials** and spécially the **Reinforcement Learning** tutorial. 
You already confident with the notion of _Learning Rate_ and _Exploration/Exloitation Trade-off_.

We will start from the `myPy421RLearner.py` to create our `myPy421QLearner.py`.

```sh
cp tutos/myPy421RLearner.py tutos/myPy421QLearner.py
```

However, we want to learn Q-values of the states instead of statistical rewards. 
So we have to change the attribute name `statreward` to `qvalues`, and modify your `launcher` to inport your new player and get a working envirnement ready.


## State definition

As for the `myPy421RLearner` player, the learning require a dictionnary built over state and action defined on string format, with for instance the following method:

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

The previous method permit to filter terminal state if the player decide to keep the all 3 dice.
In fact _Q-Value_ is a recursive evaluation of state that for it is important to clearlly identifiate terminal states in finit game.
In terminal state, the player will not be quered for a new decision and we expect that all terminal states will keep _Q-Value_ equals to _0_.

Adapt the player to include this proposed `stateStr` method.

## Update the Q value

Actually your _Q-Values_ update only compute the statistical reward for each tuple of states and actions and should lookalike: 

```python
self.qvalues[self.state][self.action]= self.qvalues[self.state][self.action]*(1-self.learningRate)
self.qvalues[self.state][self.action]+= self.reward*self.learningRate
```

It is time to implement the update of **Q** value for the last visited state
accordinglly to the _Q-Value_ equation (cf. [wikipedia](https://fr.wikipedia.org/wiki/Q-learning)).


### Test

We will consider that a certain number of games match an episode in the learning process.
$1000$  games for instance.
The goal is to play several episodes and observe increase in the *Q-values*.

You can also print the number of entrances in the dictionary, the average of the best values of states (the average over the states, by considering the best action to perform) etc...


## Test a more complicated games:


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
