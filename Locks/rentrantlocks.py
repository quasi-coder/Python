#!/usr/bin/env python3
''' Two shoppers adding garlic and potatoes to a shared notepad '''

import threading

garlic_count = 0
potato_count = 0
'''
a reentrant lock that can be acquired multiple time before being released.
difference between regular lock and Rlock in Python is that the regular lock can be released by different threads than the one that acquired it, but the reentrant lock must be released by the same thread that acquired it.And of course, it must be released by that thread as many times as it was acquired before it will be available for another thread to take.
'''
pencil = threading.RLock()

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count+=1
    pencil.release()


def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()
    pencil.release()

def shopper():
    for i in range(10_000):
        add_garlic()
        add_potato()

if __name__ =='__main__':
    divya = threading.Thread(target=shopper)
    shree = threading.Thread(target=shopper)
    divya.start()
    shree.start()
    divya.join()
    shree.join()
    print('We should buy', garlic_count,'garlic.')
    print('We should buy', potato_count,'potatoes.')
