#
# Example file for working with functions
#

# define a basic function
def func1():
  print("I am a function")

# function that takes arguments


def func2(arg1, arg2):
  print(arg1, " ", arg2)

# function that returns a value


def cube(x):
  return x*x*x

# function with default value for an argument


def power(num, x=1):
  result = 1
  for i in range(x):
    result = result * num
  return result

#function with variable number of arguments, we can combine the variable arguments with the fixed args but in that case variable args should always be at the end


def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result


# function is being called directly and executes the contents of the function
func1()
#function is also being called inside the print function,
#so the output is the same as in the first case, but then the outer print statement executes,
#and since our function doesn't return a value,
#Python evaluates the return value to be the Python constant of none,
#and then just prints the string representation of that.
print(func1())
#function itself is not being executed at all since we're not including those little parentheses that would call the function.
#We're just printing the value of the function definition itself,
#which evaluates to this string that you see here.
#This just demonstrates that functions themselves are objects that can be passed around to other pieces of Python code.
print(func1)

func2(10, 20)
print(func1)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))
