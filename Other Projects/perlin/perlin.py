import pygame
import random

pygame.init()

WINDOW_RESOLUTION = (1200, 1200)
image_resolution = [10, 10]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION)

one_d = True
two_d = False

color_white = (255, 255, 255)
color_black = (0, 0, 0)

run = True
seed1 = 1
seed2 = 1


def make_samples(sample_size, seed):
    random.seed(seed)
    samples = []
    for i in range(sample_size):
        samples.append(random.randint(0, 10000) / 10000)

    return samples


samples1 = make_samples(3, 10)
samples2 = make_samples(3, 10)


def perlin_noise(pos, samples):
    index = pos * (len(samples) - 1)
    i1 = int(index)
    if i1 == len(samples) - 1:
        return samples[i1]
    i2 = int(index) + 1

    k = (samples[i2] - samples[i1])
    m = samples[i1] - k * i1

    return k * index + m


while run:

    transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
    samples1 = make_samples(10, seed1)
    samples2 = make_samples(10, seed2)
    print(seed1, seed2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                one_d = not one_d
                print(one_d)
            if event.key == pygame.K_2:
                print(two_d)
                two_d = not two_d
            if event.key == pygame.K_UP:
                seed1 += 1
            if event.key == pygame.K_DOWN:
                seed1 -= 1
            if event.key == pygame.K_LEFT:
                seed2 -= 1
            if event.key == pygame.K_RIGHT:
                seed2 += 1





            if event.key == pygame.K_9:
                image_resolution[0] += 10
                image_resolution[1] += 10
            if event.key == pygame.K_0:
                image_resolution[0] -= 10
                image_resolution[1] -= 100



    pygame.display.update()
    display.fill(color_black)


    if two_d:
        for x in range(image_resolution[0]):
            p1 = perlin_noise(x / image_resolution[0], samples1)
            for y in range(image_resolution[1]):
                p2 = perlin_noise(y / image_resolution[1], samples2)

                p = (p1 + p2) / 2
                pygame.draw.rect(display, (255 * p, 255 * p, 255 * p), [x * transform_resolution[0], y * transform_resolution[1], transform_resolution[0], transform_resolution[1]])

    if one_d:
        for i in range(WINDOW_RESOLUTION[0]):
            pygame.draw.rect(display, color_white, [i, perlin_noise(i / (WINDOW_RESOLUTION[0]), samples1) * 100 + 600, 1, 1])

        for i in range(WINDOW_RESOLUTION[1]):
            pygame.draw.rect(display, color_white, [perlin_noise(i / (WINDOW_RESOLUTION[1]), samples2) * 100 + 600, i, 1, 1])







