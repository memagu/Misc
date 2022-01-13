a = 1
b = 5
number_of_rectangles = 40

Dx = (b - a) / number_of_rectangles

print(Dx)

def f(x):
    return x ** 2 * 2.71828 ** x

def g(x):
    return 2.71828 ** (x ** 3 + 3 * x + 3)


rectangle_areas = []

for i in range(1, number_of_rectangles + 1):
    z = i * Dx - (Dx / 2)
    rectangle_areas.append(g(z) * Dx)

print(f"Integral between {a} and {b} estimated with {number_of_rectangles} rectangles is: {sum(rectangle_areas)}")

