import matplotlib.pyplot as plt
import numpy as np
from typing import List


def plot_data(plot, x_data: List[int | float], x_quantity: str, x_unit: str, y_data: List[int | float], y_quantity: str,
              y_unit: str):
    x = np.array(x_data)
    y = np.array(y_data)

    k, m = np.polyfit(x, y, 1)

    plot.set_title(f"{y_quantity}({x_quantity}) = {k:.8f}{x_quantity} {'+' if m > 0 else '-'} {abs(m):.8f}")
    plot.set_xlabel(f"{x_quantity} / {x_unit}")
    plot.set_ylabel(f"{y_quantity} / {y_unit}")
    plot.plot(x, y, 'yo', x, k * x + m, '--k')
    plot.grid(which="major", linestyle="-")
    plot.grid(which="minor", linestyle="--")
    plot.minorticks_on()


current_current_ampere = [0, 0.25, 0.38, 1.11, 1.71, 3.08, 3.71, 4.84, 4.93]
current_mass_gram = [0, 0.1, 0.2, 0.5, 0.7, 1.4, 1.7, 2.1, 2.2]
current_force_newton = list(map(lambda x: x / 1000 * 9.82, current_mass_gram))

magnets_n_magnets = [6, 5, 4, 3, 2, 1]
magnets_mass_gram = [0.42, 0.37, 0.3, 0.26, 0.16, 0.1]
magnets_force_newton = list(map(lambda x: x / 1000 * 9.82, magnets_mass_gram))

length_length_mm = [12, 22, 32, 42, 64, 84]
length_length_m = list(map(lambda x: x / 1000, length_length_mm))
length_mass_gram = [0.2, 0.4, 0.7, 0.9, 1.3, 1.6]
length_force_newton = list(map(lambda x: x / 1000 * 9.82, length_mass_gram))

figure, axis = plt.subplots(1, 1)

# plot_data(axis, current_current_ampere, "I", "A", current_force_newton, "F", "N")
# plot_data(axis, length_length_m, "s", "m", length_force_newton, "F", "N")
plot_data(axis, magnets_n_magnets, "magneter", "antal", magnets_force_newton, "F", "N")

plt.show()
