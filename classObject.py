#Creat parent class Person
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def showDetail(self):
        print("My name is ", self.firstName, self.lastName)


#Inheritance from class Person
#Pass: do not want to add any other properties or methods to the class
class Student(Person):
    pass

nameStudent = Student("Borith", "MOEK")
nameStudent.showDetail()


#Inheritance from class person but add method gender
class Teacher(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.gender = "Male"

nameTeacher = Teacher("Lunar", "MOON")
nameTeacher.showDetail()
print(nameTeacher.gender)


#Inheritance from class Teacher and add method year
class Chile(Teacher):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.bd = 2017

nameChile = Chile("Nana", "Baby")
print("Chile BD: ", nameChile.bd)

#Inheritance from class Teacher with graduatYear
class StudentGraduat(Teacher):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduatYear = year

    def showGraduatYear(self):
        print(self.firstName, self.lastName, "graduat: ", self.graduatYear)

nameStudentGraduat = StudentGraduat("Borith", "Moek", 2020)
nameStudentGraduat.showGraduatYear()


#Inheritanc from class person
class Staff(Person):
    # def __init__(self, fname, lname):
    pass
nameOfStaff = Staff("Neymar", "jR")
nameOfStaff.showDetail()


i = "apple"
for k in i:
    print(k)
    break
    
print("hello")