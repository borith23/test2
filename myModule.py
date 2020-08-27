
def greeting(name):

    print("Hello, " + name)

person1 = {
    "name": "Rith",
    "age": 21,
    "country": "Cambodia"
}


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    
    def displayName(self):
        print(self.firstName, self.lastName)


class Student(Person):
    pass
studentName = Student("Bo", "Rith")
studentName.displayName()

if 50 == 30:
    print("True!")
else:
    print("False!")


if 5 > 3 and 2 < 5:
    print("Good!")
else:
    print("Not Good!")


if 4 > 8 or 5 > 0:
    print("Yes!")
else:
    print("No!")


if not(5 > 1 or 5 < 10):
    print("kdkdkd")
else:
    print("aaaaa")

