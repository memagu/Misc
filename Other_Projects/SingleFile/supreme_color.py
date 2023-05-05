import math


def rainbow_2(angle):
    r = ((math.sin(angle) + 1) / (2)) * 255 * 0.9 ** (((math.sin(((angle) / (10))) + 1) / (2)) * 30)
    g = ((math.sin(angle + 2 * math.pi / 3) + 1) / (2)) * 255 * 0.9 ** (((math.sin(((angle) / (10))) + 1) / (2)) * 30)
    b = ((math.sin(angle + 4 * math.pi / 3) + 1) / (2)) * 255 * 0.9 ** (((math.sin(((angle) / (10))) + 1) / (2)) * 30)
    return tuple(map(int, (r, g, b)))


def rainbow(angle):
    r = ((math.sin(angle) + 1) / (2)) * 255
    g = ((math.sin(angle + 2 * math.pi / 3) + 1) / (2)) * 255
    b = ((math.sin(angle + 4 * math.pi / 3) + 1) / (2)) * 255
    return tuple(map(int, (r, g, b)))


import pygame
import time

pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True

angle = 0

r, g, b = 0, 0, 0

while run:
    # r = (r + 2) % 256
    # g = (g + 1) % 256
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # display.fill((r, g, b))
    display.fill(rainbow(angle))
    angle += 0.1
    print(f"{r=}\t{g=}\t{b=}")
    pygame.display.update()
    time.sleep(0.2)
