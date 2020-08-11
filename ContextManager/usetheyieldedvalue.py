#!/usr/bin/env python3
'''
A context manager has a yield statement that acts as a flow control device and passes control back to the caller. But it also serves another purpose. By putting a value to the right of it, it is actually made available inside the with block of the caller.
'''
from time import time
from contextlib import contextmanager

HEADER = 'this is the header \n'
FOOTER = 'this is the footer \n'

@contextmanager
def new_log_file(name):
    try:
        logname = name
        f = open(logname,'w')
        f.write(HEADER)
        yield f 
    finally:
        f.write(FOOTER)
        print('logFile created')
        f.close()


with new_log_file('logFile') as file:
    file.write('this is the body to that file \n')
