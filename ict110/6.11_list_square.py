'''
This is a program that accepts a list of numbers and
squaring each number in the list.

Aggie Wheeler Bateman

10/31/19
'''

def introState():
    print("Hi, I'm Howard! I am a program that when the squareEach function is called it accepts an arguement of a list with intergers and then returns that list with the numbers squared.")


def squareEach(nums):
    introState()

    #range(min value, max value)
    #min value is by default 0 if not declared
    #max value is assigned if only one number in range
    #range is counted up to the max value, but does not include max value
    squaredList = []

    for i in range(len(nums)):
        squaredList.append(nums[i]**2)
    print("The list of numbers squared is " + str(squaredList))


squareEach([2,5,25,23])
