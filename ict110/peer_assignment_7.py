'''
This program creates a guessing game. The game gets a random number between
1 and 1000. The user/player gets 10 chances to guess the number. The program
responds to each guess by telling them too high, too low or correct. Each try
starts off with 10 points. Each wrong guess subtracts one point.

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

from random import randrange

#introduction
def intro():
    print("This program is a simple guessing game.")
    print("The program will generate a random number between 1 and 1000.")
    print("You get 10 guesses.")
    print("The game will tell you if the guess is too high, too low, or correct.")
    print("Each time you play is worth 10 points. Each wrong guess substracts a point.")

def getRandom():
    number = randrange(1, 1001)
    return number

def getUserGuess():
    guess = int(input("Enter a guess between 1 and 1000: "))
    return guess

def evalGuess(number, guess):
    state = 0
    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Congrats! You got it!")
        state = 1
        return state

def play():
    number = getRandom()
    score = 10
    for i in range(0, 11):
        guess = getUserGuess()
        state = evalGuess(number, guess)
        if state == 1:
            break
        score = score-1
    return score

def game():
    choice = "y"
    scores = []
    while choice == "y":
        score = play()
        print("Your score was", score)
        scores.append(score)
        choice = input("Play another game? Enter Y to continue: ")
        choice.lower()
    return scores

def getAvgScores(scores):
    total = 0
    for item in scores:
        total += item
    average = total/len(scores)
    return average

def printAverage(average):
    print("Your average score was", average)

def main():
    intro()
    scores = game()
    avg = getAvgScores(scores)
    printAverage(avg)

main()  

