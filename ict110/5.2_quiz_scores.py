'''
This a program that accepts a quiz score as an input and prints out the
cooresponding grade.

Aggie Wheeler Bateman

10/17/19
'''

def main():
    print("Hi! My name is Quizzo, and I will convert your quiz score to its cooresponding letter grade.")
    print()

    quizScore = int(input("Please enter your quiz score (1-5): "))

    gradeList = ["F", "F", "D", "C", "B", "A"]

    print("Your letter grade is", gradeList[quizScore])

main()

    
    
