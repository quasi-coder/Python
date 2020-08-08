import sys 
import os
import random
import datetime
def main():
    v1 = sys.version_info
    v2 = sys.platform
    v3 = os.name
    v4 = os.getenv('PATH')
    v5= os.urandom(25).hex()
    v6 = random.randint(1,1000)
    v7 = list(range(25))
    random.shuffle(v7)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day)
    print(v1)
    print('Python version is {}.{}.{}'.format(*v1))
    print(v2)
    print(v3)
    print(v4)
    print(v5)
    print(v6)
    print(v7)
    

if __name__=='__main__':main()
