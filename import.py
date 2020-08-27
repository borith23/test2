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

#change first item in array to aa  
i[0] = "aa"
print(i)

#loop to show result of array i
for k in i:
    print(k)

#add bb to array i
i.append("bb")
print(i)

#add dd to first item in array i
i.insert(0, "dd")
print(i)

k = 5
l = 5
print(k is l)


array = ["na", "ma", "ka"]
array.remove("ma") #remove item ma from array
print(array)

array.pop() #use pop() to remove last item from array
print(array) 

