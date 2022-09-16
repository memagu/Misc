import random

MIN = 0
MAX = 20


for i in range(10):
    n = random.randint(-50, 50)
    clamped = min(MAX, max(n, MIN))
    print(f"{n=} \t{clamped=}")


"""
min(MAX, max(val, MIN))

max(MIN, min(val, MAX))
"""





