'''
This is a program that allows the user to type in a phrase and then outputs the
acronym for that phrase.

Aggie Wheeler Bateman

10/17/19
'''

def main():
    print("This is a program that will convert your phrase to an acronym.")
    print()

    userPhrase = input("Please enter your phase: ")

    phraseList = userPhrase.split()
    listAcronym = []
    
    for i in phraseList:
        listAcronym += (i[0])

    strAcronym = "".join(listAcronym)
    print(strAcronym.upper())

main()
