def sqrt(num, *, upper: float = 0, lower: float = 0, depth: int = 50):
    if not upper:
        upper = num * 2

    mid = (upper + lower) / 2

    if not depth:
        return mid

    mid_sq = mid ** 2

    if mid_sq == num:
        return mid

    if mid_sq > num:
        return sqrt(num, upper=mid, lower=lower, depth=depth-1)

    # if mid_sq < num:
    return sqrt(num, upper=upper, lower=mid, depth=depth-1)


def test():
    import math
    import random

    decimals = 20
    for _ in range(9800, 9900):
        num = random.randint(0, 10000) / 1000
        sqrt_o = sqrt(num)
        math_sqrt_o = math.sqrt(num)
        print(f"sqrt({num})={sqrt_o:.{decimals}f}\tmath.sqrt({num})={math_sqrt_o:.{decimals}f}\tdiff={abs(math_sqrt_o - sqrt_o):.{decimals}f}")


def main():
    test()


if __name__ == "__main__":
    main()
