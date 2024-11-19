import module;
a = ["apple", "banana", "cherry"] #list
b = ("apple", "banana", "cherry") #tuple
c = range(6)  #range
d = {"name" : "John", "age" : 36}  #dict
e = {"apple", "banana", "cherry"} #set
f = frozenset(["apple", "banana", "cherry" , "apple"])
g = b"Hello"
h  = bytearray(5)
i  = memoryview(bytes(5))
j = None
# print(b[2:])
# print(b.strip())
# print(b.strip().split(","))
# a[0] = "mango"
# age = 36
# price = 59
# txt = f"The price is {20 * 59} dollars"
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

class TextContainer:
    def __init__(self, text):
        self.text = text  # Store the string

    def __len__(self):
        return len(self.text)  # Return the length of the string

# Usage
# container = TextContainer(a)
# print(len(a))
# Output: 13, the length of "Hello, world!"


# for item in zip(a,c):
#     print(item)

# if type(d) == dict:
#     for key,value in d.items():
#         print( key,"=>",value)
#
# if type(b) == tuple:
#     for value in b:
#         print(value)

# for xy in range(10):
#     print(xy)

age = 30
agetext = f"My age is {age}";
# print(agetext.lower().find("s"))
# print( 5 // 2)

thislist = ["apple", "banana", "orange", "kiwi", "mango", "cherry"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist.append("Ashish")
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# thislist.clear()
# print(thislist)
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# newlist = []

# for x in thislist:
#   if "a" in x:
#     newlist.append(x)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
mylist = thislist.copy()
# print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

index = list1.index("c")
# print(index)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

arrayex = [10,True,"Ashish" , 29]

# print(arrayex)

class Person:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def sum(self,addtional = 0):
      return self.x + self.y + addtional

class Student(Person):
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def minus(self , addtional = 0):
        return self.x - self.y - addtional
p1 = Student(25, 50)

print(p1.minus(-10))

# print(a[0])
# print(b[0])
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)
# print(j)
global x
x = 300

def myfunc():
  x = 500
  def myinnerfunc():
    pass
  myinnerfunc()
  print(x)

myfunc()

print(x)

x = lambda a : a + 10 if a > 0 else 0
print(x(0))

print(module.name("Zeel"))