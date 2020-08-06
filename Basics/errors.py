# have captured the error. The other nice thing about this is that by capturing the error, I can handle it intelligently, #and I can go on with my code. I can actually do something else because I know that this didn't work. I could assign a #rational value to x, or I could call a function or whatever, but I've caught that error and now my execution continues. #If I don't catch the error, then it actually stops the execution of my script, so there's a number of different possible 
#errors here

import sys

def main():
    try:
        #x = int('foo') # Value error
        #x = 5/3 # Zero Divison Error
        x = 5/0
    except ValueError:
        print('I caught a value errror')
    #except ZeroDivisionError:
        #print('don\'t divide by zero')
    except: # default catch with the information 
        print(f'unknown error: {sys.exc_info()}')
        #print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('Good job !')
        print (x)
if __name__=='__main__':main()
