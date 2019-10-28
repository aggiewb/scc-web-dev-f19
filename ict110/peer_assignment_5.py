'''
Peer assignment 5

steps:
1. get a sentence from a user
2. split the sentence to get a list of the words
3. loop through the list of words
4. get the length of each word
5. total the lengths of all the words
6. divide the total lengths by the number of words in the list
7. print the average

Aggie Wheeler Bateman
10/28/18
'''

def main():
    print ("This program returns the average word length in a sentence.")
    sentence = input("Enter a sentence: ")
    words = sentence.split() #divide by comma sentence.split(',')
    totalLength = 0
    for w in words:
        totalLength += len(w)
    averageLength = totalLength / len(words)
    print ("The average length of the a word is {0:0.1f}".format(averageLength), ".")

main()
    
    

