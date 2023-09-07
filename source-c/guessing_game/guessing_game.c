#include "zetz/guessing_game.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static int s_secret_number = 0;

void zetz_guessing_game_init()
{
    srand((unsigned)time(NULL));
    s_secret_number = rand() % 100;
}

void zetz_guessing_game_run()
{
    printf("Guess the number!\n");

    int guess = 0;
    while (1)
    {
        printf("Please input your guess.\n");
        scanf("%d", &guess);

        printf("You guessed: %d\n", guess);

        if (guess == s_secret_number)
        {
            printf("You win!\n");
            break;
        }
        else if (guess < s_secret_number)
        {
            printf("Too small!\n");
        }
        else
        {
            printf("Too big!\n");
        }
    }
}