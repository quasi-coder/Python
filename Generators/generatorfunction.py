#!/usr/bin/env python3
""" Generators are the best way to iterate through large or complex data sets, especially when performance and memory are of concern.
The generator function returns a generator object and that generator object will yield the values. Now, you may have heard that generators yield rather than return, which is true. 
"""

def even_integers_function(n):
    for i in range(n):
        if i % 2 == 0:
            yield i  # return a generator object

print(list(even_integers_function(10)))
