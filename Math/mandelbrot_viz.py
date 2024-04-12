def scale(value: float, a0: float, b0: float, a1: float, b1: float) -> float:
    return a1 + ((b1 - a1) / (b0 - a0)) * (value - a0)


def mandelbrot(real: float, imaginary: float, max_iterations: int) -> int:
    c = complex(real, imaginary)
    z = 0.0j

    for i in range(max_iterations):
        z = z * z + c
        if z.real ** 2 + z.imag ** 2 >= 4:
            return i

    return max_iterations


import time

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(2560, 1440)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.time()
clock = pygame.time.Clock()
run = True

while run:

    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            window_resolution.xy = event.w, event.h
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         pass

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_1]:
        #     pass

    display.fill(Vector3(0, 0, 0))

    for x in range(int(window_resolution.x)):
        lin_x = scale(x, 0, window_resolution.x, -2, 0.47)
        for y in range(int(window_resolution.y)):
            lin_y = scale(y, 0, window_resolution.y, -1.12, 1.12)
            display.set_at((x, y), Vector3(255, 255, 255) * mandelbrot(lin_x, lin_y, 30) / 30)

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
