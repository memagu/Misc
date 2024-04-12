import math
import time

import keyboard
import mouse

DURATION = 5
RADIUS = 500


def trace_circle(origin_x: float, origin_y: float, radius: float, duration: float) -> None:
    angle_velocity = 2 * math.pi / duration
    angle = 0
    time_prev = time.perf_counter()

    while angle < 2 * math.pi:
        time_now = time.perf_counter()
        dt = time_now - time_prev
        time_prev = time_now

        angle += angle_velocity * dt

        mouse.move(origin_x + math.cos(angle) * radius, origin_y + math.sin(angle) * radius)


def main() -> None:
    while not keyboard.is_pressed("enter"):
        continue

    origin_x, origin_y = mouse.get_position()

    mouse.move(RADIUS, 0, False)
    mouse.press()
    trace_circle(origin_x, origin_y, RADIUS, DURATION)
    mouse.release()



def min_percentage():
    while not keyboard.is_pressed("enter"):
        continue

    tolerance = 5

    min_rad = 150 + tolerance
    max_rad = 600 - tolerance

    origin_x, origin_y = mouse.get_position()

    mouse.move(origin_x + min_rad, origin_y)

    mouse.press()

    mouse.move(origin_x + max_rad, origin_y, duration=0.5)
    mouse.move(0, max_rad, absolute=False, duration=1.5)
    mouse.move(-2 * max_rad, 0, absolute=False, duration=0.5)
    mouse.move(0, -2 * max_rad, absolute=False, duration=0.5)
    mouse.move(2 * max_rad, 0, absolute=False, duration=0.5)
    mouse.move(0, max_rad, absolute=False, duration=0.5)

    mouse.release()


if __name__ == "__main__":
    min_percentage()
