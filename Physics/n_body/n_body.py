import pygame
from helpers import *
import random

pygame.init()

window_resolution = [800, 800]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

gravity_strength = Slider([40,40], "exponent", 0, 200, -2, 2, 0)

planets = [Planet(Vec2(random.randint(0, window_resolution[0]), random.randint(0, window_resolution[1])),
                  Vec2(),
                  random.randint(10, 1000),
                  Vec3(random.randint(100, 255), random.randint(100, 255), random.randint(0, 255)))
           for _ in range(25)]

while run:

    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = [event.w, event.h]


        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    gravity_strength.update()

    for planet in planets:
            planet.calculate_acceleration(planets, 6.67*10**gravity_strength.value)

    # Draw
    display.fill(color_black)

    gravity_strength.draw_slider(display)

    for planet in planets:
        planet.update(dt)
        planet.draw(display)
        if planet.pos.x < 0:
            planet.vel.x *= -1
            planet.pos.x = 0
            continue
        if planet.pos.x > window_resolution[0]:
            planet.vel.x *= -1
            planet.pos.x = window_resolution[0]
            continue
        if planet.pos.y < 0:
            planet.vel.y *= -1
            planet.pos.y = 0
            continue
        if planet.pos.y > window_resolution[1]:
            planet.vel.y *= -1
            planet.pos.y = window_resolution[1]
            continue


    show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
