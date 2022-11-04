def fib(n):
    a = 1
    b = 0

    if n > 0:
        for _ in range(n - 1):
            a, b = a + b, a
        return a

    for _ in range(-n + 1):
        a, b = b, a - b
    return a


if __name__ == "__main__":
    # print(fib(8))
    n = 100
    for i in range(-n, n+1):
        print(fib(i))


# Time complexity: O(n)

# Space complexity: O(1)


# DFS with memo
# Time complexity: O(n)
# Space complexity: O(n)