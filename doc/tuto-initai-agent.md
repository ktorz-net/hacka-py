# The notion of Agent

- Return to the [Table Of Content](toc.md)

The Agent is a central element in Artificial Intelligence theory.
It is both a software module involving AI algorithms and a concept permitting to handle complex systems.
The notion of agent is the core notion of Agent-Based modeling [cf. [Wikipedia](https://en.wikipedia.org/wiki/Agent-based_model)] allowing to understand systems as interacting autonomous agents.


## Perception and action loop

We are here interested in the decision process of autonomous agents.
As a first definition an agent is an entity capable of perception and action in it environment [cf. [Wikipedia](https://en.wikipedia.org/wiki/Agent-based_model)] 

In **HackaGames** the notion of Agent is concretely implemented through the player's methods: `perceive` and `decide`.
The two methods would be continuously called until the end of a game, by starting with `perceive`.
As for, a player artificial intelligence can be seen as an Agent playing in the game.

As for the classical Agent simulation, developers do not control the program loop.
Developers propose agents, and agents are activated at the turn by the program with the appropriate methods.
The life processes of an agent on HackaGames is also bounded by the methods `wakeUp` and `sleep` to indicate to the agent that a new game start or stop.

As a simple exercice the idea is to trace the experiences by editing a log file.
The log file includes the successive `perception`, `score`, `action` to permit off-line statistic computations and learning (i.e. generate simulated Data).
In python it consist in _open_ a file in _append_ mode. Then it is possible to write string before to close the resource (more about files on the [w3schools](https://www.w3schools.com/python/python_file_handling.asp)).

```python
dataFile = open("data.log", "a")
dataFile.write("hello file\n")
dataFile.close()
```

In the shell, `ls` permit to validate the presence of _data.log_ file, `cat data.log` to print in content into the terminal ,`cp data.log new_data.log` and `rm data.log` to copy and to remove it.

**to-do:** open and close the file respectively into `wakeUp` and `sleep` methods and print a new line with the perception and the chosen action respectively into `perceive` and `decide` methods.
You have a first version of data generators.
You can learn more about string manipulation in python with the [w3schools](https://www.w3schools.com/python/python_strings.asp).


## Discrete Event Machine

An agent can be seen as a discrete event machine [cf. [Wikipedia](https://en.wikipedia.org/wiki/Discrete-event_simulation)].
It will answer a sequence of events in time.
That will result in a succession of _events_ or _perceptions_ and _responses_ or _actions_.

Following this principle, most of the deliberative agents are based on automata theory [cf. [Wikipedia](https://en.wikipedia.org/wiki/Automata_theory)]
The finite number of game configurations defines the state space of the player.
However in most applications a state is multi-variable. It is defined on as a tuple of value, at least the value of 3 dice in **Py421**.
Transition from a state $s$ to a new one $s'$ depends on the chosen action and the reached new state.


**to-do:** define a state attribute to your player as a finite list of finite values.
For instance `self.state= [D1, D2, D3]` for a state based on the 3 dices values (but more elements can be included).
Update your log file consequently (`dataFile.write("P: {self.state}\n")`).
The final log file would lookalike: 

```
P: [4, 2, 1]
A: rool-rool-rool
P: [6, 3, 1]
A: keep-keep-keep
P: [6, 3, 1]
P: [5, 5, 2]
A: keep-rool-keep
P: [5, 4, 2]
...
```


## Todo: 

For the one player 421 version:

### Define state :


- Define a `state` attribut to `Py421` player as a list of values inside the `perception` method and print it (Python list on [w3schools](https://www.w3schools.com/python/python_lists.asp)).
- Use the `state` attribute to propose an action in `decide` method.

### Optional :


**State Space:**  

At run time, count the number of visited states.
One way to do that is to feed a dictionary with the perception line (string format) and, at the end to count the number of entrances.
More about python dictionary on the [w3schools](https://www.w3schools.com/python/python_dictionaries.asp).

By the way with the dictionary, you can count the number of time you reach each state. Are they equiprobable ?

**Optimization:**  

In **HackaGames**, the goal is to optimize action chose to reach best game ends at possible.
In `Py421` the optimization criterion is materialized as a specific `gameState` children modeling the scores. 
The first score is the value of the actual dice combination, the second, the value reached by the opponent.
In the one-player version the opponent score is 0, and the goal is to maximize the average player score.

You can add a line `V:` that states the values after printing a perception.

The two values' vector is not directly integrable into optimization algorithms.
Only the modification in time of the difference between the player score and the opponent score is relevant.
Modify the value `V:` line into a reward `R:` line that highlights this change:
$$
\mathit{reward}=  (player.score - opponent.score)_{t} - (player.score - opponent.score)_{t-1}
$$
