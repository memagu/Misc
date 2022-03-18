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

s1 = Slider([100, 100], "circle diameter")
s2 = Slider([400, 200], "rect height", math.pi / 3)
print(s1.pos_to_value((200, 100)))

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
            transform_resolution = (
            window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    # Draw
    display.fill(color_black)

    s1.draw_slider(display, color_white)
    s2.draw_slider(display, color_white)
    s1.update()
    s2.update()

    show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
