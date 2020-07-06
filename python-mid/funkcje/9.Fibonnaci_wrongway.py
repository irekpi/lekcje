import functools
import time


@functools.lru_cache()
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for item in range(1, 37):
    print(fib(item))
end = time.time()
duration = end-start
print(duration)
print(fib.cache_info())