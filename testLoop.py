class Numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myClass = Numbers()
myIter = iter(myClass)

for x in myIter:
  print(x)
  
print("==================")

for i in range(1,20,2):
    print (i)

print("==================")

for i in range(11):
    for j in range(i):
        print (i, end=' ')
    print()