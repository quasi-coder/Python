import platform

def main():
    message()

x = 'Hello World "{1:<09}" "{0:>09}"'.format(8,9)
y = 10
a = 42
b = 73
r = f'I am f string ====> {y} {a}'
print(r)
def message():
    print("This is python version {}" .format(platform.python_version()));print("I am {}".format(x));print("Just Checking %d" % y)
    print(f"hehaww. {y}")
    if False:
        print("I am False")
    else:
        print("not True")


if a < b:
    z= 112
    print('a < b: a is {} and b is {}'.format(a, b))
elif a > b:
    print('a > b: a is {} and b is {}'.format(a, b))
elif a == b:
    print('a == b: a is {} and b is {}'.format(a, b))
else:
    print("do something")

print("Print value of z as block does not define scope is . {}".format(z))

words = ['one','true','three','four','five']

n = 0

while(n<5):
    print(words[n])
    n +=1

for i in words:
    print(i)

def function(n =1):
    print("Result of function method +++++ {}".format(n))
# Takes default value n =1
function()
# Takes passed value
function(42)

c = function(17)
# Since function method does not return any specific value so default is None
print(c)

def me(n =1):
    return n * 2 

print(me())

#By having this conditional statement at the bottom that calls main, it actually forces the interpreter to read the entire script before #it executes any of the code. This allows a more procedural style of programming, and it's because Python requires that a function is #defined before it's called.
if __name__ == '__main__': main()

