#A decorator is a form of metaprogramming and it can be described as a special type of function that returns a wrapper #function.
import time

def f1(f):
    def f2():
        print("this is before the function call")
        f()
        print("this is after the function call")
    return f2

@f1 
def f3():  # Decorator
    print("this is f3")

f3()

#x = f1(f3)
#x()

#f3 = f1(f3)
#f3()



def elasped_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f"Elasped time: {(t2-t1) * 1000} ms")
    return wrapper

@elasped_time
def big_sum():  # Decorator
    num_list = []
    for num in range(0,1000):
        num_list.append(num)
    print (f"Big sum : {sum(num_list)}")

def main():
    big_sum()

if __name__ =="__main__": main()
