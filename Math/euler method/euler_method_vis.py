import pygame
import time

pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)


# Text
pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


def y_(x, y):
    return 4 - x * y


n_iterations = 10000
step_size = 0.01

draw_scale = 1 / step_size

while run:
    x = 0
    y = 1

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            draw_scale += 10 * dt
        if keys[pygame.K_DOWN]:
            draw_scale -= 10 * dt

    # Draw
    display.fill(Color.black)

    for i in range(window_resolution[0]):
        g_x_r = i * draw_scale + window_resolution[1] // 2
        g_x_l = -i * draw_scale + window_resolution[1] // 2
        print(g_x_r)
        pygame.draw.aaline(display, Color.white, (g_x_r, 0), (g_x_r, window_resolution[1]))
        pygame.draw.aaline(display, Color.white, (g_x_l, 0), (g_x_l, window_resolution[1]))

    for i in range(window_resolution[1]):
        g_y_u = -i * draw_scale + window_resolution[0] // 2
        g_y_d = i * draw_scale + window_resolution[0] // 2
        pygame.draw.aaline(display, Color.white, (0, g_y_u), (window_resolution[0], g_y_u))
        pygame.draw.aaline(display, Color.white, (0, g_y_d), (window_resolution[0], g_y_d))

    for i in range(n_iterations):
        last_x = x
        last_y = y
        y += y_(x, y) * step_size
        x += step_size

        d_last_x = last_x * draw_scale + window_resolution[0] // 2
        d_last_y = max(min((last_y * -1), window_resolution[1]), -window_resolution[1]) * draw_scale + window_resolution[1] // 2
        d_x = x * draw_scale + window_resolution[0] // 2
        d_y = max(min(y * -1, window_resolution[1]), -window_resolution[1]) * draw_scale + window_resolution[0] // 2

        pygame.draw.aaline(display, Color.white, (d_last_x, d_last_y), (d_x, d_y))

    show_fps(dt)
    pygame.display.update()
    if fps > 0:
        clock.tick(fps)
