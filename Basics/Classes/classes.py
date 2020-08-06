#
# Example file for working with classes
# self is not a keyword.
#the first argument is self, which is a reference to the object, not the class, to the object. And so, when an object is #created from the class, self will reference that object. And then everything that references anything defined in the #class is dereferenced off itself to get the instantiated object version of it. And the period operator is used to #dereference the object. And the same is true outside of the class.

# Class methods have 'self' specified as their first argument. Given this case, below statement is true
#The argument is automatically filled when the method is called.

class baseClass():
  sound = "Quaack!"
  walking = "Walking like a duck."
  def method1(self):
    print("Calling baseClass method1"+"   ----->"+self.sound+"    +++++++"+self.walking) 

  def method2(self, someString):
    print("Calling baseClass method2: " + someString)


class childClass(baseClass): 
  def method2(self):
    print("Calling childClass method2")

  def method1(self):
    baseClass.method1(self)
    print("Calling baseClass method1 from childClass method1 in the prior statement")


def main():
  c = baseClass()
  c.method1()
  c.method2("This is a baseClassString")
  c2 = childClass()
  c2.method2()
  c2.method1()


if __name__ == "__main__":
  main()
