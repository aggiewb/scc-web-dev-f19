'''
This is a program that contains a class called "area", that takes in two
parameters "side1", and "side2".  The measurements are in feet. Inside the
class there is a function that calculates the total area by multiplying side1
and side2. There is also function that returns the total area and a __str__
function that returns "The total area is " + [area in square feet] (put your
variable here). In the main function, the class will be called, which prints
the string.

Aggie Wheeler Bateman
12/8/19
'''

class Area:
    def __init__(self, side1, side2):
        self.side1=side1
        self.side2=side2

    def calTotalArea(self):
        totalArea = self.side1 * self.side2
        return totalArea

    def __str__(self):
        return "The total area is " + str(self.getTotalArea()) + " feet."

    def getTotalArea(self):
        return self.calTotalArea()

    def main():
        print(Area(3, 12))


Area.main()
        
