'''
This is a program that uses a while loop to determine how long it takes
for an investment to double at a given rate. The input will be an annualized
interest rate, and the output is the number of years it takes an investment to
double.

Aggie Wheeler Bateman

11/7/19
'''

def getRate():
    rate = float(input("Please enter the annualized interest rate: "))
    initInvest = float(input("Please enter your initial invesment amount: "))
    return rate, initInvest
