'''
This is a program uses two functions to (1) print out the sum of the first n
natural numbers and (2) print the sum of the cubes of the first n natural
numbers.

Aggie Wheeler Bateman

10/24/19
'''

#Returns the sum of the first n natural numbers

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)
    

sumN(4)
        
    


