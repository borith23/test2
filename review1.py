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
        print("My name is", self.firstName, self.lastName, "and Gender:", self.gender)
nameTeacher = Teacher("Rady", "Y", "male")
nameTeacher.showTeacher()

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())   
print(my_list)
print(next(my_iter))    
print(my_iter.__next__())  

print("=========>*<==========")

for x in my_list:
    print(x)

print("=========>*<==========")

length = len(my_list)
for i in range(length): 
    print(my_list[i]) 