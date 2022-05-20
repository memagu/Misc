
calls = 0

def fib_n(n, calls):
    if n == 1 or n == 2:
        return 1

    calls += 2
    return fib_n(n-1, calls)[0] + fib_n(n-2, calls)[0], calls


print(fib_n(10, calls))
