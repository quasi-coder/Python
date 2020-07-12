#Find the greatest common denominator of two numbers
#Using Elucid's algorithm a = b ; b = r till b == 0
def gcd(a, b):
    while(b!=0):
        t = a
        a = b
        b = t % b
    return a    


#try out the function with few examples
print(gcd(60, 96)) # should be 12
print(gcd(20,8)) #should be 4