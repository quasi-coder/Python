a = True
b = False

x = ("bear", "bunny", "tree", "sky", "rain")
y = "bear"

#For AND to be satisfied both have to be true
if a and b :
    print("expression is true")
else:
    print("expression is false")

#For OR  to be satisfied one have to be true
if a or b:
    print("expression is true")
else:
    print("expression is false")

# Urinary not, because b is false so expression becomes true
if not b:
    print("expression is true")
else:
    print("expression is false")

# Value in set
if y in x:
    print("expression is true")
else:
    print("expression is false")

#Value not in set
if y not in x:
    print("expression is true")
else:
    print("expression is false")

# Strings are not mutable so even if you have two literal strings with exactly the same variable, there is no reason to  #carry around two separate objects 
# Same object identity  
if y is x[0]:
    print("expression is true")
else:
    print("expression is false")

#Not same object identity
if y is not x[0]:
    print("expression is true")
else:
    print("expression is false")
