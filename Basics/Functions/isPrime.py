def isPrime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range (100):
        if isPrime(n):
            print(n,end=" ",flush=True)        

list_primes()

n = 6
if isPrime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
    
