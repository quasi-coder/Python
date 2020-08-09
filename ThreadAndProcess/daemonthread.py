#!/usr/bin/env python3
""" Shree finishes cooking while Divya cleans """

import threading
import time


def kitchen_cleaner():
    while True:
        print('Divya cleaned the kitchen.')
        time.sleep(1)


if __name__ == '__main__':
    divya = threading.Thread(target=kitchen_cleaner)
    divya.daemon = True
    divya.start()

    print('Shree is cooking...')
    time.sleep(0.6)
    print('Shree is cooking...')
    time.sleep(0.6)
    print('Shree is cooking...')
    time.sleep(0.6)
    print('Shree is done!')
