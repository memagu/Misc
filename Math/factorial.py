def factorial_recursive(num: int):
    """
    n! = n * (n-1)!
    ↓
    (n-1)! = (n-1) * ((n-1)-1)!
    ↓
    ...
    ↓
    (n-k)! = (n-k) * 1
    """
    if num == 2:
        return 2

    return num * factorial_recursive(num - 1)


def factorial_iterative(num: int):
    """
    n! = n * (n-1) * (n-2) * (n-3) ... (n-k) * 1
    """
    result = num
    while num != 2:
        result *= num - 1
        num -= 1
    return result