#!/usr/bin/env python3
''' Two shoppers adding items to a shared notepad '''

import threading
import time

garlic_count = 0
pencil = threading.Lock()


def shopper():
    global garlic_count
    
    for i in range(5):
        print(threading.current_thread().getName(),'is thinking.')
        time.sleep(0.5)
        '''
        We've minimized the critical section to only protect the part of this program that truly requires mutual exclusion. i.e before incrementing the garlic count and after that.
        '''
        pencil.acquire()
        garlic_count += 1
        pencil.release()

if __name__ == '__main__':
    divya = threading.Thread(target=shopper)
    shree = threading.Thread(target=shopper)
    divya.start()
    shree.start()
    divya.join()
    shree.join()
    print('We should buy', garlic_count, 'garlic.')
