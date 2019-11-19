class Student:
    def __init__(self):
        self.studentSchool = "Maple Leaf Elementary School"

    def setStudentLastName(self):
        self.studentLastName = input("Enter your last name: ")

    def getStudentLastName(self):
        return self.studentLastName

    def setStudentFirstName(self):
        self.studentFirstName = input("Enter your first name: ")

    def getStudentFirstName(self):
        return self.studentFirstName

    def setStudentGrade(self):
        self.studentGrade = input("Enter your grade level: ")

    def getStudentGrade(self):
        return self.studentGrade

def main():
    student1 = Student()
    student1.setStudentLastName()
    student1.setStudentFirstName()
    student1.setStudentGrade()

    print(student1.studentSchool + ", " + student1.getStudentLastName() + ", " + student1.getStudentFirstName() + ", Grade " + student1.getStudentGrade())

main()

    
        
