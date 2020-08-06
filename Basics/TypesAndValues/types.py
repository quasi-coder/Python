from decimal import *

a = Decimal('.10')
b = Decimal('.30')

x = a + a + a - b
print("x is {}".format(x))
print(type(x))

y = [1,2,3,4]
y[0] = 98
for i in y:
    print("i is {}".format(i))

z = (1,"two",3.0,[4,"string"],5)
d = (1, "two", 3.0, [4, "string"], 5)
#z[0] = 23
for i in z:
   print("i is {}".format(i))
   print(type(i))

#print the different ids of two objects
print(id(z))
print(id(d))  

# Since only single object is there for  literal number '1', so the ids are same 
print(id(z[0]))
print(id(d[0]))

if z[0] is d[0]:
    print("yep")
else:
    print("nope")

if z is d:
    print("yep")
else:
    print("nope")

if isinstance (z,tuple):
    print("yes")
else:
    print("nope")

q = range(5,50,5) 
 #range is also immutable like tuple
for i in q:
    print("i is {}".format(i))


w = { "one" : 1, "two" : 2, "three" : 3}
w["three"] = 42
for i in w:
    print("i is {}".format(i))

for k,v in w.items():
   print("key: {}, value: {} ".format(k,v))
