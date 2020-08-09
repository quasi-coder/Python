#!/usr/bin/env python3
''' Two threads cookig soup '''

import threading 
import time

class ChefDivya(    threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print('Divya started & waiting for a sausage to thaw...')
        time.sleep(3)
        print('Divya is done cutting sausage')

# main thread
if __name__=='__main__':
    print('Shree started and requesting Divya\'s help.')
    divya = ChefDivya()
    print(' is Divya alive?', divya.is_alive())
    print('Shree tells Divya to start')
    divya.start() 
    print(' is Divya alive?', divya.is_alive())
    print('Shree continues cooking soup')
    time.sleep(0.5)
    print(' is Divya alive?', divya.is_alive())
    print('Shree patiently waits for Divya to finish and join...')
    divya.join()
    print(' is Divya alive?', divya.is_alive())
    print('Divya and Shree are both done!')
    

