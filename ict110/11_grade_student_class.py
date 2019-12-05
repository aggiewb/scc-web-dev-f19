'''
This is a program that will contain three classes: Grade, Student, and
Display.

The Grade class contains the class name, the credits and the grade point
(from 0 to 4) for the grade.

The Student class contains the students name and id number and a list of
grade objects. It has methods to enter the name and id, and a method to
calculate a GPA.

The Display class allows you to enter the information into the Grade and
Student classes and then displays the student name, student id, and their GPA.

Aggie Wheeler Bateman
12/5/19
'''

class Grade:
    def __init__(self, className, classCredits, gradePoint):
        self.className = className 
        self.classCredits = classCredits
        self.gradePoint = gradePoint
            

class Student:
    def __init__(self, studentName, studentID):
        self.studentName = studentName
        self.studentID = studentID
        self.grades = []

    def addGrades(self):
        decision = "yes"
        while decision == "yes":
            className = input("Enter your class name: ")
            classCredits = int(input("Enter the classes's credits: "))
            gradePoint = float(input("Enter your grade point(0-4) for that class: "))
            self.grades.append(Grade(className, classCredits, gradePoint))
            decision = input("Do you have more classes to enter, yes or no? ")

    
    def studentGPA(self):
        weightsSum = 0
        creditsSum = 0
    
        for i in range(len(self.grades)):
            currentGrade = self.grades[i]
            gradePoint = currentGrade.gradePoint
            classCredits = currentGrade.classCredits
            classWeight = gradePoint * classCredits
            weightsSum += classWeight
            creditsSum += classCredits

        studentGPA = weightsSum / creditsSum
        print("Their GPA is {0:0.2f}".format(studentGPA) + ".")
            
        
class Display:
    def userInfo():
        studentName = input("Enter your first and last name: ")
        studentID = input("Enter your student ID: ")
        person = Student(studentName, studentID)
        person.addGrades()
        print("The student that was entered is " + person.studentName + ". The student ID is " + person.studentID + ".")
        person.studentGPA()


Display.userInfo()







        
