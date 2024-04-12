from pathlib import Path

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution)
pygame.display.set_caption(Path(__file__).name)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(Vector3(0, 0, 0))
    pygame.display.update()

    