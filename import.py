import myModule
import datetime
# import classObject

myModule.greeting("Rith")

a = myModule.person1["age"]
print(a)

getTime = datetime.datetime.now()
print(getTime.year, getTime.strftime("%a"), getTime.month)
print(getTime.month, getTime.strftime("%A"), getTime.year)
