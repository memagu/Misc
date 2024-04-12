import random

import pygame
import time
from helpers import *


pygame.init()

WINDOW_RESOLUTION = [1200, 900]
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 0  # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
font = pygame.font.SysFont(None, WINDOW_RESOLUTION[1] // 32)


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))

particles = []

while run:

    print(len(particles))

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    dt += (1 / 2 ** 16) if dt == 0 else 0
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WINDOW_RESOLUTION = [event.w, event.h]

        # Keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                temp = [*particles]
                for particle in temp:
                    particles += particle.explode(20, 100)
                for particle in temp:
                    particles.remove(particle)

        if event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(
                Particle(pygame.mouse.get_pos(),
                         [random.randint(-80, 80), -200],
                         [0, -200],
                         1.5,
                         10,
                         color_white,
                         0))

    # Draw
    display.fill(color_black)

    for particle in particles:
        if particle.fuse_time < 0 or particle.pos[1] - particle.radius > WINDOW_RESOLUTION[1]:
            if particle.acceleration[1] < 0:
                particles += particle.explode(20, 100)
            particles.remove(particle)
            continue
        particle.update_position(dt)
        particle.update_color(dt)
        if particle.is_visible(0, WINDOW_RESOLUTION[0], 0, WINDOW_RESOLUTION[1]):
            particle.draw(display)

    show_fps(dt)
    pygame.display.update()
    if fps > 0:
        clock.tick(fps)