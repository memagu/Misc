import pygame
import time
import sys
import random

pygame.init()
run = True

WINDOW_RESOLUTION = (960, 960)
GAME_RESOLUTION = (16, 16)
TRANSFORM_RESOLUTION_X = WINDOW_RESOLUTION[0] // GAME_RESOLUTION[0]
TRANSFORM_RESOLUTION_Y = WINDOW_RESOLUTION[1] // GAME_RESOLUTION[1]
display = pygame.display.set_mode(WINDOW_RESOLUTION, 0, 32)
count = 0
drawn_graphics = True
framerate = 30

pygame.transform.scale(pygame.image.load("snake head.png"), (TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y))

image_head = pygame.transform.scale(pygame.image.load("snake head.png"), (TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y))
image_segment = pygame.transform.scale(pygame.image.load("snake segment.png"), (TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y))
image_apple = pygame.transform.scale(pygame.image.load("apple.png"), (TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y))


snake_length = 2
snake_length_add = 1
snake_head = GAME_RESOLUTION[0] // 2 * TRANSFORM_RESOLUTION_X, GAME_RESOLUTION[1] // 2 * TRANSFORM_RESOLUTION_X
snake_body = []
direction = (0, 0)
directions = [(0, TRANSFORM_RESOLUTION_Y * -1), (TRANSFORM_RESOLUTION_X * -1, 0),
              (0, TRANSFORM_RESOLUTION_Y), (TRANSFORM_RESOLUTION_X, 0)]
apple = (0, 0)
apple_eaten = True

color_background = (25, 75, 0)
color_green = (0, 255, 0)
color_yellow = (255, 255, 0)
color_black = (0, 0, 0)
color_red = (255, 0, 0)

autopilot = False
grid = False
teleport = False
invincible = False



def add_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def generate_apple_pos(snake_coordinates):
    x = random.randint(0, GAME_RESOLUTION[0] - 1) * TRANSFORM_RESOLUTION_X
    y = random.randint(0, GAME_RESOLUTION[1] - 1) * TRANSFORM_RESOLUTION_Y
    while (x, y) in snake_coordinates:
        x = random.randint(0, GAME_RESOLUTION[0] - 1) * TRANSFORM_RESOLUTION_X
        y = random.randint(0, GAME_RESOLUTION[1] - 1) * TRANSFORM_RESOLUTION_Y
    return x, y


def lose():
    display.fill(color_red)
    time.sleep(2)
    sys.exit()

def draw_grid(w_res, g_res, t_res):
    for x in range(g_res[0]):
        pygame.draw.rect(display, color_black, [x * t_res[0], 0, 1, w_res[1]])

    for y in range(g_res[1]):
        pygame.draw.rect(display, color_black, [0, y * t_res[1], w_res[0], 1])



while run:
    events = pygame.event.get()
    for event in events:
        # print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and direction != directions[2] and not autopilot:
                direction = directions[0]
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction != directions[3] and not autopilot:
                direction = directions[1]
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and direction != directions[0] and not autopilot:
                direction = directions[2]
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and direction != directions[1] and not autopilot:
                direction = directions[3]
            if event.key == pygame.K_t:
                teleport = not teleport
            if event.key == pygame.K_i:
                invincible = not teleport
            if event.key == pygame.K_g:
                grid = not grid
            if event.key == pygame.K_n and framerate > 10:
                framerate -= 10
            if event.key == pygame.K_m:
                framerate += 10
            if event.key == pygame.K_p:
                autopilot = not autopilot

    if autopilot:
        temp = (0, 0)
        if snake_head[1] // TRANSFORM_RESOLUTION_Y % 2 == 1 and snake_head[0] != WINDOW_RESOLUTION[0] - TRANSFORM_RESOLUTION_X and snake_head[0] != 0:
            direction = directions[3]
            # print("right")
        elif snake_head[1] // TRANSFORM_RESOLUTION_Y % 2 == 0 and snake_head[0] != TRANSFORM_RESOLUTION_X and snake_head[0] != 0:
            direction = directions[1]
            # print("left")
        elif snake_head[0] == WINDOW_RESOLUTION[0] - TRANSFORM_RESOLUTION_X or snake_head[0] == TRANSFORM_RESOLUTION_X and direction != directions[0] and snake_head[1] != 0:
            direction = directions[0]
            # print("up")
        elif snake_head[0] == 0 and snake_head[1] == WINDOW_RESOLUTION[1] - TRANSFORM_RESOLUTION_Y:
            direction = directions[3]
            # print("right")
        elif snake_head[0] == 0 and snake_head[1] != WINDOW_RESOLUTION[0] - TRANSFORM_RESOLUTION_X:
            direction = directions[2]
            # print("down")



    snake_head = add_tuple(snake_head, direction)

    if snake_head[0] < 0:
        if teleport or invincible:
            snake_head = add_tuple(snake_head, (WINDOW_RESOLUTION[0], 0))
        else:
            lose()

    if snake_head[0] > WINDOW_RESOLUTION[0] - TRANSFORM_RESOLUTION_X:
        if teleport or invincible:
            snake_head = add_tuple(snake_head, (WINDOW_RESOLUTION[0] * -1, 0))
        else:
            lose()

    if snake_head[1] < 0:
        if teleport or invincible:
            snake_head = add_tuple(snake_head, (0, WINDOW_RESOLUTION[1]))
        else:
            lose()

    if snake_head[1] > WINDOW_RESOLUTION[1] - TRANSFORM_RESOLUTION_Y:
        if teleport or invincible:
            snake_head = add_tuple(snake_head, (0, WINDOW_RESOLUTION[1] * -1))
        else:
            lose()

    snake_body.insert(0, snake_head)
    if len(snake_body) > snake_length:
        snake_body.pop()

    if snake_head == apple:
        snake_length += snake_length_add
        apple_eaten = True

    if apple_eaten and snake_length != GAME_RESOLUTION[0] * GAME_RESOLUTION[1]:
        apple = generate_apple_pos(snake_body)
        apple_eaten = False


    # print(apple)

    display.fill(color_background)

    if drawn_graphics:
        display.blit(image_apple, [*apple, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])

        for segment in snake_body:
            display.blit(image_segment, [*segment, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])

        display.blit(image_head, [*snake_head, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])

    else:
        pygame.draw.rect(display, color_red, [*apple, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])

        for segment in snake_body:
            pygame.draw.rect(display, color_green, [*segment, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])

        pygame.draw.rect(display, color_yellow, [*snake_head, TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y])


    if snake_head in snake_body[1:] and snake_length > 2 and not invincible:
        lose()

    if grid:
        draw_grid(WINDOW_RESOLUTION, GAME_RESOLUTION, (TRANSFORM_RESOLUTION_X, TRANSFORM_RESOLUTION_Y))

    if snake_length == GAME_RESOLUTION[0] * GAME_RESOLUTION[1]:
        lose()


    # print(0 + TRANSFORM_RESOLUTION_X, WINDOW_RESOLUTION[0] - TRANSFORM_RESOLUTION_X, snake_head, direction,snake_head[1] // GAME_RESOLUTION[1] , snake_head[1] // GAME_RESOLUTION[1] % 2)
    pygame.display.update()
    time.sleep(1 / framerate)
