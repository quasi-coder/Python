def main():
    x = ("meow", "grr", "purr")
    kitten(*x)
    #kitten("meow","grr","purr")
    #kitten()

def kitten(*args): # variable length argument list treated as sequence in tuple
    if len(args):
        for s in args:
            print(s)
    else:
        print("Meow.")

if __name__ == "__main__": main()
