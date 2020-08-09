#!/usr/bin/env python3
''' Thread that wastes CPU cycles '''
import os 
import threading

# a simple function that wastes CPU cycle forever
def cpu_waster():
    while True:
        pass

#display information about this process
print('\n Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)

print('\nStarting 4 CPU Wasters...')
for i in range(4):
    threading.Thread(target=cpu_waster).start()

#display information about this process
print('\n Process ID : ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)


