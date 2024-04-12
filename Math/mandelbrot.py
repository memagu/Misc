def scale(value: float, a0: float, b0: float, a1: float, b1: float) -> float:
    return a1 + ((b1 - a1) / (b0 - a0)) * (value - a0)


def mandelbrot(real: float, imaginary: float, max_iterations: int) -> int:
    c = complex(real, imaginary)
    z = 0.0j

    for i in range(max_iterations):
        z = z * z + c
        if z.real ** 2 + z.imag ** 2 >= 1e8:
            return i

    return max_iterations


WIDTH = 34
HEIGHT = 16
MAX_ITER = 1 << 16

for y in range(HEIGHT):
    lin_y = scale(y, 0, HEIGHT, -0.9, 0.9)
    line = []
    for x in range(WIDTH):
        lin_x = scale(x, 0, WIDTH, -2, 0.475)

        if mandelbrot(lin_x, lin_y, MAX_ITER) == MAX_ITER:
            line.append('* ')
        else:
            line.append('  ')

    print("".join(line))

print("...")
