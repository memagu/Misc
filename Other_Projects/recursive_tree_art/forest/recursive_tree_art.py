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

number_of_trees = 13
tree_depth = 8
branch_length_coefficient = 0.8
left_branch_angle = math.pi / 16
right_branch_angle = -math.pi / 16
branching_probability = 1
angle_noise_amplitude = 0.1
seed = 3

roots = []
for i in range(number_of_trees):
    roots.append(Branch([(i + 1) * window_resolution[0] / (number_of_trees + 1), window_resolution[1] - (window_resolution[1] >> 3)],
             3 / 4 * window_resolution[1] / sum([branch_length_coefficient ** i for i in range(tree_depth)]),
             math.pi / 2))


trees = []
for root in roots:
    trees.append(construct_tree(root,
                 tree_depth,
                 branching_probability,
                 branch_length_coefficient,
                 angle_noise_amplitude,
                 left_branch_angle,
                 right_branch_angle))

angle_offset = 0
angle_speed = math.pi/2

while run:

    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    angle_offset += angle_speed * dt
    change_angle = math.sin(angle_offset) * math.pi / 512

    random.seed(seed)
    for i in range(len(trees)):
        trees[i] = construct_tree(roots[i],
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

            for i in range(number_of_trees):
                print((i + 1) * window_resolution[0] / (number_of_trees + 1))
                roots[i] = (Branch([(i + 1) * window_resolution[0] / (number_of_trees + 1), window_resolution[1] - (window_resolution[1] >> 3)],
                            3 / 4 * window_resolution[1] / sum([branch_length_coefficient ** i for i in range(tree_depth)]),
                            math.pi / 2))

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    # Draw
    display.fill((29, 29, 29))

    for tree in trees:
        draw_tree(tree, display, color_white, True)

    show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
