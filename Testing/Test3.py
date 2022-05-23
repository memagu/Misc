import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\033[92m{func.__name__}\033[0m execution time: {round((end - start) * 10 ** 6, 3):,}µs")

    return wrapper


@timer
def test(n):
    arr = [i for i in range(n)]


test(1000000)

print([1,2,3].remove(1))

