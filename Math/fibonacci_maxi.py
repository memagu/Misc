# Maxis val av variabler

import time

n = 99999

start = time.perf_counter()

fibbe = [0, 1]
for fibbes_mamma in range(1, n):
    fibbe.append(fibbe[fibbes_mamma] + fibbe[fibbes_mamma-1])
    # print(fibbe[-1])

stop = time.perf_counter()

print(stop-start)

# 0, 1, 1, 2, 3, 5

