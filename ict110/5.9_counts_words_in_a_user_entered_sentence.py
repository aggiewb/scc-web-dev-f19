'''
This is a program that counts the number of words in a sentence
entered by the user.

Aggie Wheeler Bateman

10/17/19
'''

def main():
    print("Hi! My name is Counter. I will count the number of words in a sentence excluding punctuation.")
    print()

    userSentence = input("Please enter the sentence you would like me to count and exclude any punctuation: ")

    sentenceList = userSentence.split()

    print("The amount of words in your sentence is", len(sentenceList))

main()
    

    
