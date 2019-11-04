'''
Peer assignment 6
Calculate weekly wage with functions
1. Get hours worked
2. Get hourly wage
3. Calculate regular pay
4. Calculate overtime pay
5. Calculate weekly pay
6. Print the results

Aggie Wheeler Bateman
11/4/19
'''

REG_HOURS = 40

def getHours():
    hours = int(input("Enter the hours worked for the week: "))
    return hours

def getWage():
    wage = float(input("Enter the hourly wage: "))
    return wage

def calculateRegularPay(hrs, wage):
    regPay = 0
    if hrs > REG_HOURS:
        regPay = (REG_HOURS * wage)
    else:
        regPay = hrs * wage
    return regPay

def calculateOvertime(hrs, wage):
    otPay = 0
    if hrs > REG_HOURS:
        otPay = wage * (hrs-REG_HOURS) * 1.5
    return otPay

def calculateWeeklyWage():
    h = getHours()
    w = getWage()
    reg = calculateRegularPay(h, w)
    ot = calculateOvertime(h, w)
    total = reg + ot
    printWages(reg, ot, total)

def printWages(reg, ot, total):
    print("Your regular pay is: ${0:0.2f}".format(reg))
    print("Your overtime pay is: ${0:0.2f}".format(ot))
    print("Your total pay is: ${0:0.2f}".format(total))

def main():
    calculateWeeklyWage()

main()
    
    
