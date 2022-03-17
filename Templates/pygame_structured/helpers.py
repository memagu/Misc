import pygame
import time
import math

# Misc variables

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


# Functions
def show_fps(surface, font, dt, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / dt)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / dt)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


def rainbow(angle):
    r = (math.sin(angle) + 1) / 2
    g = (math.sin(angle + math.pi / 1.5) + 1) / 2
    b = (math.sin(angle + 2 * math.pi / 1.5) + 1) / 2
    return [255 * r, 255 * g, 255 * b]


if __name__ == "__main__":
    print(__file__.split("\\")[-1])
