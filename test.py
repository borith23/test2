

class Person:
  def __init__ (self, fname, lname):
    self.firstName = fname
    self.lastName = lname

  def printname(self):
    print(self.firstName + " " + self.lastName)

name = Person("Borith", "MOEK")
name.printname()


class Student(Person):
  def __init__ (self, fname, lname):
    Person.__init__(self, fname, lname)


nameStudent = Student("Lunar", "MOON")
nameStudent.printname()
