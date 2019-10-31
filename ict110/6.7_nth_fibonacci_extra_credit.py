'''
This is a program that computes the nth Fibonacci number.

Aggie Wheeler Bateman

10/31/19
'''

def getNumber():
    print("Hi, I'm Knipe! I will compute the nth digit of the Fibonacci sequence of a specified number greater than 3.")
    number = int(input("Please enter your desired number greater than 3: "))
    return number
        
    
def fibCompute():
    n = getNumber()
    nSequence = [0, 1]
    for i in range(n - 2):
        nSequence.append(nSequence[i] + nSequence[i + 1])
    return nSequence[n - 1]
    
                         
def giveNumber():
    print("The nth digit of the Fibonacci sequence is " + str(fibCompute()) + ".")

giveNumber()
