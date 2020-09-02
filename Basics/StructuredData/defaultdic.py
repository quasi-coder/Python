# Demonstrate the usage of defaultdict objects
'''
 default dict is really useful, but you have to be careful when you use it, because any key that you didn't explicitly add to the dictionary, will be assigned a default value, when you try to access it. So, if you have a situation where the fact that a key is missing from the dictionary is an important indicator, then default dict is probably not the right collection to use.
'''

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)

    # use a dictionary to count each element with lambda
    #I'll give default dict a lambda with no, argument, and just give it the value 100. So now each key will start off at #100.
    #fruitCounter = defaultdict(lambda: 100)

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
