class Cooler():
    def __init__(self, nCooler, dCooler):
        self.nameOfCooler = nCooler
        self.dateOfCooler = dCooler
    def printCooler(self):
        print("The cooler is", self.nameOfCooler, "and state date for use is", self.dateOfCooler)


class Home(Cooler):
    pass
coolerHome = Home("Teal", "8/28/2020")
coolerHome.printCooler()

class School(Home):
    def __init__(self, nCooler, dCooler):
        super().__init__(nCooler, dCooler)
        self.eCooler = "9/01/2020"
endCooler = School("Red", "8/28/2020")
print(endCooler.eCooler)


class Car(Cooler):
    def __init__(self, nCooler, dCooler, pCooler):
        super().__init__(nCooler, dCooler)
        self.priceCooler = pCooler
    def diplayPrice(self):
        print(self.nameOfCooler, self.dateOfCooler, self.priceCooler)

detailCooler = Car("Blue", "8/28/2020", 70)
print(detailCooler.diplayPrice())

list = ["item1", "item2", "item3"]
for showItem in list:
    print(showItem)

   