print('Hello World !'.upper())
print('Hello World !'.lower())
print('Hello World !'.capitalize())
print('Hello World !'.title())
print('Hello World !'.swapcase())
#so if I use like a German sharp S here, and we run this, you notice that comes out to a lowercase ss. Where if I just do #this in lower, and run it, you notice it does not lowercase the German sharp S. And so that's useful for words like #strasse, the name of a street in German. And if I make that casefold, then it spells it in lowercase.
print('Hello World ! ß. '.casefold())

s1 = 'Hello World !'
# Strings are immutable, any operation on them creates new object
s2 = s1.upper()
s3 = 'this is another string'
s4 = s1 + s3
# Literal strings can be concatenated like this
s5 = 'this string ' ' that string'
print(id(s1))
print(id(s2))
print(s4)
print(s5)
