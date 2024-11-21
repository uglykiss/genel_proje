print("selam buse")
a = 10
print(a)

#ctrl d double it
#ctrl q quick info
#f2 tuşu bir sonraki hataya geçiyor

a = Moby Dick
sayfa = 195
print(bu kitabın ismi ( isim ) ve ( sayfa ) sayfa uzunluğundadır.)
print(a)

import random
print(random.randrange(1,10))

a = "kemal"
print(len(a))

b = "hello ai"
print(len(b))

txt = "kemal has a dog"
print("dog" in txt)


txt = "kemal has a dog"
print("cat" in txt)

x = "hello class!"
print(x[0:8])
print(len(x))

x = "          kemal      gunay            "
print(x.strip())
print(x)
p = "merve"
print("merhaba benim adım 'p'")

y = "hello class!"
print(x[:7])


print(x[2:])
print(x[-5:-2])

a = "kemal"
print(a.replace("k", "c"))

x = "kemal gunay, mert uzuner, eren kocaömer"
print(x.split(","))
print(x)

a = "qasim"
b = " kazmi"

c = a + b
print(c)

age = "18"
name = "My name is Bengisu, I am" + age
print(name)

age = "18"
name = f"My name is Bengisu, I am {age}"
print(name)

price = 59
txt = f"the price is {price:.7f} dollars"
print(txt)


price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)

txt = f"the price is {20 + 60} dollars"
print(txt)

txt = "I am a lecturer.'kemal' "
print(txt)

print(10 < 9)

a = 100
b = 20

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("hi"))

print(bool(15))

def myFunction():
    return True

print(myFunction())

x = 100
print(isinstance(x, str))

b = "GFG"
print(type(x))

x  =+ 3
print(x)

x = 100
x += 3
print(x)

x = 100
x *= 3
print(x)

x = 3
y = 3
print(x == y)

x = 3
y = 3
print(x != y)



print(x > 1 and x < 4 and x < 10)

print(x < 4 or x > 10)

x = 3
print(not(x < 5 and x < 10))


x = 3
y = 3
print(x is not y)

x = ("kemal", "eren", "kuzey", "halil")

print(x)
print(x[0])
print(x[3])

y = ["kemal", "eren", "kuzey", "halil", "kemal"]
print(y)


print(len(y))

list=(("kemal", "eren", "kuzey", "halil"))
list4 = list
print(list4)

list4 = list(("kemal", "eren", "kuzey", "halil"))
print(list4)

list1 = ["kemal", "eren", "kuzey", "halil"]
print(list1[-1])

list5 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
print(list5[2:5])

list5 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
print(list5[:4])
print(list5[1:4])
print(list5[-3:])


list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[0] = "bengisu"
print(list6)

list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[1:2] = ["mustafa", "yusuf"]
print(list6)

list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[1:4] = ["abdurahman"]
print(list6)

list6 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list6[1:2] = ["mustafa", "eren"]
print(list6)

list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.insert(2, "abdurahman")
print(list7)

list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.insert(3, "melike")
print(list7)

list7 = ["kemal", "eren", "kemal", "halil", "mete", "omer"]
list7.append("melike")
print(list7)

list8 = ["kemal", "eren", "kuzey", "halil"]
list9 = ["banana", "orange"]
list8.extend(list9)
print(list8)

list8 = ["kemal", "eren", "kuzey", "halil"]
mytuple = ("banana", "orange")
list8.extend(mytuple)
print(list8)

list7 = ["kemal", "eren", "kuzey", "halil", "mete", "omer"]
list7.remove("kemal")
print(list7)

lists = ["yastık", "got", "steteskop"]
lists.remove("got")
print(lists)

mylist = ["kemal", "mehmet", "sıla", "sevi"]

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(len(mytuple))

thistuple = ("kemal",)
print(type(thistuple))

tuplelistem = ("kemal", 99, True, 22, "kedi")
print(tuplelistem)
print(type(tuplelistem))

mytuple = tuple(("kemal", "mehmet"))
print(mytuple)

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[3])

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[-2:])

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[2:5])

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[:3])

mytuple = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(mytuple[3:])

x = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
y = list(x)
print(type(y))

x = ("apple", "apple", "kiwi", "cheery", "peanut", "orange")
print(type(x))

x = ("apple", "orange")
y = ("peanut",)
x += y
print(x)

mylist = ["kemal", "mehmet", "sıla", "sevi"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

mylist = ["kemal", "mehmet", "sıla", "sevi"]

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

for i in range(1,3):
    print(mylist[i])

mylist = ["kemal", "mehmet", "sıla", "ezgi"]
[print(x) for x in mylist]

mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = []

for x in mylist:
    if "a" in x:
        newlist.append(x)

print(newlist)

mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x for x in mylist if "a" in x]
print(newlist)

mylist = ["kemal", "mehmet", "sıla", "ezgi"]
newlist = [x for x in mylist if x != "kemal"]
print(newlist)

newlist = []
newlist = [x for x in range(9)]
print(newlist)

fruits = ["apple", "kiwi", "cheery", "peanut", "banana"]
fruits.sort(reverse = True)
print(fruits)

thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
mylist = thislist[:3]
print(mylist)

thislist = ["apple", "Kiwi", "cheery", "peanut", "Orange"]
numbers = [5, 6, 2, 1, 4, 3]

for x in numbers:
    thislist.append(x)

print(thislist)