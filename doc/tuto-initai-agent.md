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

## Discrete Event Machine

An agent can be seen as a 
discrete event machine [cf. [Wikipedia](discrete-event simulation)].
It will answer a sequence of events in time with a finite method. 
That will result in a succession of `perceptions` and `actions`.

In **HackaGames**, the goal is to optimize action chose to reach best game ends at possible.
In `Py421` the optimization criterion is materialized as a specific `gameState` children modeling the scores. 
The first score is the value of the actual dice combination, the second, the value reached by the opponent.
In the one-player version the opponent score is 0, and the goal is to maximize the average player score.

## Todo: 

For the one player 421 version:

### Define state :


- Define a `state` attribut to `Py421` player as a list of values inside the `perception` method and print it (Python list on [w3schools](https://www.w3schools.com/python/python_lists.asp)).
- Use the `state` attribut to propose an action in `decide` method.

### State space :

The first indication to estimate the complexity of a system to control is the state space, in other terms, the number of states a player can reach.

- Count the number of states a player reach during a bunch of encounters.
- Generate data. write the trace of successive `perception`, `score`, `action` in a external file to permit off-line statistic computations.

