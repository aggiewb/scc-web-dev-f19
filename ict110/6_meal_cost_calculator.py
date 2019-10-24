'''
This is a program that calculates a tip.
It will consist of four separate functions to take in the meal amount,
get the tip percent, calculate the tip amount, and output the result.

Aggie Wheeler Bateman

10/24/19
'''

def getTipPercent():
    tipPercent = int(input("Enter ze tip percent you'd like to give your garçon: "))
    return tipPercent


def getMealAmount():
   mealAmount = float(input("Enter ze meal amount: "))
   return mealAmount

def calculateTipAmount():
    tipPercent = getTipPercent()
    mealAmount = getMealAmount()
    tipAmount = mealAmount * (tipPercent/100)
    print("Your tip should be ${0:0.2f}".format(tipAmount))

def tipOutput():
    print("Bonjour! I'm Aimée, and I am able to calculate ze tip for you.")
    calculateTipAmount()

tipOutput()


