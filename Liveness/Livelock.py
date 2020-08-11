#!/usr/bin/env python3
''' 
 livelock looks similar to a deadlock in the sense that two threads are blocking each other from making progress, but the difference is that the threads in a livelock are actively trying to resolve the problem. A livelock can occur when two or more threads are designed to respond to the actions of each other. Both threads are busy doing something, but the combination of their efforts prevent them from actually making progress and accomplishing anything useful. The program will never reach the end. The ironic thing about livelocks is that they're often caused by algorithms that are intended to detect and recover from deadlock. If one or more process or thread takes action to resolve the deadlock, then those threads can end up being overly polite and stuck in a livelock. To avoid that, ensure that only one process takes action chosen by priority or some other mechanism, like random selection. 

'''

import threading
import time
from random  import random

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 500


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:  # eat sushi until it's all gone
        first_chopstick.acquire()
        if not second_chopstick.acquire(blocking = False):
            print(name, 'philosopher released their first chopstick')
            first_chopstick.release()
            #time.sleep(random()/10)  # Introduce randomeness to avoid more livelock issues
        else:
            try:
                if sushi_count > 0:
                    sushi_count -= 1
                    print(name, 'took a piece! Sushi remaining:', sushi_count)
            finally:
                second_chopstick.release()
                first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=(
        'Divya', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=(
        'Shree', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=(
        'Ansh', chopstick_a, chopstick_c)).start()
