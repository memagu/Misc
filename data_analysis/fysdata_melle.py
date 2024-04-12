import matplotlib.pyplot as plt
import numpy as np
from typing import List


def plot_data(plot, line_color: str, x_data: List[int | float], x_quantity: str, x_unit: str, y_data: List[int | float],
              y_quantity: str,
              y_unit: str):
    x = np.array(x_data)
    y = np.array(y_data)

    k, m = np.polyfit(x, y, 1)

    plot.set_title(f"{y_quantity}({x_quantity}) = {k:.8f}{x_quantity} {'+' if m > 0 else '-'} {abs(m):.8f}")
    plot.set_xlabel(f"{x_quantity} / {x_unit}")
    plot.set_ylabel(f"{y_quantity} / {y_unit}")
    plot.plot(x, y, "ko", x, k * x + m, f"--{line_color}")
    plot.grid(which="major", linestyle="-")
    plot.grid(which="minor", linestyle="--")
    plot.minorticks_on()


current_current_ampere = [0, 0.58, 1.09, 1.49, 2.03, 2.94, 3.67, 4.29]
current_force_newton = [0, 0.002946, 0.006874, 0.008838, 0.011784, 0.016694, 0.021604, 0.02455]

length_length_m = [0.01, 0.022, 0.032, 0.042, 0.064, 0.08]
length_force_newton = [0.002946, 0.006874, 0.008838, 0.011784, 0.016694, 0.021604]

magnets_n_magnets = [6, 5, 4, 3, 2, 1, 0]
magnets_force_newton = [0.003928, 0.002946, 0.001964, 0.001964, 0.001964, 0, 0]

figure, axis = plt.subplots(1, 1)

plot_data(axis, 'b', current_current_ampere, "I", "A", current_force_newton, "F", "N")
plot_data(axis, 'r', length_length_m, "s", "m", length_force_newton, "F", "N")
plot_data(axis, 'g', magnets_n_magnets, "magneter", "antal", magnets_force_newton, "F", "N")

plt.show()
