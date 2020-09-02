# deque objects are like double-ended queues

'''
Pronounced as "deck" sort of a hybrid object between a stack and a queue. In fact, the name itself basically means double-ended queue and they are designed to be memory-efficient.

Deques can be initialized to be either empty or get their initial data from an existing, iterable object, and they can also be specified to have a maximum length. To add data to a deque, you use either the append or append left methods to add items onto the end or the beginning, and similarly, items can be removed using either pop or pop left. Deques also support a rotate function, which can operate in either direction. The rotate function takes a parameter indicating how many items to rotate and defaults to one, so positive numbers will rotate to the right, while negative numbers will rotate to the left,
'''

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    d.rotate(1)
    print(d)


if __name__ == "__main__":
    main()
