'''
This is a program that calculates the cost of an order at a coffee shop.

Aggie Wheeler Bateman

10/10/19
'''

COFFEE_PER_POUND = 10.50 #dollars

def main():
          print("Welcome to Coffee Inc. order calculation system. This system will calcute the cost of an order.")
          print()
          orderAmount = float(input("Please enter the amount of pounds of coffee ordered: "))
          shippingCost = (0.86 * orderAmount) + 1.50 #dollars
          orderCost = (orderAmount * COFFEE_PER_POUND) + shippingCost
          print("The total cost of your order is $", orderCost)
main ()
