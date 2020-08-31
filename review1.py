class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def displayDetail(self):
        print(self.firstName, self.lastName)


class Staff(Person):
    pass
nameStaff = Staff("Rith", "BO")
nameStaff.displayDetail()


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.year = 21
    
nameStudent = Student("lunar", "life")
nameStudent.displayDetail()
print(nameStudent.year)

class Teacher(Person):
    def __init__(self, fname, lname, sex):
        super().__init__(fname, lname)
        self.gender = sex 

    def showTeacher(self):
        print("I'm name is", self.firstName, self.lastName, "and Gender:", self.gender)
nameTeacher = Teacher("Rady", "Y", "male")
nameTeacher.showTeacher()
