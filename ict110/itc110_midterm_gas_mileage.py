'''
This is a program to calculate the gas mileage for your car based off of the
total miles traveled and the gallons of gas used for that distance.

Aggie Wheeler Bateman

11/6/19
'''

def getMiles():
    miles = int(input("Please enter the total amount of miles traveled: "))
    return miles

def getGas():
    gas = int(input("Please enter the gallons of gas used: "))
    return gas

def gasMileage():
    print("This is a program to calculate the gas mileage for your car.")
    gasMiles = getMiles() // getGas()
    print("The gas mileage for your car is about", gasMiles, "miles per gallon.")

gasMileage()
