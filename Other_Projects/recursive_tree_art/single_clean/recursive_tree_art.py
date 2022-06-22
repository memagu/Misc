import random


import pygame
from helpers import *

pygame.init()

window_resolution = [1600, 1200]
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
right_branch_angle = 7 * math.pi / 4
branching_probability = 1
angle_noise_amplitude = 0.3
seed = 1

sliders = []
vertical_separation = 88
sliders.append(Slider([32, 40 + vertical_separation * 0], "tree depth", min_value=0, max_value=20, value=tree_depth))
sliders.append(Slider([32, 40 + vertical_separation * 1], "branch length coefficient", min_value=0, max_value=1, value=branch_length_coefficient))
sliders.append(Slider([32, 40 + vertical_separation * 2], "left branch angle", min_value=-math.pi * 2, max_value=math.pi * 2, value=left_branch_angle))
sliders.append(Slider([32, 40 + vertical_separation * 3], "right branch angle", min_value=-math.pi * 2, max_value=math.pi * 2, value=right_branch_angle))
sliders.append(Slider([32, 40 + vertical_separation * 4], "branching probability", min_value=0, max_value=1, value=branching_probability))
sliders.append(Slider([32, 40 + vertical_separation * 5], "angle noise amplitude", min_value=0, max_value=2, value=angle_noise_amplitude))
sliders.append(Slider([32, 40 + vertical_separation * 6], "seed", min_value=0, max_value=100, value=seed))


root = Branch([window_resolution[0] / 2, window_resolution[1] - (window_resolution[1] >> 3)],
              3 / 4 * window_resolution[1] / sum([branch_length_coefficient ** i for i in range(int(sliders[0].value))]),
              math.pi / 2)

tree = construct_tree(root,
                      int(sliders[0].value),
                      sliders[4].value,
                      sliders[5].value,
                      sliders[1].value,
                      sliders[2].value,
                      sliders[3].value)

angle_offset = 0
angle_offset_velocity = math.pi / 2
angle_offset_amplitude = math.pi / 512

sliders.append(Slider([32, 40 + vertical_separation * 7], "angle offset velocity", min_value=0, max_value=math.pi * 2, value=angle_offset_velocity))
sliders.append(Slider([32, 40 + vertical_separation * 8], "angle offset amplitude", min_value=0, max_value=math.pi / 16, value=angle_offset_amplitude))
sliders.append(Slider([32, 40 + vertical_separation * 9], "base width ratio", min_value=0, max_value=1, value=0.2))

while run:

    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    angle_offset += sliders[7].value * dt
    change_angle = math.sin(angle_offset) * sliders[8].value

    random.seed(int(sliders[6].value))
    tree = construct_tree(root,
                          int(sliders[0].value),
                          sliders[4].value,
                          sliders[5].value,
                          sliders[1].value,
                          sliders[2].value + change_angle,
                          sliders[3].value + change_angle)

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
                              [sliders[1].value ** i for i in range(int(sliders[0].value))]),
                          math.pi / 2)


    # Draw
    display.fill((29, 29, 29))

    traverse_tree(root, draw_branch_polygon, display, sliders[9].value, color_white, True)
    for slider in sliders:
        slider.update()
        slider.draw_slider(display, color_white)

    # show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
