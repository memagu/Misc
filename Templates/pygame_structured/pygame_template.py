import pygame
from helpers import *

pygame.init()

window_resolution = [1200, 900]
image_resolution = [1200, 900]
transform_resolution = (window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

while run:

    dt = delta_time(prev_time)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = [event.w, event.h]
            transform_resolution = (window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])


        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    # Draw
    display.fill(color_black)

    show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
