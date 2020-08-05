#we notice that it prints 3 in the kitten function, and x is still five in the main function after the function call, and #so this is what they call in the Python documentation call by value, and in most call-by-value languages, when you pass #a variable to a function, the function operates on a copy of the variable, so the value is passed, but not the object #itself, and this is an important distinction because if the object were actually passed, then if I were to change it at #line 9, it would also change there in main

def main():
    x =5
    print(id(x))
    kitten(x)
    print(f"in main: x is {x}")

def kitten(a):
    print(id(a))
    a =3
    print(id(a))
    print("Meow.")
    print(a)

if __name__ == "__main__":main()
