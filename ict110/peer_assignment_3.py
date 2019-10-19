'''
Peer Assignment 3
Determine how many vans are needed to move people
Aggie Wheeler Bateman
10/13/19
'''

VAN_MAX = 8

def main():
    print("This program determines how many vans are needed for a group of people")
    people  = eval(input("Enter the total amount of riders: "))
    vans = people // VAN_MAX
    if people % VAN_MAX > 0:
        vans = vans + 1
    print("You will need", vans, "vans.")

main()
