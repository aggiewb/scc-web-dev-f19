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
        self.charge = float(charge)
        self.percentTip = float(percentTip)
        self.taxRate = float(taxRate)

    @property
    def charge(self):
        return self.charge
    #this is the getter(accesor)

    @charge.setter
    def charge(self, charge):
        self.charge = float(charge)
    #this is the setter(mutator)

    @property
    def percentTip(self):
        return self.percentTip
    #this is the getter(accesor)

    @percentTip.setter
    def percentTip(self, percentTip):
        self.percentTip = percentTip
    #this is the setter(mutator)

    def getTaxRate(self):
        return self.taxRate
    #this is the getter(accessor)

    def setTaxRate(self, taxRate):
        self.taxRate = taxRate
    #this is the setter(mutator)

    def tipAmount():
        tipAmount = (percentTip/100) * charge
        return tipAmount

    def taxAmount():
        taxAmount = (taxRate/100) * charge
        return taxAmount

    def totalCost():
        totalCost = tipAmount() + taxAmount() + charge
        print("The tip amount is" + tipAmount() + ".")
        print("The tax amount is" + taxAmount() + ".")
        print("The total cost is" + totalCost + ".")





    


        

    


    

    
        

        
        
        
