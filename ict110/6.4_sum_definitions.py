'''
This is a program uses two functions to (1) print out the sum of the first n
natural numbers and (2) print the sum of the cubes of the first n natural
numbers.

Aggie Wheeler Bateman

10/24/19
'''

import math

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("The sum of the first natural numbers of " + str(n) + " is " + str(int(sum)) + ".")

def sumNCubes(n):
    sumCube = 0
    for i in range(1, n+1):
        sumCube += math.pow(n,3)
    print("The sum of the cubes of the first natural numbers of " + str(n) + " is " + str(int(sumCube)) + ".")

def getNum():
    n = int(input("Enter the number that you'd like the sum of the first natural numbers and the sum of the cubes of the first natural numbers: "))
    sumN(n)
    sumNCubes(n)

getNum()
    


        
    


