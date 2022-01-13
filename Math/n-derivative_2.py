import sympy

while True:

    f = input("Input function: ")
    n = int(input("Input derivative depth: "))
    x = sympy.Symbol(input("Input dependent variable: "))

    print(f"\n----------------\n0 f(x) = {f}")

    for i in range(n):
        f_prime = sympy.diff(f)
        print(f"{i + 1} f{chr(39) * (i + 1)}(x) = {f_prime}")
        f = f_prime

    print("----------------\n")

