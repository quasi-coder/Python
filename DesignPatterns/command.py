'''
There are situations when it's necessary to wrap a request in an object. In an object oriented language like Python, the request comes in the form of a method. The command pattern addresses this need and provides guidance on how to best build an object whose sole purpose is to package a method that can be easily passed around. 
To reiterate, the concrete commands are our mechanism for invoking an action on a receiver object. It implements the execute interface of the command class. A client object initiates a transaction involving a concrete command by creating a concrete command object and deciding who its receiver is. The invoker class is responsible for holding onto various command objects and telling them to take an action on a receiver when the time is right. 
'''

class Command:
    '''
    The only method the command class has is the execute method that serves as an interface used to execute various self contained operations. It doesn't do anything by itself.
    '''
    def execute(self):
        pass

'''
 let's define some concrete command classes.
'''
class Copy(Command):
    def execute(self):
        print('Copying ...')

class Paste(Command):
    def execute(self):
        print('Pasting ...')

class Save(Command):
    def execute(self):
        print('Saving ...')
'''
The invoker class creates multiple concrete command objects and stores them in a list.
That is it stores a sequence of actions to be taken, in a single container, so that a user doesn't have to execute the actions, individually, but can trigger them with a one step process, like clicking on a macro button
'''
class Macro:
    def __init__(self):
        self.commands = []
    def add(self,command):
        self.commands.append(command)
    def run(self):
        for o in self.commands:
            o.execute()

def main():
    macro = Macro()
    macro.add(Copy())
    macro.add(Paste())
    macro.add(Save())
    macro.run()

if __name__=='__main__':main()


