import random

while True:
  n = random.randint(4096, 4294967296)
  n = str(bin(n)).removeprefix("0b")

  print("\033[92m" + n)