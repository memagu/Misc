import random

SIZE = 40 * 1024 ** 3

with open("test", "wb") as f:
    f.write(random.randbytes(SIZE))