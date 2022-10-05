import pygame
import time

pygame.init()

window_resolution = pygame.math.Vector2(1200, 900)
origin = pygame.math.Vector2(window_resolution.x / 2, window_resolution.y / 2)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480 # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", int(window_resolution.y) >> 5)


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


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    text = f"FPS: {int(1 / delta_time)}"
    fps_text = font.render(text, True, text_color)
    fps_outline = font.render(text, True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


class Curve:
    def __init__(self, diff_func, x, y):
        self.diff_func = diff_func
        self.x = x
        self.y = y

    def draw(self, n_iterations, step_size):
        right_x, left_x = self.x, self.x
        right_y, left_y = self.y, self.y

        for _ in range(n_iterations):
            last_right_x = right_x
            last_right_y = right_y
            right_y += y_(right_x, right_y) * step_size
            right_x += step_size

            right_point_start = pygame.math.Vector2(last_right_x, max(min(last_right_y * -1, window_resolution.y),
                                                          -window_resolution.y)) * draw_scale + origin
            right_point_end = pygame.math.Vector2(right_x, max(min(right_y * -1, window_resolution.y),
                                                   -window_resolution.y)) * draw_scale + origin

            last_left_x = left_x
            last_left_y = left_y
            left_y += y_(left_x, left_y) * -step_size
            left_x -= step_size

            left_point_start = pygame.math.Vector2(last_left_x, max(min(last_left_y * -1, window_resolution.y),
                                                          -window_resolution.y)) * draw_scale + origin
            left_point_end = pygame.math.Vector2(left_x, max(min(left_y * -1, window_resolution.y),
                                                   -window_resolution.y)) * draw_scale + origin

            pygame.draw.aaline(display, Color.white, right_point_start, right_point_end)
            pygame.draw.aaline(display, Color.white, left_point_start, left_point_end)


def draw_grid():
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


def y_(x, y):
    # equation = 4 - x * y
    equation = x + y
    return min(max(equation, -2 ** 31), 2 ** 31 - 1)


n_iterations = 1000
step_size = 0.1
draw_scale = 100

c1 = Curve(y_, 0, -1)

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
            window_resolution = pygame.math.Vector2(event.w, event.h)
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        draw_scale = min(draw_scale + 10 * dt, max(window_resolution) / 2)
    if keys[pygame.K_DOWN]:
        draw_scale = max(draw_scale - 10 * dt, 1)
    if keys[pygame.K_w]:
        origin.y += 50 * dt
    if keys[pygame.K_s]:
        origin.y -= 50 * dt
    if keys[pygame.K_a]:
        origin.x += 50 * dt
    if keys[pygame.K_d]:
        origin.x -= 50 * dt

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

    pygame.draw.circle(display, Color.red, origin, 4)

    draw_grid()

    c1.draw(n_iterations, step_size)

    show_fps(dt)
    pygame.display.update()
    if fps > 0:
        clock.tick(fps)
