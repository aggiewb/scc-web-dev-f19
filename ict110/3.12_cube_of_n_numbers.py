'''
This is a program that finds the sum of the cube of the first "n" natural
numbers where the value of "n" is provided by the user.

Aggie Wheeler Bateman

10/10/19
'''

import math

def main():
    print("Hi! My name is Ice. I am program that will calculate the sum of the cube of natural numbers.")
    userNaturalNumber = int(input("Please enter the number that I will calculate up to: "))
    cube = 0
    for cube in range (1, userNaturalNumber + 1):
        cubeNaturalNumber = int((math.pow(cube, 3) + cube))
        #the following is an example of the long version of the loop:
        #cubeNaturalNumber = (1 * 1 * 1) + 0
        #cubeNaturalNumber = (2 * 2 * 2) + 2
    print("The sum of the cube of your series of natural numbers is", cubeNaturalNumber) 
    
main()
