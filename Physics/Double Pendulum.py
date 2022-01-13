import pygame
from math import sin, cos, pi
import time

pygame.init()

WINDOW_RESOLUTION = (1000, 1000)
center = (WINDOW_RESOLUTION[0] / 2, WINDOW_RESOLUTION[1] / 2)
display = pygame.display.set_mode(WINDOW_RESOLUTION)
framerate = 60
trace = True

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

color = color_white

r1 = 200
r2 = 200
m1 = 10
m2 = 10
a1 = pi * 5 / 6
a2 = pi * 7 / 6
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0
g = 1


def acc1():
    p1 = -g * (2 * m1 + m2) * sin(a1)
    p2 = -m2 * g * sin(a1 - 2 * a2)
    p3 = -2 * sin(a1 - a2) * m2
    p4 = a2_v * a2_v * r2 + a1_v * a2_v * r1 * cos(a1 - a2)
    d = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    return (p1 + p2 + p3 * p4) / d


def acc2():
    p1 = 2 * sin(a1 - a2)
    p2 = a1_v * a1_v * r1 * (m1 + m2)
    p3 = g * (m1 + m2) * cos(a1)
    p4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2)
    d = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    return (p1 * (p2 + p3 + p4)) / d


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                None

    a1_a = acc1()
    a2_a = acc2()

    print(a1_a, a2_a)

    a1_v += a1_a
    a2_v += a2_a

    a1 += a1_v
    a2 += a2_v

    x1 = r1 * sin(a1) + center[0]
    y1 = r1 * cos(a1) + center[1]
    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r1 * cos(a2)














    display.fill(color_black)

    pygame.draw.line(display, color, [*center], [x1, y1])
    pygame.draw.line(display, color, [x1, y1], [x2, y2])
    pygame.draw.circle(display, color, [x1, y1], m1)
    pygame.draw.circle(display, color, [x2, y2], m2)

    pygame.display.update()

    time.sleep(1 / framerate)
