from pathlib import Path

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(2560, 1440)
display = pygame.display.set_mode(window_resolution)
pygame.display.set_caption(Path(__file__).name)

class ResolutionCalculator:
    def __init__(self, base_resolution: Vector2, size_inches: float):
        self.base_resolution = base_resolution
        self.size = size_inches
        self.aspect_ratio = base_resolution.x / base_resolution.y
        self.pixels_per_inch = (base_resolution.x ** 2 + base_resolution.y ** 2) ** 0.5 / size_inches

    def inch_to_resolution(self, inches: float) -> Vector2:
        height = (inches * self.pixels_per_inch) / (1 + self.aspect_ratio ** 2) ** 0.5
        width = height * self.aspect_ratio

        return Vector2(width, height)


resolution_calculator = ResolutionCalculator(window_resolution, 27)
resolution_14_inch = resolution_calculator.inch_to_resolution(14)
resolution_16_1_inch = resolution_calculator.inch_to_resolution(16.1)
resolution_17_inch = resolution_calculator.inch_to_resolution(17)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(Vector3(0, 0, 0))

    pygame.draw.rect(display, Vector3(85), (0, 0, *resolution_17_inch))
    pygame.draw.rect(display, Vector3(170), (0, 0, *resolution_16_1_inch))
    pygame.draw.rect(display, Vector3(255), (0, 0, *resolution_14_inch))

    pygame.display.update()

