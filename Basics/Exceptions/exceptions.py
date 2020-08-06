# A generator is a special class of function that serves as an iterator instead of returning a single value the generator #returns a stream of values.
def main():
    try:
        for i in inclusive_range(0, 10, 5,5):
            print(i, end=" ")
        print()
    except TypeError as e:
        print(f'range error: {e}')


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    #initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f"Expected at most 3 arguments, got {numargs}")

    #generator
    i = start
    while i <= stop:
        # it's like return except it's for generator. It yields a value and then after it yields a value the function
        #continues until it yields the next value
        yield i
        i += step


if __name__ == "__main__":
    main()
