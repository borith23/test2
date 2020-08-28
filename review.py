#Creat class person
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def displayName(self):
        print(self.firstName, self.lastName)


#Create class teacher and inheritance from super class Person
class Teacher(Person):
    pass
x = Teacher("Python", "Nice")
x.displayName()

#create class student and exstane from Person class and add method graduatYear
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduatYear = 2020

nameStudent = Student("Borith", "MOEK")
print(nameStudent.graduatYear)


#creat function and global varaible
h = "Guy"
def fun():
    global h
    h = "Way"
    print("hello " + h)
fun()
print(h)

#Display string with number by format method
a = 10
b = 100
c = 1000
myorder = "I want {2} pieces of item {1} for {0} dollars."
print(myorder.format(a, b, c))
print("I want " + format(a) + " pieces of item " + format(b) + " for " + format(c) + " dollars.")


list = ["book", "pen", "class"]
for show in list:
    print(show)
    break

def k():
    print("I'm K")
k()

