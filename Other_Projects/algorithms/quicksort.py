import random
import time


def qsort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    arr.remove(pivot)

    left = [e for e in arr if e < pivot]
    right = [e for e in arr if e >= pivot]

    return qsort(left) + [pivot] + qsort(right)


rand_arr = [random.randint(0, 1000000) for _ in range(1000000)]

print(qsort(rand_arr))