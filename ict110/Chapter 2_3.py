#Chapter 2:3 Modify the Avg2 program to find the average of 3 exams
#Aggie Wheeler Bateman
#A simple program to average three exam scores, and illustrates use of
#multiple input

def main():
    print("This program computes the average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma:  "))
    average = (score1 + score2 + score3) / 3

    print("The average score of the scores is:", average)

main()
    
                                        
