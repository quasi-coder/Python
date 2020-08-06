class Animal:
    #class constructor
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound

    #class constructor with kwargs

    #def __init__(self, **kwargs):
        #self._type = kwargs['type']
        #self._name = kwargs['name']
        #self._sound = kwargs['sound']

    #class constructor with default values

    #def __init__(self, **kwargs):
        #self._type = kwargs['type'] if 'type' in kwargs else 'fluffy'
        #self._name = kwargs['name'] if 'name' in kwargs else 'kitten'
        #self._sound = kwargs['sound'] if sound in kwargs else 'rawr'


    #getters
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
    
def print_animal(o):
    if not isinstance(o,Animal):
        raise TypeError("print_animal(): requires an Animal")
    print("The {} is named \"{}\" and says \"{}\" .".format(o.type(),o.name(),o.sound()))

def main():
    #a0 = Animal(type="kitten", name="fluffy", sound="rwar") # for kwargs constructor
    #a0 = Animal() # for default values constructor
    a0 = Animal("kitten","fluffy","rwar")
    a1 = Animal("duck","donald","quack")
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal("velociraptor","managers","hello"))

if __name__ == "__main__":main()

    

