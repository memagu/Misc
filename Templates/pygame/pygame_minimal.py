import time

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

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
