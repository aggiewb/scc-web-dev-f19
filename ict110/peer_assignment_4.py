'''
Peer assignment 4
Steps:
1. Get the number of values to be entered from the user.
2. Prompt the user for each number.
3. Total the numbers
4. Print the total
Aggie Wheeler Bateman
10/21/19
'''

def main():
    print("This program will total values entered by the user.")
    n =  int(input("How many values do you want to enter?  "))
    total = 0
    for i in range(n):
        num = int(input("Enter a number:  "))
        total += num #total = num + total
    print("Your total is", total)

main()
