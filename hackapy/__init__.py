#!env python3

from . import pieceOfData, board, game, player, command
#from . import element, interprocess, game, player, cmd

# HackaGames Elements
Pod= pieceOfData.Pod
Board= board.Board
AbsGame= game.AbsGame
AbsSequentialGame= game.AbsSequentialGame
AbsSimultaneousGame= game.AbsSimultaneousGame
AbsPlayer= player.AbsPlayer
PlayerIHM= player.PlayerIHM

#Piece= game.Piece
#Cell= game.Cell
#Tabletop= game.Tabletop

# Command tools
StartCmd= command.StartCmd
