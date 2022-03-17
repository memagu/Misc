import random

import pygame
from helpers import *

pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] >> 5)

tree_depth = 12
branch_length_coefficient = 0.7
left_branch_angle = math.pi / 4
right_branch_angle = -math.pi / 4
branching_probability = 1
angle_noise_amplitude = 0.3
seed = 1

root = Branch([window_resolution[0] / 2, window_resolution[1] - (window_resolution[1] >> 3)],
              3 / 4 * window_resolution[1] / sum([branch_length_coefficient ** i for i in range(tree_depth)]),
              math.pi / 2)

tree = construct_tree(root,
                      tree_depth,
                      branching_probability,
                      branch_length_coefficient,
                      angle_noise_amplitude,
                      left_branch_angle,
                      right_branch_angle)

angle_offset = 0
angle_speed = math.pi / 2

while run:

    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    angle_offset += angle_speed * dt
    change_angle = math.sin(angle_offset) * math.pi / 512

    random.seed(seed)
    tree = construct_tree(root,
                          tree_depth,
                          branching_probability,
                          angle_noise_amplitude,
                          branch_length_coefficient,
                          left_branch_angle + change_angle,
                          right_branch_angle + change_angle)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = [event.w, event.h]
            root = Branch([window_resolution[0] / 2, window_resolution[1] - (window_resolution[1] >> 3)],
                          3 / 4 * window_resolution[1] / sum(
                              [branch_length_coefficient ** i for i in range(tree_depth)]),
                          math.pi / 2)

        # Keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                seed += 1
            if event.key == pygame.K_c:
                seed -= 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        left_branch_angle += math.pi / 8 * dt
    if keys[pygame.K_DOWN]:
        left_branch_angle -= math.pi / 8 * dt
    if keys[pygame.K_RIGHT]:
        right_branch_angle += math.pi / 8 * dt
    if keys[pygame.K_LEFT]:
        right_branch_angle -= math.pi / 8 * dt


    # Draw
    display.fill((29, 29, 29))

    # draw_tree(tree, display, color_white, True)
    #traverse_tree(root, draw_branch, display, color_white, True)
    traverse_tree(root, draw_branch_polygon, display, 0.2, color_white, True)

    #show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
