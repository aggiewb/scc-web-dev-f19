'''
This is a program that uses a funtion to return a grade letter for a score.

Aggie Wheeler Bateman

10/30/2019
'''

import math

def getScore():
    print("Hi, I'm Kate! I am a program that will tell you what letter grade you've gotten for your exam score.")
    score = int(input("Enter your exam score: "))
    return score

def findLetter():
    userScore = getScore() // 10 - 1
    letterScore = ["F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    print(letterScore[math.floor(userScore)])

findLetter()
    

    
