#What's being passed is a reference to the object, and you can change the object in the caller from the function. So this #is important to understand: an integer is not mutable, so it cannot change, so when you assign a new value to an #integer, you're actually assigning an entirely different object to the name. The original integer is not changed, the #name simply refers to a new object. Passing a value to a function acts exactly the same way. A reference to the object #is passed and acts exactly like an assignment. So mutable objects may be changed, and those changes will be reflected in #the caller. 
def main():
    x =[5]
    kitten(x)
    print(f"in main x is {x}")

def kitten(a):
    a[0] = 3
    print("Meow.")
    print(a)

if __name__ == "__main__":main()
