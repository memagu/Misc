import math
from typing import List


def factors(x: int) -> List[int]:
    return [divisor for divisor in range(1, x + 1) if not x % divisor]


def prime_factors(x: int) -> List[int]:
    divisors = []
    last_divisor = 2

    while True:
        for divisor in range(last_divisor, x + 1):
            print(divisor, x)
            if not x % divisor:
                divisors.append(divisor)
                last_divisor = divisor
                x //= divisor
                break
        else:
            break

    return divisors


if __name__ == '__main__':
    test_nums = [12, 100, 130, 30300]

    for num in test_nums:
        print(f"{num=: <16} {factors(num)=}")

    print('-' * 32)

    for num in test_nums:
        print(f"{num=: <16} {prime_factors(num)=}")
