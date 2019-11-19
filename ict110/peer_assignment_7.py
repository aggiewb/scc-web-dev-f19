''' This program creates a guessing game. The game gets a random number
between 1 and 1000. The user/player gets 10 chances to guess the number. The
program responds to each guess by telling them too high, too low or
correct. Each try starts off with 10 points. Each wrong guess subtracts one
point.

The players score is however many points they have when they guess the right
answer or 0 if they don't. At the end of each game the plater is asked whether
or not they want to play again. If yes, the game restarts, if not the player
is given an average of their scores and the game quits.

Programming steps for the game:
1. Get a random number
2. Loop 10 times:
    a. Get the user's guess
    b. Determine if it is too high, too low, or correct
    c. Adjust the player score
3. Display player score
4. Add score to list of scores
5. Ask player if they want to play again
    a. If YES start new game
    b. If NO show average score and quit

Aggie Wheeler Bateman
11/19/2019
'''
