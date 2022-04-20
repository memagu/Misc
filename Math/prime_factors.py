def is_prime(num):
    if num == 2:
        return True

    if num in [0, 1] or num % 2 == 0:
        return False

    sqrt_num = num ** 0.5

    for i in range(3, int(sqrt_num) + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_factors(num):
    if is_prime(num):
        return [num]

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return prime_factors(num // i) + prime_factors(i)


def factors(num): #TRASIG
    base_factors = prime_factors(num) + [1]
    factor_muls = set()
    for i in range(len(base_factors)):
        for j in range(len(base_factors)):
            if i != j:
                factor_muls.add(base_factors[i] * base_factors[j])
    return list(factor_muls) + [1, num]


print(prime_factors(720720))
print(sorted(factors(720720)))