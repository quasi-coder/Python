#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """
'''
 Classic example that's used to illustrate synchronization issues when multiple threads are competing for multiple locks is the Dining Philosopher's problem.
 As dining philosophers we'll both continue to alternate between eating and thinking but since we're operating as concurrent threads neither one of us knows when the other one wants to eat or think And that can lead to problems
 We've both acquired one of the two locks that we need so we're both stuck waiting on the other thread to release the other lock to make progress.
'''

import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 5000


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0:  # eat sushi until it's all gone
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count -= 1
            print(name, 'took a piece! Sushi remaining:', sushi_count)

        second_chopstick.release()
        first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=philosopher, args=(
        'Divya', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=(
        'Shree', chopstick_b, chopstick_c)).start()
    threading.Thread(target=philosopher, args=(
        'Ansh', chopstick_a, chopstick_c)).start()
