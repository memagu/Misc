#!/bin/python

import base64
from itertools import combinations
from typing import Iterable

CIPHERS = (
    "bWqznPKmVMkt0Obu8bAINKvcBYpurA2yC0NKkUTXWw24Y8AtW9eK9+zipS2Cs6qBHDF7Jpn4z2jm2iT/RWXw6QbQgNb2Ty64i5IuVZxpHsZ6GGr860eM7g==",
    "dmrn1eTjXYw8y+bIx4V4buP0UcJ8qhG+X3hGnFiSTFiJZskgTI7Tssv9uDeE/b+QGjVsZdX63X28k0rfanPYvBrFjaL2UWucmIMLX+lyEtZtHGD26EmF9g==",
    "amqiy6HpTN5ox6/fypQqaavmRIRq+0jGF05W2FWWW1+vL84iRoDd5uXzvmOG9v6RDDw1JID73Hjljg7GZj7N/Q6KycvxAjuJmJ8TRbxrHcYzWVL07UWM6g==",
    "A7K+WILzJAdYo41+QSfb/Ud6MvX+cIopvwYoAcP5V3Y+6g2vYtZdzlulJPc1jvu1uDIgz1hjbLxAz6ya6zzIR7zc8Q9xeqJid/8KOg7HPhD/QI7Ohyj4Sg=="
)


def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def crib_drag(a: bytes, b: bytes, crib: str) -> list[str]:
    crib = bytes(crib, encoding="ASCII")
    xored = xor(a, b)
    return [result for i in range(len(a) - len(crib) + 1) if
            (result := xor(xored[i:i + len(crib)], crib).decode("ASCII", errors="ignore")).isprintable()]


def crib_drag_all(ciphers: Iterable[bytes], crib: str) -> list[tuple[int, int, list[str]]]:
    return [(i, j, crib_drag(cipher_a, cipher_b, crib)) for (i, cipher_a), (j, cipher_b) in
            combinations(enumerate(ciphers), 2)]


def main():
    ciphers = tuple(map(base64.b64decode, CIPHERS))
    crib = "multi-time pad"

    for i, j, results in crib_drag_all(ciphers, crib):
        if not results:
            continue

        print(f"Cipher {i} and {j} with crib: '{crib}' produced the following, printable only, strings:")
        print('\n'.join(results), end="\n\n")


if __name__ == '__main__':
    main()
