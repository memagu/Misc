import pygame
import time

pygame.init()

window_resolution = pygame.math.Vector2(1200, 900)
origin = pygame.math.Vector2(window_resolution.x / 2, window_resolution.y / 2)
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
    gray = (128, 128, 128)
    kc_gray = (29, 29, 29)


# Text
pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", int(window_resolution.y / 32))


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    text = f"FPS: {int(1 / delta_time)}"
    fps_text = font.render(text, True, text_color)
    fps_outline = font.render(text, True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


def y_(x, y):
    return 4 - x**2 * y**3


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
            window_resolution = pygame.math.Vector2(event.w, event.h)
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        draw_scale += 10 * dt
    if keys[pygame.K_DOWN]:
        draw_scale -= 10 * dt
    if keys[pygame.K_w]:
        origin.y -= 50 * dt
    if keys[pygame.K_s]:
        origin.y += 50 * dt
    if keys[pygame.K_a]:
        origin.x -= 50 * dt
    if keys[pygame.K_d]:
        origin.x += 50 * dt

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.math.Vector2(pygame.mouse.get_pos())
    if not mouse_buttons[0]:
        select_pos = mouse_position
        select_origin = origin

    else:
        delta_pos = mouse_position - select_pos
        origin = select_origin + delta_pos

    # Draw
    display.fill(Color.kc_gray)

    pygame.draw.circle(display, Color.red, origin, 3)

    x_start = min(-(int(origin.x) // int(draw_scale)), 0)
    x_end = max(int(window_resolution.x - origin.x) // int(draw_scale), 0)

    for i in range(x_start, x_end + 1):
        grid_x = i * draw_scale + origin.x
        pygame.draw.aaline(display, Color.gray, (grid_x, 0), (grid_x, window_resolution.y))

    y_start = min(-(int(origin.y) // int(draw_scale)), 0)
    y_end = max(int(window_resolution.y - origin.y) // int(draw_scale), 0)

    for i in range(y_start, y_end + 1):
        draw_y = i * draw_scale + origin.y
        pygame.draw.aaline(display, Color.gray, (0, draw_y), (window_resolution.x, draw_y))

    for i in range(-n_iterations, n_iterations):
        last_x = x
        last_y = y
        y += y_(x, y) * step_size
        x += step_size

        point_start = pygame.math.Vector2(last_x, max(min(last_y * -1, window_resolution.y),
                                                      -window_resolution.y)) * draw_scale + origin
        point_end = pygame.math.Vector2(x, max(min(y * -1, window_resolution.y),
                                               -window_resolution.y)) * draw_scale + origin

        pygame.draw.aaline(display, Color.white, point_start, point_end)

    show_fps(dt)
    pygame.display.update()
    if fps > 0:
        clock.tick(fps)
