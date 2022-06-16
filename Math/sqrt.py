def slow_sqrt(num, *, upper_limit=0, lower_limit=0, max_depth=942, depth=0):
    if depth == 0:
        upper_limit = num * 2
    current = (upper_limit + lower_limit) / 2

    if depth == max_depth:
        return current

    current_sq = current ** 2

    if current_sq == num:
        return current

    if current_sq > num:
        return slow_sqrt(num, upper_limit=current, lower_limit=lower_limit, depth=depth+1)

    if current_sq < num:
        return slow_sqrt(num, upper_limit=upper_limit, lower_limit=current, depth=depth+1)


def test():
    import math
    decimals = 20
    for i in range(9800, 9900):
        print(f"slow_sqrt({i/1000})={slow_sqrt(i/1000):.{decimals}f}\tmath.sqrt({i/1000})={math.sqrt(i/1000):.{decimals}f}\tdiff={abs(math.sqrt(i/100)-slow_sqrt(i/100)):.{decimals}f}")


if __name__ == "__main__":
    import math
    print(f"{math.pi ** 2:.100f}")
    print(slow_sqrt(9.869604401089357992304940125904977321624755859375) - math.pi)
