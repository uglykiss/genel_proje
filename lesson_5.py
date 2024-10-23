# loop list
mylist = ["kemal", "bjk","ömer"]

for x in mylist:
     print(x)

# range(), len()
for i in range(len(mylist)):
     print(mylist[i])

x = 5
print(x)

# range(), len()
for i in range(1,2):
     print(mylist[i])


# while loop
mylist = ["kemal","mehmet","sıla","ömer"]
i = 0
while i < len(mylist):
     print(mylist[i])
     i = i + 1

###########################################
# list comprehension

[print(x) for x in mylist]

#example
mylist = ["kemal","mehmet", "sıla","ezgi"]
newlist = []

for x in mylist:
     if "a" in x:
          newlist.append(x)
print(newlist)

# append = ekle

# list comprehension example
newlist = [x for x in mylist if "a" in x]
print(newlist)

# EĞER kemal hariç diğerleri çağırmak istiyorsam
newlist = [x for x in mylist if x != "kemal"]
print(newlist)

# iterable - range
newlist = []
newlist = [x for x in range(9)]
print(newlist)


newlist = []
newlist = [x for x in range(1,7)]
print(newlist)

#example
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in mylist]
print(newlist)

# Andrew NG scientist

# example
fruits = ["apple","orange", "cherry","peanut", "banana"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# sort list - alphabetically
fruits.sort()
print(fruits)

# sort numbers
numbers = [28, 11, 89, 57, 66]
numbers.sort()
print(fruits)

# sort descending
fruits.sort(reverse = True)
print(numbers)

# case intensitive sort
# sort method is case sensitive
thislist = ["apple","Kiwi","cherry","peanut","Orange"]
thislist.sort()
print(thislist)

# perfore a case-insensitive sort of the list
thislist.sort(key=str.lower)
print(thislist)


# copy a list
mylist = thislist.copy()
print(mylist)

# another way to make a copy is to use list() method
mylist = list(thislist)
print(mylist)

# example
mylist = thislist[:3]
print(mylist)


# python join list
numbers = [5, 6, 2, 1, 4, 3]
list3 = thislist + numbers
print(list3)

# append() method
for x in numbers:
     thislist.append(x)
print(thislist)


# extend()
thislist.extend(numbers)
print(thislist)

# tuples
mytuple = ["apple","Kiwi","cherry"]

#unchangeable
#ordered
# tuples are written with round brackets
# tuple item are index 0, the second index
# allow dublicates

mytuple = ("a","b","c","d","e")
print(mytuple)

# tuple length
print(len(mytuple))

#devamını yazamıyorum.





