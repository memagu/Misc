def is_prime(n):
    if n == 2:
        return True

    if n in [0, 1] or n % 2 == 0:
        return False

    sqrt_n = n ** 0.5

    if sqrt_n % 2 == 0:
        return False

    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True


n = 100
seq = [0, 1]
for i in range(1, n):
    seq.append(seq[i] + seq[i-1])
    if is_prime(seq[i]):
        print(seq[i])

