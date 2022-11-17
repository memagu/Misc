def pow_mod(base: int, exponent: int, mod: int):
    if mod == 1:
        return 0

    for exp in range(1, exponent + 1):
        if not (congruent := base ** exp % mod) in (1, 0, mod - 1):
            continue

        result = base ** (exponent % exp)

        if not congruent:
            result *= 0

        if congruent == -1:
            result *= 1 if exponent // exp % 2 else -1

        return result % mod


def test(base: int, exponent: int, mod: int):
    pow_ = pow(base, exponent, mod)
    pow_mod_ = pow_mod(base, exponent, mod)

    return f"{pow_=} | {pow_mod_=} | {pow_ == pow_mod_}"


if __name__ == "__main__":
    print(test(7, 9634, 5))
    print(test(7, 9634, 343))
    print(test(7, 123, 11))
    print(test(7, 1, 76))
    print(test(7, 10, 4))
    print(test(7, 123, 8))
