'''
This program will involve creating a class called Tip that calculates the
amount of a tip. The program will have mutators and accesors to take in
the amount of the charge, the percent for the tip, and the tax rate. The
program should have methods that return, the tip amount and the tax amount
and the total cost.

Aggie Wheeler Bateman
11/14/19
'''

class Tip():
    def __init__(self, charge, percentTip, taxRate):
        self.charge = charge
        self.percentTip = (percentTip/100) * charge
        self.taxRate = (taxRate/100) * charge

    def totalCost(self):
        tipAmount = self.percentTip
        taxAmount = self.taxRate
        totalCost = self.percentTip + self.taxRate + self.charge
        print("The tip amount is ${0:0.2f}.".format(tipAmount))
        print("The tax amount is ${0:0.2f}.".format(taxAmount))
        print("The total cost is ${0:0.2f}.".format(totalCost))

    def getCharge(self):
        return self.charge

    def getPercentTip(self):
        return self.percentTip

    def getTaxRate(self):
        return self.taxRate
                   
def getInput():
    charge = float(input("Please enter the charge without tax and tip: "))
    percentTip = float(input("Please enter the tip percent you'd like to give: "))
    taxRate = float(input("Please enter the sales tax rate in your area: "))
    return charge, percentTip, taxRate
              
def main():
    charge, percentTip, taxRate = getInput()
    c1= Tip(charge,percentTip,taxRate)
    c1.totalCost()
    print("Your stated charge amount is ${0:0.2f}.".format(c1.getCharge()))
    print("Your stated tip percent is {0}%.".format(c1.getTaxRate()))
    print("Your stated tax rate is {0}%.".format(c1.getTaxRate()))

main()
    


