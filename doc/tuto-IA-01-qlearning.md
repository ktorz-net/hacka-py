# Q-Learning

**Q-Learning** is a  quite simple and we aim to implement it for learning to play to **421** game.

1. Implement a new *PlayerQ*
2. At initialization **Q** is created empty with the other required variable.
3. At perception steps the player update its **Q-value** and choose a new action to perform accordingly to **Q-Learning** algorithm.

## Ints for implementing Q

A simple way to implement **Q** in python language is to implement it as a Dictionnary of dictionaries.

- [Python documentation](https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries)
- [On w3school](https://www.w3schools.com/python/python_dictionaries.asp)

Initilizing an empty **Q** will look like:

```python
qvalues= {}
```

Typically in the constructor method `__init__` in python (and with Q-Learning attributes):

```python
class QPlayer :
    def __init__(self, explorationRatio=0.1, discountFactor=0.99, learningRate= 0.1 ):
        self.epsilon= 0.1 # the exploration ratio, 0.1 over 1 chance to take a random action.
        self.gamma= 0.99 # the discount factors, interest of immediate reward regarding future gains
        self.alpha= 0.1 # the learning rate, speed that incoming experiences erase the oldest.
        self.qvalues= {} # 
```

Initilizing action values for a given state will look like:

```python
state= "2-6-3-2"
if state not in self.Q.keys() :
    self.qvalues[state]= { "keep-keep-keep":0.0, "roll-keep-keep":0.0, "keep-roll-keep":0.0, "roll-roll-keep":0.0, "keep-keep-roll":0.0, "roll-keep-roll":0.0, "keep-roll-roll":0.0, "roll-roll-roll":0.0 }
```

A new state requires to be added to `qvalues` each time it is necesary in the `wakeUp` and the `perceive` methods.
To test the increasing dictionary it is possible to simply use the python function `print` with the dictionary in parameter.

```python
print(self.qvalues)
```

Finally, modifying a value in **qvalues** will look like:

```python
self.qvalues["2-6-3-2"]["roll-roll-roll"]= ...
```

**To resume**

1. First you have to increase **Q** dictionary with a new entrance each time a new state is visited.
2. Then you can implement the update of **Q** value for the last visited state (`Q[stateStr][actionStr]`)
   - To notice that *updateQ* will require another method to select the maximal value in **Q** for a given state.
3. Now the *action* method can randomly select an exploration or an exploitation action.
   - To notice that *action* will require another method to select the action with the maximal value in **Q** for a given state.
4. A proper **PlayerQ** class permit users to customize the algorithms parameters $\epsilon$, $\gamma$ ... Let’s do it in the `__init__` method (with default parameters value).
   - Handle default parameters value in python with [w3schools](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp).

<!--
To notice that in professional condition (if you target to become an engineer in Computing Science), you will rarely have a decomposition of the tasks to achieve.
-->

You ~~can~~ must test your code at each development step by executing the code for few games and validate that the output is as expected (a good python tool to make test: `pytest`).

1. You can now try to answer the question: how many episodes are required to learn a good enough policy.

## Going further:

1. *PlayerQ* save its learned **Q-values** on a file.
2. *PlayerQ* initialize its **Q-values** by loading a file.
3. A new *PlayerBestQ* simply play the best action always from a given **Q-values** dictionary (without upgrading **Q**).
4. You are capable of plotting the sum over **Q** with one point per episode (with [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) for instance).
