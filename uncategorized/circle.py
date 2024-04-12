import math
from pathlib import Path
from typing import Callable

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(600, 600)
display = pygame.display.set_mode(window_resolution)
pygame.display.set_caption(Path(__file__).name)

def rainbow(angle: float) -> Vector3:
    r = math.sin(angle) * 0.5 + 0.5
    g = math.sin(angle + 2 * math.pi / 3) * 0.5 + 0.5
    b = math.sin(angle + 4 * math.pi / 3) * 0.5 + 0.5

    return Vector3(r, g, b) * 255


def red_umbrella(angle: float) -> Vector3:
    return Vector3(255, 0, 0) * (math.sin(angle * 7) * 0.5 + 0.5)


def draw_circle(surface: pygame.Surface, point: Vector2, radius: float, color_func: Callable[[float], Vector3]) -> None:
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            temp = Vector2(x, y)

            if point.distance_to(temp) > radius:
                continue

            angle = math.atan2(*(temp - point).yx)

            color = color_func(angle)

            surface.set_at((x, y), color)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(Vector3(0, 0, 0))

    draw_circle(display, Vector2(200, 200), 100, red_umbrella)
    draw_circle(display, Vector2(400, 400), 150, rainbow)

    pygame.display.update()