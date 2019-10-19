# File: chaos.py
# A simple program illustrated chaotic behavior.
#Aggie Wheeler Bateman *edited 9/29/19

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:  "))
    y = eval(input("Enter a different number between 0 and 1:  "))
    z = eval(input("Enter a third different number between 0 and 1:  "))
    for i in range(10):
        x = 3.9 * (x - x * x)
        y = 3.9 * (x - x * x)
        z = 3.9 * (x - x * x)
        print (x, y, z, sep = "\n")
        #The default for sep is a space, setting the sep to \n sets the
        #separator to a new line instead.
        print (x, y, z)
        

main()
