'''
This is a program a program that allows a user to enter data that is
written to a text file and will read the file.

Aggie Wheeler Bateman

10/17/19
'''

from tkinter.filedialog import askopenfilename

def main():
    print("Hi! I am Text, and I will allow you to enter a text file, and I will read the file.")
    print()

    userTextFile = askopenfilename()
    data = open(userTextFile, "r")

    print(data.read()) #This way of printing using a read method may cause the formatting to be lost


    #You can also use a for loop to iterate each line of the data
    #for line in data:
        #print(line)

main()
