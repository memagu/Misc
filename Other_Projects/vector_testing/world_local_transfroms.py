import pygame
import time
from Math.melutil.melvec import *

pygame.init()

window_resolution = [400, 400]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

# Text
pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

################################

local_origin_in_worldspace = Vec2(200, 200)
i_hat = Vec2(20, 0)
#i_hat = Vec2.from_angle(-math.pi / 6, 20)
j_hat = Vec2(7, -18)
#j_hat = Vec2.from_angle(-2 * math.pi/3, 20)


local_pt = Vec2(2, 1)


def local_to_world(point: Vec2) -> Vec2:
    x = i_hat * point.x
    y = j_hat * point.y
    return x + y + local_origin_in_worldspace

################################

while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_1:

    # Draw
    display.fill(color_black)

    for i in range(-9, 10):
        pygame.draw.aaline(display, (29, 29, 29), local_to_world(Vec2(i, -10)).as_list(), local_to_world(Vec2(i, 10)).as_list())
        pygame.draw.aaline(display, color_white, local_to_world(Vec2(i, -0.25)).as_list(), local_to_world(Vec2(i, 0.25)).as_list())

    for i in range(-9, 10):
        pygame.draw.aaline(display, (29, 29, 29), local_to_world(Vec2(-10, i)).as_list(), local_to_world(Vec2(10, i)).as_list())
        pygame.draw.line(display, color_white, local_to_world(Vec2(-0.25, i)).as_list(), local_to_world(Vec2(0.25, i)).as_list())

    pygame.draw.line(display, color_white, local_to_world(Vec2(-10, 0)).as_list(), local_to_world(Vec2(10, 0)).as_list())
    pygame.draw.line(display, color_white, local_to_world(Vec2(0, -10)).as_list(), local_to_world(Vec2(0, 10)).as_list())

    pygame.draw.circle(display, color_white, local_to_world(Vec2(-5, 7)).as_list(), 2.5)

    for i in range(-999, 1000):
        x = i / 100
        y = x ** 2
        pygame.draw.circle(display, color_white, local_to_world(Vec2(x, y)).as_list(), 2.5)

    pygame.display.update()
    if fps > 0:
        clock.tick(fps)
