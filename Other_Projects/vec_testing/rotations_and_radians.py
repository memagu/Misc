import math
import time

from melvec import Vec2, Vec3
import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.time()
clock = pygame.time.Clock()
run = True

center = Vec2(*window_resolution.xy / 2)

v = Vec2(100, 0)
angle_velocity = math.pi/4

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
            center = window_resolution / 2

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         pass

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_1]:
        #     pass

    v = v.rotate(angle_velocity * dt)

    display.fill(Vector3(0, 0, 0))

    pygame.draw.aaline(display, (255, 255, 255), tuple(center), tuple(v + center))

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
