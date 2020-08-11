#!/usr/bin/env python3

# list comprehension
'''
 A list comprehension is simply an expression with a set of brackets which evaluates to a list. 
'''
newlist = [n for n in range(10) if n % 2 ==0]
print(newlist)

#generator expression

''' A generator expression evaluates to a generator object rather than a list.
    It only evaluates one item at a time without storing any sequence in memory.   
'''
even_integers = (n for n in range(10) if n % 2 ==0)
print(list(even_integers))


# list of mixed format numbers 
numbers = [7,22,4.5,99.7,'3','5']

#convert numbers to integers using expression
integers = (int(n) for n in numbers) 
print(list(integers))   

names_list = ['Divya', 'Shree', 'Ansh']
reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))
print(list(reverse_uppercase))


