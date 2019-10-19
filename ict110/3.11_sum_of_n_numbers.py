'''
This is a program that finds the sum of the first "n" natural numbers, where
the value of "n" is provided by the user.

Aggie Wheeler Bateman

10/10/19
'''

def main():
    print("Hi, my name is Numba. I am a program that will calculate the sum of natural numbers.")
    userNaturalNumber = int(input("Please enter the final number in which I will find the sum of the first natural numbers up to: "))
    sumNatural = 0
    for count in range(1, userNaturalNumber + 1):
        sumNatural += count
        #the following is the long written example of the loop in action:
        #sumNatural = sumNatural + count
        #sumNatural = 0(sumNatural) + 1(count)
        #sumNatural = 1(sumNatural) + 2(count)
        #sumNatural = 3(sumNatural) + 3(count)
    print("The sum of the natural numbers is", sumNatural)
        
main()

