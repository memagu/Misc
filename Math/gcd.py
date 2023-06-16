def gcd(a, b) -> int:
    q, r = divmod(a, b)
    if r == 0:
        return b

    return gcd(b, r)


if __name__ == "__main__":
    import math
    import random

    print(all(gcd(a, b) == math.gcd(a, b) for a, b in
              ((random.randint(-1_000_000_000, 1_000_000_000), random.randint(-1_000_000_000, 1_000_000_000)),) for _ in
              range(1_000_000)))
