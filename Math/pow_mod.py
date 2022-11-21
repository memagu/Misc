def pow_mod(base: int, exponent: int, mod: int):
    if mod == 1:
        return 0

    congruents = {1, 0, mod - 1}

    for exp in range(1, exponent + 1):
        if (congruent := base ** exp % mod) not in congruents:
            continue

        result = base ** (exponent % exp)

        if not congruent:
            result *= 0

        if congruent == mod - 1:
            # result *= -1 if exponent // exp % 2 else 1
            result *= (not exponent // exp % 2) * 2 - 1

        return result % mod

    return base ** exponent % mod

def test(base: int, exponent: int, mod: int):
    pow_ = pow(base, exponent, mod)
    pow_mod_ = pow_mod(base, exponent, mod)

    return f"{base=}, {exponent=}, {mod=} | {pow_=} | {pow_mod_=} | {pow_ == pow_mod_}"


if __name__ == "__main__":
    print(test(7, 9634, 5))
    print(test(7, 9634, 343))
    print(test(7, 123, 11))
    from random import randint
    for i in range(100):
        print("False" in test(randint(0, 1000), randint(0, 10000), randint(1, 200)))
