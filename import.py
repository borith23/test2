import myModule
import datetime
# import classObject

myModule.greeting("Rith")

a = myModule.person1["age"]
print(a)



getTime = datetime.datetime.now()
#Display real time 
print(getTime.year, getTime.strftime("%a"), getTime.month)
print(getTime.month, getTime.strftime("%A"), getTime.year)



i = ["apple", "banana", "cc"]
#display item array i from -3 to -1 
print(i[-3:-1])

#add aa to first item of array i
i[0] = "aa"
print(i)

#loop to show result of array i
for k in i:
    print(k)

#add bb to array i
i.append("bb")
print(i)
