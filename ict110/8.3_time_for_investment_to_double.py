'''
This is a program that uses a while loop to determine how long it takes
for an investment to double at a given rate. The input will be an annualized
interest rate, and the output is the number of years it takes an investment to
double.

Aggie Wheeler Bateman

11/7/19
'''

def getRate():
    return float(input("Please enter the annualized interest rate: "))

def getInitInvest():
     return float(input("Please enter your initial invesment amount: "))
     
def calInvestment():
    initialInvest = getInitInvest()
    annualRate = getRate()

    investment = initialInvest
    count = 0

    while (investment / initialInvest) < 2:
        investment += ((annualRate/100) * investment)
        count += 1

    print("The amount of time it will take you to double your investment is", count, "years.")
    print("You will have earned ${0:0.2f} in that amount of time.".format(investment))


calInvestment()
