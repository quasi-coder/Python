#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """
'''
Starvation occurs when a thread is unable to gain access to a necessary resource and is therefore unable to make progress. If another greedy thread is frequently holding a lock on the shared resource, then the starved thread won't get a chance to execute. - In a simple scenario like ours, with two equal threads competing for execution time, starvation probably isn't a concern. Both of our threads should get plenty of chances to take sushi. However, if our two threads are given different priorities then that may not be the case.- How different thread priorities get treated will depend on the operating system, but generally higher priority threads will be scheduled to execute more often and that can leave low priority threads, like me, feeling hungry. Another thing that can lead to starvation is having too many concurrent threads. - Oh, I forgot to mention that I invited some friends over. (scoffing) - Well with this many competing threads, I may never get any sushi.
'''
import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()
sushi_count = 10000


def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    shushi_eaten = 0
    while sushi_count > 0:  # eat sushi until it's all gone
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count -= 1
            shushi_eaten += 1
            print(name, 'took a piece! Sushi remaining:', sushi_count)
        second_chopstick.release()
        first_chopstick.release()
    print(name, 'took', shushi_eaten, 'pieces')


if __name__ == '__main__':
    for i in range(50):
        threading.Thread(target=philosopher, args=(
            'Divya', chopstick_a, chopstick_b)).start()
        threading.Thread(target=philosopher, args=(
            'Shree', chopstick_b, chopstick_c)).start()
        threading.Thread(target=philosopher, args=(
            'Ansh', chopstick_a, chopstick_c)).start()
