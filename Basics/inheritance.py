#Why would you sometimes want to use keyword arguments in a class constructor
#You can provide the constructor arguments in any order.

class Animal:

    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name'] 
        if 'sound' in kwargs:
            self._sound = kwargs['sound'] 

    #Getters And Setters
    def type(self, t=None):
        if t:
            self._type = t
        try: 
            return self._type
        except AttributeError: 
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    # To string representation of the object
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs) 

    def kill(self,s):
        print(f'{self.name()} will now kill all {s}!')


def main():
    a0 = Kitten(name='fluffy', sound='rwar')
    a1 = Duck(name='donald', sound='quack')
    a0.kill('humans')
    print(a0)
    print(a1)


if __name__ == '__main__':
    main()
