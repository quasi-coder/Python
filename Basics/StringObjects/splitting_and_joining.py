s = 'This is a long string with bunch of words in it.'
l = s.split()
s2 = ':'.join(l)
print(s2)
print(s.split())
print(s.split('i'))
s1 = ''' This is a 
        long string with bunch of words 
        
        
        in it'''
print(s1.split())
