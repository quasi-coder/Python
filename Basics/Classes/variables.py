#Encapsulation is one of the major benefits of object oriented programing. If my variables are encapsulated, that means #that they belong to the object, and not to the class. This variable here, this x variable is not encapsulated and so it #exists, it's exactly the same object in every instance of the class. And every object that's created by the class, #because it only exists in the class. So that makes it not encapsulated. As a general rule, except for things like #constants that you are never going to change, and those should be immutable not mutable. You're really never going to #want to put mutable data in the class.

class Animal:
    #Class variable
    x = [1,2,3]
    def __init__(self, **kwargs):
        #Object variables
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    #Getters And Setters
    def type(self, t=None):
        if t:
            #Python doesn't have private variables so we have convention to put '_' which indicates it's private
            self._type = t 
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    # To string representation of the object
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'
def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a0._name = 'Joe'  # Directly changed the name (private variable)
    print(a0._name) #print(a0.name()) gives the same result
    print(a0.x)
    a1.x[0] = 5
    print(a0.x)  # Now the list has 5 in it, we changed it using a1 but it reflected in a0 too as it is a class variable
    print(a0) 
    print(a1)

if __name__ == '__main__':
    main()
