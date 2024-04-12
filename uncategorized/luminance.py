import math
import time

import pygame
from pygame.math import Vector2, Vector3

pygame.init()


def normalize_channels(color: Vector3) -> Vector3:
    return color / 255


def sRGB_to_linear(normalized_color_channel: float) -> float:
    if normalized_color_channel <= 0.04045:
        return normalized_color_channel / 12.92

    return ((normalized_color_channel + 0.055) / 1.055) ** 2.4


def luminance(linear_color: Vector3) -> float:
    return linear_color.x * 0.2126 + linear_color.y * 0.7152 + linear_color.z * 0.0722


def percieved_lightness(luminance: float) -> float:
    if luminance <= 0.008856:
        return luminance * 9.033

    return (luminance ** (1 / 3) * 116 - 16) / 100


def color_to_percieved_lightness(color: Vector3) -> float:
    normalized_color = normalize_channels(color)
    return percieved_lightness(luminance(Vector3(sRGB_to_linear(normalized_color.x), sRGB_to_linear(normalized_color.y),
                                                 sRGB_to_linear(normalized_color.z))))


def rainbow(angle: float) -> Vector3:
    return Vector3(
        math.sin(angle) + 1,
        math.sin(angle + 2 * math.pi / 3) + 1,
        math.sin(angle + 4 * math.pi / 3) + 1,
    ) * 128

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.time()
clock = pygame.time.Clock()
run = True

angle = 0
angle_velocity = math.pi / 4

while run:

    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    angle += angle_velocity * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            window_resolution.xy = event.w, event.h
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         pass

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_1]:
        #     pass

    display.fill(Vector3(0, 0, 0))

    color = rainbow(angle)
    # lightness_grayscale = Vector3(255, 255, 255) * color_to_percieved_lightness(color)
    lightness_grayscale = rainbow(angle + math.pi)

    print(color_to_percieved_lightness(color), angle, sep="\t")

    pygame.draw.rect(display, color, (0, 0, window_resolution.x / 2, window_resolution.y))
    pygame.draw.rect(display, lightness_grayscale, (window_resolution.x / 2, 0, window_resolution.x, window_resolution.y))

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
