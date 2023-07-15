## To-Do

- Update BOARD structure.
	* Geometry 2D (coordinates)
- Reinforcement-Learning: Sleep with last perception elements.
- Revise doc structure with section/directories.
- Complete HackaGames Py421 state (i.e. horizon = 0 wen `keep-keep-keep`, and modify stateStr in Q-Learning tutorials).
- Complete Tutos and set a first clean version (WebPage), WebPage Doc with no subterfuge

- Reactivate - TicTacToe
- Doc: impose Launcher as a first solution, then the Client/Server option.
- Think a simple Risky (metha-action) (expand X, fight Y, reinforce) 
- Initialize a `log` function in games and players to put the things potentially silent.
- HackaLib - C lib + gameC421 exemple (game421 -> gamePy421).
- Change `local` to `start` or `play` and pootentially `start` to `server`. Attention to change the documentation as well.
- Look at PAIO-promo2022-grp-vert code and their python based viewer...
- Initialize a move game (no crach, MAPF) or something like that.
- larger dice game - the return of zombie game ?
- Integrate a Game Engine (gestion des collision, rendu graphique....): Option: (Best Box2d - godot)
	+ RayLib (Simple...)
	+ Godot - https://en.wikipedia.org/wiki/Godot_(game_engine)
	+ ClanLib - https://github.com/sphair/ClanLib
	+ Delta3D - https://en.wikipedia.org/wiki/Delta3D
	+ ORX - https://orx-project.org/news/
	+ box2d.org
	+ FlatLand
	+ Cairo - https://en.wikipedia.org/wiki/Cairo_%28graphics%29
- Integrate ShapeFile format.

Aprés HackaGames se veux etre un game Engine a TDH engine (Two Dimension and a Half)

Q= {
    'end'= { 'kkk': 0, 'rkk': 0 .... },
    '4-2-1'= { 'kkk': 0, 'rkk': 0 .... },
    'X-2-1'= { 'kkk': 0, 'rkk': 0 .... },
    'X-1-1'= { 'kkk': 0, 'rkk': 0 .... },

    ...
 }

 168 X 8 : q-valeurs.