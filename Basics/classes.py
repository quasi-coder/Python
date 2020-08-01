#
# Example file for working with classes
#

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
