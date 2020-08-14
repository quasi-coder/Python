import pickle
'''
The pickle module allows us to serialize and de-serialize Python objects. In other words, it can transform an object into a tech stream before saving it into a file. The reverse is also possible and referred to as de-serializing. 

Here we can create a constructor that sets the initial state of an originator object to none by typing self._state = None

memento object, the name of the method is create_memento. Type "return pickle.dumps(vars(self))". All this does is using the pickle module method called dumps and turns an originator object into a character stream. By the way, the VARS method is a built in Python function that returns a dictionary containing all the attribute value pairs of an object.

The next method set_memento allows us to restore the previous state of an object. We first de-serialize our memento object, which provides the snapshot of the previous state of the object. Type "previous_state = pickle.loads(memento)". Then we use the VARS function to wipe out the current state. vars(self).clear(). Finally, we replace the current state with the previous state. vars(self).update(previous_state)
'''

class Originator:
    def __init__(self):
        self._state = None

    def create_memento(self):
	    return pickle.dumps(vars(self))
   

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear
        vars(self).update(previous_state)	

def main():
	originator = Originator()
    
    #We then print the current state of the originator.

	print(vars(originator))

	memento = originator.create_memento()

	originator._state = True

	print(vars(originator))

	originator.set_memento(memento)

	print(vars(originator))


if __name__ == "__main__":
	main()
