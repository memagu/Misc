import pygame
from math import sin, cos, atan, pi
import time

pygame.init()

WINDOW_RESOLUTION = (1000, 1000)
center = (WINDOW_RESOLUTION[0] / 2, WINDOW_RESOLUTION[1] / 2)
display = pygame.display.set_mode(WINDOW_RESOLUTION)
framerate = 480
trace = False

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
x2 = 0
y2 = 0
g = 9.82

trail = []
trail_length = 2048


def acc1():
    p1 = -g * (2 * m1 + m2) * sin(a1)
    p2 = -m2 * g * sin(a1 - 2 * a2)
    p3 = -2 * sin(a1 - a2) * m2
    p4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2)
    d = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    return (p1 + p2 + p3 * p4) / d


def acc1_new():
    return (-g * (2 * m1 + m2) * sin(a1) - m2 * g * sin(a1 - 2 * a2) -2 * sin(a1 - a2) * m2 * (a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2))) / (r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2)))


def acc2():
    p1 = 2 * sin(a1 - a2)
    p2 = a1_v * a1_v * r1 * (m1 + m2)
    p3 = g * (m1 + m2) * cos(a1)
    p4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2)
    d = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    return (p1 * (p2 + p3 + p4)) / d


def acc2_new():
    return 2 * sin(a1 - a2) * (a1_v * a1_v * r1 * (m1 + m2) + g * (m1 + m2) * cos(a1) + a2_v * a2_v * r2 * m2 * cos(a1 - a2)) / (r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2)))


def rainbow(angle):
    red = (sin(angle) + 1) / 2
    green = (sin(angle + pi / 1.5) + 1) / 2
    blue = (sin(angle + 2 * pi / 1.5) + 1) / 2
    return 255 * red, 255 * green, 255 * blue


time_prev = time.time()

run = True

while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    pos2_prev = x2, y2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                None

    a1_a = acc1()
    a2_a = acc2()

    a1_v += a1_a * dt
    a2_v += a2_a * dt

    a1 += a1_v * dt
    a2 += a2_v * dt

    mousepos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        a1 = atan(-1 * (mousepos[1] - center[1] + 2**-64) / (mousepos[0] - center[0] + (2 >> 31))) + pi / 2
        if mousepos[0] < center[0]:
            a1 += pi
        a1_v = 0
        a1_a = 0
        a2_a = 0
        a2_v = 0

    x1 = r1 * sin(a1) + center[0]
    y1 = r1 * cos(a1) + center[1]

    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r1 * cos(a2)

    trail.append((pos2_prev, (x2, y2), rainbow(a2)))
    if trail_length < len(trail):
        trail.pop(0)

    display.fill(color_black)

    for trail_segment in trail:
        pygame.draw.aaline(display, trail_segment[2], (trail_segment[0][0], trail_segment[0][1]),
                           (trail_segment[1][0], trail_segment[1][1]))

    pygame.draw.aaline(display, color, [*center], [x1, y1])
    pygame.draw.aaline(display, color, [x1, y1], [x2, y2])
    pygame.draw.circle(display, color, [x1, y1], m1)
    pygame.draw.circle(display, color, [x2, y2], m2)

    pygame.display.update()

    time.sleep(1 / framerate)
