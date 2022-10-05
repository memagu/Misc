from random import uniform

from melvec import Vec2

ITERATIONS = 1_000_000
CENTER = Vec2()


def estimate_pi(iterations):
    circle_hits = 0

    for _ in range(iterations):
        rand_pos = Vec2(uniform(-1, 1), uniform(-1, 1))
        circle_hits += CENTER.distance_to_squared(rand_pos) <= 1

    return f"{circle_hits=:,}\t{iterations=:.2e}\tpi≈{4 * circle_hits / iterations}"


if __name__ == "__main__":
    # for i in range(9):
    #     print(f"{i}. ", estimate_pi(10**i))
    for i in range(1, 10001):
        print(f"{i}. ", estimate_pi(i))





