'''
This is a program that determines the distance to a lightning strike based
on the time elapsed between the flash and the sound of the thunder.

Aggie Wheeler Bateman

10/10/19
'''

SPEED_OF_SOUND = 1100 #ft/sec
MILE = 5280 #feet

def main ():
          print("Hi, my name is Crash. I'm a friendly bot that will determine how many miles away a bolt of lightning struck near you.")
          print()
          seconds = int(input("Please enter the amount seconds you counted in between the flash of lightning and the sound of thunder: "))
          distance = (SPEED_OF_SOUND * seconds) / MILE
          print("The bolt of lightning you saw is", distance, "miles away.")
main()
