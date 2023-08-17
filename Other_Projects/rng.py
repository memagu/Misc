from collections import Counter
from typing import Callable, Iterator

import matplotlib.pyplot as plt
from matplotlib import gridspec


def linear_rng(seed: int, func: Callable[[int], int]) -> Iterator[int]:
    x = seed
    while True:
        x = func(x)
        yield x


rng_a = linear_rng(0, lambda x: (5 * x + 1) % 8)
rng_b = linear_rng(0, lambda x: (2 * x + 1) % 8)
rng_c = linear_rng(0, lambda x: ((25173 * x + 13849) % (2 << 15)))

nums_a = [next(rng_a) for _ in range(10)]
nums_b = [next(rng_b) for _ in range(10)]
nums_c = [next(rng_c) >> 7 for _ in range(65536)]

print("a)")
print('\n'.join(f"{i + 1: <8}{num: <8}{bin(num).replace('0b', '').rjust(4, '0'): <8}{bin(num).replace('0b', '').rjust(2, '0')[:2]: <8}{int(bin(num).replace('0b', '').rjust(2, '0')[:2], 2): <8}" for i, num in enumerate(nums_a)))
print("b)")
print('\n'.join(f"{i + 1: <8}{num: <8}{bin(num).replace('0b', '').rjust(4, '0'): <8}{bin(num).replace('0b', '').rjust(2, '0')[:2]: <8}{int(bin(num).replace('0b', '').rjust(2, '0')[:2], 2): <8}" for i, num in enumerate(nums_b)))

fig = plt.figure()
gs = gridspec.GridSpec(2, 2)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])

axs = ax1, ax2, ax3

for ax, nums, label in zip(axs, (nums_a, nums_b, nums_c), "abc"):
    ax.bar(*zip(*Counter(nums).items()))
    ax.title.set_text(f"{label}) n = {len(nums)}")
    ax.set_xlabel('Genererade nummer')
    ax.set_ylabel('Antal förekomster')


plt.show()
