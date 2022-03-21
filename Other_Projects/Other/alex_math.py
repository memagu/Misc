n = int(input("Enter number: "))

iterations = 0
while n > 1:
    iterations += 1
    print(n)

    if n % 2 == 0:
        n //= 2
        continue

    n = 3 * n + 1

print(1)
print(f"\n{iterations=}")