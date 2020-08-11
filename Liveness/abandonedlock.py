#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """
'''
Now that we've figured out how to avoid a deadlock between our two philosophers using chopsticks we can return to our routine of eating and philosophizing. I'm ready for another piece of sushi so I'll pick up the first chopstick, then the second one. And I think I left the refrigerator open. - Well that was rude of him. We've entered another form of a deadlock through thread death. If one thread or process acquires a lock and then terminates because of some unexpected reason it may not automatically release the lock before it disappears. That leaves others tasks like me stuck waiting for a lock that will never be released and getting hungry. - Sorry about that. Let's look at some code.
'''

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 100000


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count

    while sushi_count >0 :
        with first_chopstick:
            with second_chopstick:
                if sushi_count >0:
                    sushi_count-=1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
                if sushi_count ==0:
                    print(1/0)

    #while sushi_count > 0:  # eat sushi until it's all gone
        #first_chopstick.acquire()
        #second_chopstick.acquire()
        #try:
            #if sushi_count > 0:
                #sushi_count -= 1
                #print(name, 'took a piece! Sushi remaining:', sushi_count)
        #finally:
            #second_chopstick.release()
            #first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=(
        'Divya', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=(
        'Shree', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=(
        'Ansh', chopstick_a, chopstick_c)).start()
