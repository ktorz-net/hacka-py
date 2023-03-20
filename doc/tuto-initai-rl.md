# Reinforcement Learning

- Return to the [Table Of Content](toc.md)

Reinforcement Learning is a family of approaches and algorithms that enhance an autonomous system (an agent) to learn from it successful tries and failures [Cf. [Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning)].
Technically, at the beginning, the agent is capable of acting in it environment (with default pure random action for instance) 
and by acting it gets feedback and will be capable of evaluating the interest of actions in a given context.

So the goal is to implement a new _myPy421RLearner.py_ player learning from its reached rewards.
Starting from a pure random player (cf. [Py421 tutorial](./tuto-game-py421.md)),
the first step is to implement a reward function that state for the value of a transition. 
A transition consists on switching from a state (the previous one) to a new one by doing a given action.

## Reward in Py421

In mono-player **Py421**, the reward is equal to the difference between the value of the old conbinaison and the new one.
In the `perception` method, it consists in read lhe new value and store it in a instance attribute and to compare it to the last on :

```python
def perceive(self, gameState):
    # get elements
    elements= gameState.children()
    self.horizon= elements[0].attribute(1)
    self.dices= elements[1].attributes()
    # compute reward
    lastValue= self.value
    self.value= elements[2].value(1)
    self.reward= value - self.lastValue
    print( f'H: {self.horizon} DICES: {self.dices} REWARD: {self.reward}' )
```

Do not forget to initialize `self.value` to $0$ in the `wakeUp` method.

## Reward function as a dictionary

Due to uncertainty, doing the same action from the same state will not necessarily fall into the same next state.
It is particularly true on **Py421**.
The idea is to compute statistically reached rewards from experiments.
In other terms the function $r(s, a)$ that return the average reward by doing $a$ in state $s$.
In a pedagogical focus, we propose to implement this function as a dictionary (very convenient but not the most efficient solution).
To learn about python dictionaries you can refer to the [w3schools](https://www.w3schools.com/python/python_dictionaries.asp).

In practice, accessing a reward would lookalike: `self.statRewards[state][action]` where `state` and `action` are string definition of the state and action.
First we have initialized `self.statRewards` as an empty dictionary (`{}`) in the class constructor (`__init__` method in python) i.e. the method called when an instance of the class is created in the program (cf. [w3schools](https://www.w3schools.com/python/gloss_python_class_init.asp) for more details).

```python
def __init__(self):
    self.statRewards= {}
```

The `self.statRewards` is first define over the state space.
Then, each entrance (i.e state), return a new dictionary build over the action state.
If a new state is reached (never visited yet), a new dictionary require to be initialized.
As a first approximation, the state can be built over the dices list.

```python
def perceive(self, gameState):
    [...]
    # define new state
    self.state= str(self.dices)
    if self.state not in self.statRewards :
        self.statRewards[self.state]= {}
```

To validate the increasing number of states in the dictionary, print it in the `sleep` method, at the end of a game.
The _json_ package (cf. [python doc](https://docs.python.org/3/library/json.html)) provides a useful `dump` method to generate a string from the dictionary (and a `load` method for the reverse operation).

```python
def sleep(self):
    [...]
    print(json.dumps(self.statRewards, sort_keys=True, indent=4))
```

Do not forget to import _json_.

Finally, add a new value entrance each time a new action is chosen.

```python
def decide(self):
    [...]
    if action not in self.statRewards[self.state] :
        self.statRewards[self.state][action]= 0.0
    self.action= action
    return action
```

## Learn statistical reward

The idea now is to record a reached reward each time a transition is processed (each time we enter in the `perceive` method after the first time).
However, we cannot state that `self.statRewards[self.state][self.action] = self.reward` while we aim to compute an average reward at run time.
The idea is to introduce a learning rate factor between 0 and 1, and update the new value accordingly to this factor.

After computing the reward and before to update the state information (i.e. `self.state` is still equal to the last reached state in which `self.action` was chosen):

```python
def perceive(self, [...] )
    [...]
    if not self.first : #i.e. it is not the first time we pass here from the last wakeUp.
        self.statRewards[self.state][self.action]= self.statRewards[self.state][self.action]*(1-self.learningRate)
        self.statRewards[self.state][self.action]+= self.reward+self.learningRate
    self.first= False
    [...]
```

Do not forget to initialize the `self.learningRate` in the constructor method (`self.learningRate= 0.1` is generally a good first value) and `self.first` at `True` in the `wakeUp` method.
More about the learning rate on [wikipedia](https://en.wikipedia.org/wiki/Learning_rate).

## First optimization

Until now we just compute and record statistical rewards. 
The idea is to use-it on to take _decision_ at some time (i.e. when we record a good knowledge).
However the first difficulty in reinforcement learning result on the definition of this "at some time".
In other terms, when to stop the computation of statistical kwonledge by exploring actions and to start the exploitation of computed statistics to make decisions.
It is known as the exploration versus exploitation trade-off [cf. [wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning#Exploration)].

One way to overpass the trade-off is to put it random. 
The _ε-greedy_ heuristic suppose that you will choose an exploration action (i.e. a random action for instance) a few times in a given time step.
More technically, at each time step the AI randomly choose to get a random action or to get the best one accordingly to the current knowledge.
The random chose of explore versus exploit is weighted by $\epsilon$ and $1-\epsilon$ with $\epsilon$ between 1 and 0.


```python
def decide(self):
    #random action:
    action= random.choice( self.actions )
    if action not in self.statRewards[self.state] :
        self.statRewards[self.state][action]= 0.0
    #epsilon chose:
    if random.random() >= self.epsilon :
        action= self.bestAction(self.state)
    print( f'Action: {action}' )
    self.action= action
    return self.action
```

Do not forget to initialize the `self.epsilon` in the constructor method (`self.epsilon= 0.1` is generally a good first value, it states that a random action would be chosen 1 time over 10).
The new `decide` method suppose that you implement a `bestAction` method that returns the action entrance with the higher value in the `self.statReward[state]` dictionary.

## Experiement,

Let’s grow iteratively the number of games (parameter `-n` of the server) by 500 each time.
The average score for the player would grow starting from around $190$ with 500 games to an average around $230$ with a consecutive $4000$ games.

## Optional, record the knowledge.

It is possible to `dump` the statistical rewards into a file in the `sleep` method and then `load` it during the `wakeUp` phase.
This way the AI will start a new set of games from it previously learned rewards.
