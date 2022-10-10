import time

import pygame
from pygame.math import Vector2, Vector3

import body

DRAWSCALE_DISTANCE = 1.5e-8
DRAWSCALE_RADIUS = 5e-6
G = 6.67e-11

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.perf_counter()
clock = pygame.time.Clock()
run = True

sun = body.Body(1.98847e+30,
                6.963400e+08 * 0.1,
                Vector3(),
                Vector3(),
                Vector3(255, 255, 0))
earth = body.Body(5.972e+24,
                  6.371e+6,
                  Vector3(152.10e+9, 0, 0),
                  Vector3(0, 29.29e+3, 0),
                  Vector3(0, 128, 255))
moon = body.Body(7.34767309e+22,
                 1.7381e+06,
                 Vector3(earth.pos.x + 4.054e+8, 0, 0),
                 Vector3(0, 9.7e+2, 0),
                 Vector3(128, 128, 128))

bodies = [sun, earth]

while run:

    time_now = time.perf_counter()
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

    center = Vector3(*(window_resolution / 2), 0)
    center = Vector3(0, center.y, 0)

    for body in bodies:
        for other in bodies:
            if body is other:
                continue

            direction = (other.pos - body.pos).normalize()
            gravitational_acceleration = direction * G * other.mass / body.pos.distance_squared_to(other.pos)
            body.acc += gravitational_acceleration

        body.update(dt)
        body.acc = Vector3()

        body.draw(display, DRAWSCALE_DISTANCE, DRAWSCALE_RADIUS, center)

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
