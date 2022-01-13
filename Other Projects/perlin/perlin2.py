import copy

import pygame
import random
pygame.init()

WINDOW_RESOLUTION = (1000, 1000)
image_resolution = [10, 10]
transform_resolution = [WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1]]
print(transform_resolution)
display = pygame.display.set_mode(WINDOW_RESOLUTION)

run = True
seed = 1


def make_values(seed):
    random.seed(seed)
    values = []
    for y in range(image_resolution[1]):
        values.append([])
        for x in range(image_resolution[0]):
            values[y].append(random.randint(0, 1) / 1)

    return values


values = make_values(seed)


def interpolate(list):
    temp = copy.deepcopy(list)
    for y in range(1, len(list) - 1):
        for x in range(1, len(list[y]) - 1):
            temp[y][x] = round(sum([list[y+1][x+1], list[y][x+1], list[y-1][x+1], list[y+1][x], list[y][x], list[y-1][x], list[y+1][x-1], list[y][x-1], list[y-1][x-1]]) / 9, 1)
    return temp



    count = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                values = interpolate(values)


    for y, container in enumerate(values):
        for x, value in enumerate(container):
            pygame.draw.rect(display, (255 * value, 255 * value, 255 * value), [x * transform_resolution[0], y * transform_resolution[1], transform_resolution[0], transform_resolution[1]])

    pygame.display.update()



