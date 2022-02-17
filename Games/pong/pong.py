import pygame
import time
from helpers import *

pygame.init()

WINDOW_RESOLUTION = (1200, 800)
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
time_prev = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont(None, WINDOW_RESOLUTION[1] >> 5)
score_font = pygame.font.SysFont('leelawadeeuisemilight', WINDOW_RESOLUTION[1] >> 2)

x_padding = WINDOW_RESOLUTION[0] >> 5
y_padding = x_padding


def draw_background(surface, color):
    # wall_left
    pygame.draw.rect(surface, color, [0, 0, x_padding >> 1, WINDOW_RESOLUTION[1]])

    # wall_right
    pygame.draw.rect(surface, color, [WINDOW_RESOLUTION[0] - (x_padding >> 1), 0, x_padding >> 1, WINDOW_RESOLUTION[1]])

    # roof
    pygame.draw.rect(surface, color, [0, 0, WINDOW_RESOLUTION[0], y_padding >> 1])

    # floor
    pygame.draw.rect(surface, color, [0, WINDOW_RESOLUTION[1] - (y_padding >> 1), WINDOW_RESOLUTION[0], y_padding >> 1])

    # divider
    for y in range(16):
        if y % 2 == 0:
            pygame.draw.rect(surface, color, [WINDOW_RESOLUTION[0] / 2 - ((x_padding >> 2) + (x_padding >> 3)),
                                              y * (WINDOW_RESOLUTION[1] >> 4) + (WINDOW_RESOLUTION[1] >> 5),
                                              x_padding >> 1, (WINDOW_RESOLUTION[1] >> 4)])


def draw_scores(surface, font, score_1, score_2, color):
    score_1_text = font.render(str(score_1), True, color)
    score_2_text = font.render(str(score_2), True, color)
    score_1_rect = score_1_text.get_rect(center=(WINDOW_RESOLUTION[0] >> 2, WINDOW_RESOLUTION[1] >> 1))
    score_2_rect = score_2_text.get_rect(center=(3 * (WINDOW_RESOLUTION[0] >> 2), WINDOW_RESOLUTION[1] >> 1))

    surface.blit(score_1_text, score_1_rect)
    surface.blit(score_2_text, score_2_rect)


score_p1 = 0
score_p2 = 0

player_1 = Paddle([x_padding, WINDOW_RESOLUTION[1] >> 1], 256, [x_padding >> 1, WINDOW_RESOLUTION[1] >> 3], "w", "s",
                  (2, 2, 2))
player_2 = Paddle([WINDOW_RESOLUTION[0] - 1.5 * x_padding, WINDOW_RESOLUTION[1] >> 1], 256,
                  [x_padding >> 1, WINDOW_RESOLUTION[1] >> 3], "UP", "DOWN", (128, 0, 0))
players = [player_1, player_2]

ball_1 = Ball([WINDOW_RESOLUTION[0] >> 1, WINDOW_RESOLUTION[1] >> 1], [200, 134], x_padding >> 1, color_white)
balls = [ball_1]

while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev + (2 >> 31)
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WINDOW_RESOLUTION = [event.w, event.h]
            x_padding = WINDOW_RESOLUTION[0] >> 5
            y_padding = x_padding
            player_1.x = x_padding
            player_1.width = x_padding >> 1
            player_1.height = WINDOW_RESOLUTION[1] >> 3
            player_2.x = WINDOW_RESOLUTION[0] - 1.5 * x_padding
            player_2.width = x_padding >> 1
            player_2.height = WINDOW_RESOLUTION[1] >> 3

    # Keypresses
    keys = pygame.key.get_pressed()
    for player in players:
        if keys[player.up_key] and player.y > y_padding:
            player.move_up(dt)

        if keys[player.down_key] and player.y + player.height < WINDOW_RESOLUTION[1] - y_padding:
            player.move_down(dt)

    for ball in balls:
        if ball.collides_with_paddle(players):
            ball.x_vel *= -1
            ball.update_position(dt)
            print(True)

        if ball.y - ball.radius <= y_padding >> 1 or ball.y + ball.radius >= WINDOW_RESOLUTION[1] - (y_padding >> 1):
            ball.y_vel *= -1
            ball.update_position(dt)

        if ball.x <= 0:
            ball.x = WINDOW_RESOLUTION[0] >> 1
            ball.y = WINDOW_RESOLUTION[1] >> 1
            score_p2 += 1

        if ball.x >= WINDOW_RESOLUTION[0]:
            ball.x = WINDOW_RESOLUTION[0] >> 1
            ball.y = WINDOW_RESOLUTION[1] >> 1
            score_p1 += 1

        ball.update_position(dt)

    # Draw
    display.fill((29, 29, 29))
    draw_background(display, (58, 58, 58))
    draw_scores(display, score_font, score_p1, score_p2, (58, 58, 58))

    for player in players:
        player.draw(display)

    for ball in balls:
        ball.draw(display)

    # show_fps(display, dt, fps_font)
    pygame.display.update()
    if fps > 0:
        clock.tick(fps)
