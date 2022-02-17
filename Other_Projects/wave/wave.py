import pygame
import time
import math


pygame.init()

WINDOW_RESOLUTION = (1200, 900)
image_resolution = [300, 900]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()

offset_per_second = 20
rectangle_height = 50
amplitude = 100

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

# Text
pygame.font.init()
font = pygame.font.SysFont(None, WINDOW_RESOLUTION[0] // 32)


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


def rainbow(angle):
    r = (math.sin(angle) + 1) / 2
    g = (math.sin(angle + math.pi / 1.5) + 1) / 2
    b = (math.sin(angle + 2 * math.pi / 1.5) + 1) / 2
    return 255 * r, 255 * g, 255 * b


offset = 0
while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev + 0.000_000_000_000_000_1
    time_prev = time_now

    offset += offset_per_second * dt

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_1:

    display.fill((29,29,29))

    for i in range(image_resolution[0]):
        angle = (i * (WINDOW_RESOLUTION[0] / image_resolution[0])) / 3
        center_y = WINDOW_RESOLUTION[1] / 2 - rectangle_height / 2
        x = i * transform_resolution[0]
        # sin(((x+offset)/(10)))*50 + sin(((x+offset)/(100)))*50 + cos(x)*100
        w1 = math.sin((angle + offset) / 10) * amplitude
        w2 = math.sin((angle + offset) / 100) * amplitude
        w3 = math.cos(angle) * amplitude * 2
        y = center_y + w1 + w2 + w3
        # y = center_y + math.sin((angle + offset) / 10) * amplitude
        # pygame.draw.line(display, color_white, (x + transform_resolution[0] / 2, center_y - amplitude), (x + transform_resolution[0] / 2, center_y + amplitude))
        pygame.draw.rect(display, rainbow(angle + offset), [x, y, transform_resolution[0], rectangle_height])

    # show_fps(dt)
    pygame.display.update()
    clock.tick(480)