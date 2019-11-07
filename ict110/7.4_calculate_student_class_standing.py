'''
This is a program that calculates class standing from the number of
credits earned.

Aggie Wheeler Bateman

11/7/19
'''

def hoursCompleted():
    hoursCompleted = int(input("Please enter the amount of credit hours you have completed: "))
    return hoursCompleted

def determineClass():
    hours = hoursCompleted()
    if hours >= 26:
        return("Senior.")
    elif hours >=16:
        return("Junior.")
    elif hours >=7:
        return("Sophomore.")
    elif hours <7:
        return("Freshman.")

def classStandingOutput():
    print("Hi, I'm Hoots the Owl! I can determine your class based off of the amount of credits you've earned.")
    print("Your class standing is", determineClass())

classStandingOutput()
