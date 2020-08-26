import myModule
import datetime

# myModule.greeting("Rith")

# a = myModule.person1["age"]
# print(a)

getTime = datetime.datetime.now()
print(getTime.year, getTime.strftime("%a"), getTime.month)