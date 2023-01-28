from enum import Enum


class Ordering(Enum):
    EQUAL = 0
    LESS = 1
    GREATER = 2


def compare(a, b) -> Ordering:
    if a == b:
        return Ordering.EQUAL

    if a < b:
        return Ordering.LESS

    return Ordering.GREATER


def sqrt(num, *, upper: float = 0, lower: float = 0, depth: int = 64):
    if not upper:
        upper = 0.0005 * num + 500

    mid = (upper + lower) / 2

    if not depth:
        return mid

    mid_sq = mid ** 2

    if mid_sq == num:
        return mid

    if mid_sq > num:
        return sqrt(num, upper=mid, lower=lower, depth=depth - 1)

    # if mid_sq < num:
    return sqrt(num, upper=upper, lower=mid, depth=depth - 1)


def sqrt_iterative(x: float) -> float:
    if not x:
        return x

    iteration_limit = 64
    upper = 0.0005 * x + 500
    lower = 0
    mid = (upper + lower) / 2

    for _ in range(iteration_limit):
        match compare(mid ** 2, x):
            case Ordering.EQUAL:
                return mid

            case Ordering.LESS:
                lower = mid

            case Ordering.GREATER:
                upper = mid

        mid = (upper + lower) / 2

    return mid


def test():
    import math

    decimals = 20
    for i in range(0, 10000):
        num = i / 1000
        sqrt_o = sqrt(num)
        math_sqrt_o = math.sqrt(num)
        print(
            f"sqrt({num})={sqrt_o:.{decimals}f}\tmath.sqrt({num})={math_sqrt_o:.{decimals}f}\tdiff={abs(math_sqrt_o - sqrt_o):.{decimals}f}")


def test_random_values():
    import math
    import random

    decimals = 20
    for _ in range(9800, 9900):
        num = random.randint(0, 10000) / 1000
        sqrt_o = sqrt(num)
        math_sqrt_o = math.sqrt(num)
        print(
            f"sqrt({num})={sqrt_o:.{decimals}f}\tmath.sqrt({num})={math_sqrt_o:.{decimals}f}\tdiff={abs(math_sqrt_o - sqrt_o):.{decimals}f}")


def main():
    test()
    print(sqrt_iterative(9.0))
    print(sqrt_iterative(2.0))
    print(sqrt_iterative(0.5))
    print(sqrt_iterative(0.25))
    print(sqrt_iterative(100.0))
    print(sqrt_iterative(81.0))
    print(sqrt_iterative(49.0))
    print(sqrt_iterative(0.0))


if __name__ == "__main__":
    main()
