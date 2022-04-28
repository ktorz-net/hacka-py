/*******************************************************************************************
*
*   HackaGames
*   Copyright (c) 2020-2021 Guillaume Lozenguez - Institut Mines-Telecom
*
********************************************************************************************/
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "risky.h"

#define NUM_PLAYER 2
#define NUM_TURN   30
#define NUM_ACTION_PER_TURN 1

int fight( Organism* target, int strengh )
    { return fightDeterminist(target, strengh); }

int main(int nbArg, char ** arg)
{
    // Game Initialization
    //--------------------
    Game* game= initializeGame();

    int nbGame= 1;
    if( nbArg > 1 )
        nbGame= atoi( arg[1] );

    int nbTurn= NUM_TURN;
    if( nbArg > 2 )
        nbTurn= atoi( arg[2] );

    if( nbArg > 3 )
        game->port= atoi( arg[3] );

    int mapSeed= time(NULL);
    if( nbArg > 4 )
        mapSeed= atoi( arg[4] );

    int seed= time(NULL);
    if( nbArg > 5 )
        seed= atoi( arg[5] );
    
    puts("Game initialized");

    // Launch the Game
    //----------------
    Game_start( game );
    puts("Game started");

    // Main game loop
    puts("Starts the games:");
    for( int iGame= 0 ;  iGame < nbGame ; ++iGame )
    {
        srand( mapSeed );
        resetGame(game);
        srand( seed );
        riskyLoop(game, nbTurn, NUM_ACTION_PER_TURN );
        
        printf("score: %d(%f), %d(%f)\n",
            game->sockets[1], game->scores[1],
            game->sockets[2], game->scores[2] );
        
        if( iGame % 2 == 1)
        {
            mapSeed+= 1;
            seed+= 1;
        }
        else
        {
            game_switchPlayers(game);
        }
    }
    
    // Stop IHM
    //-----------
    Game_stop( game );
    
    Game_delete( game );
    return 0;
}
