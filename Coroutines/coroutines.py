#!/usr/bin/env python3

'''
While a generator is something that produces values each time it's called, a coroutine is something you constantly give things to that may or may not return anything. Instead, it takes what is passed to it and does something with it. What you give it and what it does with it are completely up to you. It's important to understand the differences between coroutines and generators thoroughly and what they are capable of. Unlike generators, coroutines are not for iterating over sequences

A coroutine is designed to repeatedly send input to it, process that input by following the logical path that you program it to follow, and stop when it reaches the yield statement. 

'''


def counter(string):
    count = 0
    try:
        while True:
            item = yield # Paused at yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print (item)
                else:
                    print ('No Match')
            else:
                print ('Not a string')
    except GeneratorExit:
        print (count)


c = counter('India')
'''
I must either call next or send a None value so that the coroutine object has advanced to the point of being suspended at the yield point
'''
next(c)
c.send('Cali')
c.send('nia')
c.send('Indi')
c.send(12)
