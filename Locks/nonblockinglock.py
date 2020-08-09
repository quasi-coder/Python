#!/usr/bin/env python3
''' Two shoppers adding items to a shared notepad '''

import threading
import time

items_on_notepad = 0
pencil = threading.Lock()

def shopper():
    global items_on_notepad
    name = threading.current_thread().getName()
    items_to_add = 0 
    while items_on_notepad<=20:
        # add item(s) to shared items_on_notepad
        '''
        It will first check to see if there are items to add. And only if the left side of the and is true, it will evaluate the right side, and execute the non-blocking acquire method. If the lock is available, then calling acquire will lock it, and return true. And the program will execute the code between line 20 to 24 to add items to the shared notepad. If the lock was not available, then the non-blocking acquire method will immediately return false, and that thread will execute the else clause from lines 26 to 28 to look for other things to buy.
        '''
        if items_to_add and pencil.acquire(blocking=False): 
            items_on_notepad+= items_to_add
            print(name,'added', items_to_add,'item(s) to notepad.')
            items_to_add = 0
            time.sleep(0.3) # time spent writing 
            pencil.release()
        else: # else look for other things to do 
            time.sleep(0.1) # time spent searching
            items_to_add+=1
            print(name,'found something else to buy.')

if __name__=='__main__':
    divya = threading.Thread(target=shopper, name = 'divya')
    shree = threading.Thread(target=shopper, name = 'shree')
    start_time = time.perf_counter()
    divya.start()
    shree.start()
    divya.join()
    shree.join()
    elapsed_time = time.perf_counter() - start_time
    print('Elapsed Time: {:.2f} seconds'.format(elapsed_time))




