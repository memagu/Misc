import pygame
import time
import math

pygame.init()

WINDOW_RESOLUTION = (2560, 1440)
image_resolution = [1200, 900]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()

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


x = WINDOW_RESOLUTION[0] / 2
y = WINDOW_RESOLUTION[1] / 2

w = 8
h = 8

x_vel = 100
y_vel = 100

angle = 0
angle_vel = 1

trail_surface = pygame.Surface(WINDOW_RESOLUTION, pygame.SRCALPHA, 32)

trail = []
trail_length = 2048

while run:

    pos_prev = x, y

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev + (2 ** -63)
    time_prev = time_now

    angle += angle_vel * dt
    # x += x_vel * dt
    # y += y_vel * dt

    # if not 0 < x < WINDOW_RESOLUTION[0] - w:
    #     x_vel *= -1
    #     x += x_vel * dt
    #
    # if not 0 < y < WINDOW_RESOLUTION[1] - h:
    #     y_vel *= -1
    #     y += y_vel * dt


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

        mousepos = pygame.mouse.get_pos()

        x, y = mousepos

    trail.append((pos_prev, (x, y), rainbow(angle)))
    if trail_length < len(trail):
        trail.pop(0)

    display.fill(color_black)

    # pygame.draw.circle(trail_surface, rainbow(angle), [x + w / 2, y + h / 2], (w + h) / 16)
    for trail_segment in trail:
        pygame.draw.aaline(display, trail_segment[2], (trail_segment[0][0] + w / 2, trail_segment[0][1] + h / 2), (trail_segment[1][0] + w / 2, trail_segment[1][1] + h / 2))
    pygame.draw.circle(display, rainbow(angle), mousepos, w)
    # display.blit(trail_surface, (0, 0))
    # pygame.draw.rect(display, rainbow(angle), [x, y, w, h])

    show_fps(dt)
    pygame.display.update()
    clock.tick(480)
