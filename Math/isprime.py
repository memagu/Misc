
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


def is_prime_slow(n):
    if n in [0, 1]:
        return False

    sqrt_n = n ** 0.5

    for i in range(2, int(sqrt_n) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1000):
    if is_prime(i):
        print(i)



# number_of_tests = 10
# primes_in_range = 1000000
#
#
# acc = []
# for i in range(number_of_tests):
#     start = time.perf_counter()
#     for i in range(primes_in_range):
#         # Function to test
#         is_prime(i)
#
#     stop = time.perf_counter()
#     acc.append(stop-start)
#     print(stop-start)
#
# print()
# print(sum(acc) / number_of_tests)


