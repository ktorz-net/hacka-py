# Hacka-Py - Pure Python version of HackaGames<br /> An Hackable Games' Engine

![](resources/logo-128.png)

**HackaGames** aims to be an open game engine dedicated to the development of Artificial Intelligence (AI) based on Operational Research (OR) technics.
**HackaGames** is seen as an API for game development not dedicated to graphic rendering or IHM, but to the interconnection of game and players processes.
The philosophy of **HackaGames** is to permit developers to easily work in any language of their choice.
For that, the project is based on a communication protocol relying on *ZeroMQ* and is developed according to the [KISS](https://fr.wikipedia.org/wiki/Principe_KISS) (Keep It Stupid Simple) principle.
The main feature of this project is to permit the game, players and AIs to work on their own processes, potentially distributed over different machines.
In other terms, **HackaGames** implements a simple client/server architecture to permit _AI_ to take a seat on a game through a simple communication protocol.


## Resources

- Pypip page [pypi.org/project/hacka](https://pypi.org/project/hacka).
- Source code is shared on github: [www.github.com/ktorz-net/hacka-py](https://www.github.com/ktorz-net/hacka-py). 
- Documentation is available on [ktorz-net.github.io/hackagames](https://ktorz-net.github.io/hackagames).
- First games are proposed on [www.github.com/ktorz-net/hackagames](https://www.github.com/ktorz-net/hackagames).


## Get Started

The Python version of the **HackaGames** engine is shared through [pypi.org](https://pypi.org/project/hacka/) and can be installed with `pip install hacka`. 
It is possible to install it from this repository to use the on-developpement version.

```shell
git clone https://www.github.com/ktorz-net/hacka-py
pip install ./hacka-py
```

## License

**HackaGame** is distributed under the [MIT license](./LICENCE.md).
This API comes with absolutely no guarantee.


## Contributors

- Permanent contributor:
  * **Guillaume LOZENGUEZ** - [guillaume@drods.net](mailto:guillaume@drods.net)



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
