import random
import threading
import time
from typing import List, Optional, Callable

import pygame

import tools
import util

pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 0
time_prev = time.time()
clock = pygame.time.Clock()
run = True

selected_tool: Optional[Callable] = None
selected_color: Optional[pygame.Color] = None

active_tool_threads: List[threading.Thread] = []

mouse_is_pressed = False

while run:
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            window_resolution = event.w, event.h
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                tools.run_tools = False
                for td_tool in active_tool_threads:
                    td_tool.join()

                display.fill(pygame.Color(0, 0, 0))
                pygame.display.update()
                tools.run_tools = True

            if event.key == pygame.K_f:
                selected_tool = tools.fill_bfs

            # if event.key == pygame.K_b:
            #     selected_tool = tools.brush

            if event.key == pygame.K_r:
                selected_color = pygame.Color(255, 0, 0)

            if event.key == pygame.K_g:
                selected_color = pygame.Color(0, 255, 0)

            if event.key == pygame.K_b:
                selected_color = pygame.Color(0, 0, 255)

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if not mouse_is_pressed and selected_tool and selected_color:
                mouse_is_pressed = True
                td_tool = threading.Thread(target=selected_tool, args=(display, mouse_pos, selected_color), daemon=True)
                active_tool_threads.append(td_tool)
                active_tool_threads[-1].start()
        else:
            mouse_is_pressed = False

        active_tool_threads = [td_tool for td_tool in active_tool_threads if td_tool.is_alive()]

    # if random.random() < 1:
    #     td_tool = threading.Thread(target=tools.fill_bfs, args=(display,
    #                                                             (random.randint(0, window_resolution[0] - 1),
    #                                                              random.randint(0, window_resolution[1] - 1)),
    #                                                             util.rainbow(random.uniform(0, 6.283))),
    #                                daemon=True)
    #     active_tool_threads.append(td_tool)
    #     active_tool_threads[-1].start()

    if abs(framerate):
        clock.tick(framerate)


# TODO: State machine
