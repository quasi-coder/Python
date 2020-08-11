#!/usr/bin/env python3
''' 
A context manager is a Python object that is able to act as a control structure when used after the "with" statement. They manage the context for a caller. That means performing some kind of set up, yielding control back to the caller, and then wrapping up when the caller is done.
For a Python object to be able to act as a context manager it must implement the methods "enter" and "exit." Which an open file object happens to do.

Remember those three steps that a context manager takes? Setting up a context, giving control back to the caller, and wrapping up once the caller is done? Those are accomplished with three key words, "try", "yield" and "finally."



The context manager function takes an object as an argument. When called, the first thing that will happen is it will increment the property called some property by one. Next, the yield statement causes this context manager to pause and yield control back to the color to do a particular action or actions. When the color is finished with that predetermined action the context manager will go ahead and wrap-up by executing the functionality in the finally block. In this case, it will decrement the property called some property bringing it back to it's original value. Context managers allow easy execution of setup code and wrap-up code with the help of Python generators and the context manager decorator.

'''

# increments some_property by 1
from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property +=1
        yield
    finally:
        #wrap up
        obj.some_property -=1

class Some_obj(object):
    def __init__(self,arg):
        self.some_property = arg


obj = Some_obj(5)
print(obj.some_property)

with simple_context_manager(obj):
    print(obj.some_property)

'''
What happened is that the try block was executed first meaning some property was incremented by one. Then control was yielded back to the color and the code in the with block was executed which is what we see here. But how do we know if the finally code was executed? If we print out object dot some property now, it should be back where it was. We can see it, object dot some property is back at five again.
'''
print(obj.some_property)

