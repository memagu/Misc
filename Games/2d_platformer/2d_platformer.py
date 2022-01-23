import pygame
import time
import noise
from helpers import *
from constants import *

pygame.init()

WINDOW_RESOLUTION = (1024, 768)
image_resolution = (64, 48)
transform_resolution = (WINDOW_RESOLUTION[0] // image_resolution[0], WINDOW_RESOLUTION[1] // image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

pygame.font.init()
font = pygame.font.SysFont(None, WINDOW_RESOLUTION[0] // 32)

run = True
time_prev = time.time()
clock = pygame.time.Clock()


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    if dt != 0:
        fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
        fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
        display.blit(fps_outline, (-1, -1))
        display.blit(fps_outline, (-1, 1))
        display.blit(fps_outline, (1, -1))
        display.blit(fps_outline, (1, 1))
        display.blit(fps_text, (0, 0))


def make_level(offset=0, seed=0):
    cols = []
    for col in range(image_resolution[0]):
        n = int((1 + noise.pnoise1((col + offset) / image_resolution[1], base=seed)) * 0.5 * image_resolution[1])
        cols.append(Column([range(n)]))

    return cols


w1l1 = Level(make_level())

while run:
    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            transform_resolution = (event.w // image_resolution[0], event.h // image_resolution[1])

        mouse_pos = pygame_to_coords(display, pygame.mouse.get_pos())
        mouse_pos = mouse_pos[0] // transform_resolution[0], mouse_pos[1] // transform_resolution[1]
        print(w1l1.columns[mouse_pos[0]].spans)

        if pygame.mouse.get_pressed()[0]:
            span = w1l1.columns[mouse_pos[0]].tile_in_span(mouse_pos[1])
            if span:
                w1l1.columns[mouse_pos[0]].remove_tile(span, mouse_pos[1])

        if pygame.mouse.get_pressed()[2] and not w1l1.columns[mouse_pos[0]].tile_in_span(mouse_pos[1]):
            w1l1.columns[mouse_pos[0]].add_tile(mouse_pos[1])

    display.fill(c.CYAN)

    for col in range(image_resolution[0]):
        for row in range(image_resolution[1]):
            w1l1.tile(col, row).draw(display, (col * transform_resolution[0], row * transform_resolution[1]),
                                     transform_resolution)

    show_fps(dt)
    pygame.display.update()
    clock.tick(480)
