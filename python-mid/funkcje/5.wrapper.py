import functools
import time, datetime


def wrapper_time(func):
    def making_wrapper(*args, **kwargs):
        time_start = time.time()
        v = func(*args, **kwargs)
        time_stop = time.time()
        print(time_stop - time_start)
        return v
    return making_wrapper

# func tools in proper decorator
@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(2))


# Normal way of calling decorator with func

wrapper_get_sequence = wrapper_time(get_sequence)
n = 4
if get_sequence(n) == wrapper_get_sequence(n):
    print("It works")
else:
    print("something went wrong")
