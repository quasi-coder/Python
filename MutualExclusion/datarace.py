#!/usr/bin/env python3
''' Two shoppers adding items to a shared notepad '''

'''Since a data race only occurs when at least one of the concurrent threads is modifying the value of a memory location, pay close attention to anywhere you use an assignment operation, or an operator like the plus equal incrementor that changes a variable's value. If there's a potential for two or more threads to access that variable and make changes to it, then you'll almost certainly need to use some sort of mechanism to protect it '''

import threading

garlic_count = 0

def shopper():
    global garlic_count
    for i in range(10_000_000):
        garlic_count+=1

if __name__=='__main__':
    divya = threading.Thread(target=shopper)
    shree = threading.Thread(target=shopper)
    divya.start()
    shree.start()
    divya.join()
    shree.join()
    print('We should buy', garlic_count,'garlic.')
