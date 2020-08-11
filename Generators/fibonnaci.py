#!/usr/bin/env python3
''' It's even the basis of the Fibonacci search technique, which is a method of searching assortative array. '''
def fibonnaci_gen():
    a,b = 1,1
    yield a 
    yield b 
    while True:
        a,b = b, a+b
        yield b
g = fibonnaci_gen()
v1 = next(g)
v2 = next (g)
v3 = next (g)
print (v1)
print(v2)
print(v3)
next(g)
fibs = [next(g) for i in range(5)]
print(fibs)