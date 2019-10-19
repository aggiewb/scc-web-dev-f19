'''
peer programming exercise 2
converts to inches to centimeters
Aggie Wheeler Bateman
10/7/18
'''
CONVERSION_INCHES_TO_CENTIMETER=2.54

def main():
    print("This program converts inches to centimeters.")
    inches = eval(input("Enter the number of inches: "))
    centimeters = inches * CONVERSION_INCHES_TO_CENTIMETER
    print(inches, "inches equals", centimeters, "centimeters")

main()
