import time


def fib(n, memo={}):
    memo_value = memo.get(n)
    if memo_value:
        return memo_value

    if n <= 2:
        return 1

    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result
#
#
# for i in range(10):
#     fib(i)
#
#
# def fib(n):
#     if n <= 2:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(10))


def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(5))
