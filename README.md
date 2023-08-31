# HackaGames - An Hackable Games' Engine

![](resources/logo-128.png)

**HackaGames** aims to be an open game engine dedicated to the development of Artificial Intelligence (AI) based on Operational Research (OR) technic.
The philosophy of hackagames is to permit developers to easily work in any language of its choice.
For that, the project is based on a communication protocol relying on *ZeroMQ* and is developed accordingly to [KISS](https://fr.wikipedia.org/wiki/Principe_KISS) (Keep It Stupid Simple) principle.
The main feature of this project is to permit the game, players and AIs to works on their own process potentially distributed over different machines.
In other terms, **HackaGames** implement a simple client/server architecture to permit AI to take a seat on a game through a simple communication protocol.

**HackaGames** is seen as an API for game development.
Several games are proposed  for example:

- **Py421** (Python): A very simple one player dice game to get the concept of AI implementation (not a core HackaGames client/server game).
- **TicTacToe** (Python): Classic and Ultimate _TicTacToe_ game.
- **Risky** (Python): a simple turm based startegic game.

## Documentation

Documentation is availlable on [https://imt-mobisyst.bitbucket.io/hackagames](https://imt-mobisyst.bitbucket.io/hackagames).

## License

**HackaGame** is distributed under the [MIT license](./LICENCE.md).
This API comme with absolutly no guarantee.


<!-- Obsolote: 
## Installation

**HackaGames** is natively developed on and for Linux systems.
Commands are given regarding Ubuntu-like distribution.
**HackaGames** is packaged in several levels and the level one is only relaing to `python3` language.
This way level one will be easy to install what ever our favorit operating system is.

### Level one (python)

Level one consist in making the **hakapy** `python3` module working.
The network protocol of **HackaGames** relies on `zmq` library and process-bar are implemented via `tqdm`
So first get those dependancies for instance via `pip`.

```sh
pip install zmq tqdm
```

Then get Hackagame by cloning our repository in your working directory. 
**HackaGames** is designed to be installed aside of your developments (AI, new games...).
That for we encurage to first create a workscape (`hacka-workspace` for instance), clone **HackaGames** in this workscape,
and create as new repository as you have new ideas (starting for instant with `tutos`).

```bash
mkdir hacka-workspace
cd hacka-workspace
git clone https://bitbucket.org/imt-mobisyst/hackagames.git
```

That it.
You can play to several of the games (the ones developped on top of `hackapy`), and implement some IAs (cf. **Get Started** section).

**On Windows:**

- You can use [git for windows](https://git-scm.com/download/win) and its `git bash`.
- On your powerShell use `python -m pip` instead of `pip`.

**Optional**

To notice that, you can share your `hacka-workspace` on git-based web services (github, gitlab, our like us [bitbucket.org](https://bitbucket.org)) 
So create your empty repo `my-hacka-workspace` then clone it and clone `hackagames` inside with git-submodule or by add it on `.gitignore` file.

```bash
git clone my-hacka-workspace-url.git hacka-workspace
cd hacka-workspace
git clone https://bitbucket.org/imt-mobisyst/hackagames.git
echo 'hackagames/' >> .gitignore
git add .gitignore
git commit -m "hide hackagames file" 
```

### Level two (C)

Level two consist in compiling the **C** **hackalib** and the games built on top of it.

Actually the **Level two** is desactivated due to majors modification in the client/server protocol.

**HackaGames** is natively developed on and for Linux systems.
Commands are given regarding Ubuntu-like distribution.

The classical way to get **HackaGames** is to clone then buid the project.
So first, you can clone this repository (game engine plus games):

The short way: 

```bash
./bin/install-dependencies
./bin/build
```
For the detailled way, see [install documentation](./doc/hacka-01-install.md)

-->

## In this repository

Directories:

- *bin* : scripts for project management.
- *.git* : git directory (version manager).
- *doc* : some documentation of the project.
- *hackalib* : Librairy and tools like interfaces in different programing language to help connect a game.
- *hackapy* : Python version of the librairy and tools.
- *gameXyz** : game examples on the top of **HackaGames** API.
- *resources* : some resources, images of **HackaGames** project.

Root Files:

- *README.md* : Your servitor.
- *LICENCE.md* : The Applied MIT license.

### Contributors

- Permanent contributor:
  * **Guillaume LOZENGUEZ** - [guillaume.lozenguez@imt-nord-europe.fr](mailto:guillaume.lozenguez@imt-nord-europe.fr)
