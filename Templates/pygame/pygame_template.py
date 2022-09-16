import time

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(1200, 900)
image_resolution = Vector2(1200, 900)
transform_resolution = (window_resolution.x / image_resolution.x, window_resolution.y / image_resolution.y)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480  # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()


class Color:
    black = Vector3(0, 0, 0)
    white = Vector3(255, 255, 255)
    red = Vector3(255, 0, 0)
    yellow = Vector3(255, 255, 0)
    green = Vector3(0, 255, 0)
    cyan = Vector3(0, 255, 255)
    blue = Vector3(0, 0, 255)


pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", int(window_resolution.y) // 32)


def show_fps(delta_time, text_color=Color.green, outline_color=Color.black):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


while run := True:

    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            window_resolution.xy = event.w, event.h
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    display.fill(Color.black)

    show_fps(dt)
    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
