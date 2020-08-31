my_list = [1, 2, 3, 4, 5]

lengthOfArray = len(my_list)
i = 0

while i < lengthOfArray:
  print(my_list[i])
  i += 1

print("===============")
print(len(my_list))
print("===============")
[print(i) for i in my_list]
print("===============")


for x, val in enumerate(my_list):
  print(x, ",", val)

array = ["apple", "banana"]
my_iter = iter(array)
print(next(my_iter))

listColor = "Black"
color_iter = iter(listColor)
print(next(color_iter))

for findColor in listColor:
  print(findColor)

