def main():
    x = dict(Buffy="meow", Zillia="grr", Angel="rawr")
    kitten(**x)
    #kitten(Buffy = "meow", Zillia = "grr",Angel= "rawr")

def kitten(**kwargs):  # **kwargs allows you to have variables with named arguments
    if len(kwargs):
        for k in kwargs:
            print(f"kitten {k} says {kwargs[k]}")
    else:
        print("Meow.")


if __name__=="__main__": main()
