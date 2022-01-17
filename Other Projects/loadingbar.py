import time
import random


def loadingbar(progress, length=32, filler=chr(9608), background=chr(9617), prefix="Loading:", suffix="%"):
    filler_amt = int(progress * length)
    print(f"|{filler_amt * filler}{(length - filler_amt) * background}|{f' {prefix} '}{round(progress * 100, 1)}{suffix}", end="\r")


n = 100_000_000
i = 0
increment = 1
while i < n+1:
    if i % 10000 == 0:
     increment = random.randint(1, 1000)
    i += increment
    loadingbar(1 / n * i, prefix=" Loading: ")