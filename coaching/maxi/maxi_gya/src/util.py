import pygame
from pygame.math import Vector3

BLACK = Vector3(0, 0, 0)
WHITE = Vector3(255, 255, 255)
RED = Vector3(255, 0, 0)
YELLOW = Vector3(255, 255, 0)
GREEN = Vector3(0, 255, 0)
CYAN = Vector3(0, 255, 255)
BLUE = Vector3(0, 0, 255)


def show_fps(surface: pygame.Surface,
             font: pygame.font.Font,
             dt: float,
             text_color: Vector3 = GREEN,
             outline_color: Vector3 = BLACK):
    fps_text = font.render(f"FPS: {1 / dt:.0f}", True, text_color)
    fps_outline = font.render(f"FPS: {1 / dt:.0f}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))