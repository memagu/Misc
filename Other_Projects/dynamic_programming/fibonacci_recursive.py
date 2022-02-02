import time


def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


for i in range(50):
    print(fib(i+1))


