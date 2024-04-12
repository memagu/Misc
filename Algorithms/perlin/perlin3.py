import pygame
import random
pygame.init()

WINDOW_RESOLUTION = (2560, 1440)
image_resolution = [1280, 720]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
print(transform_resolution)
display = pygame.display.set_mode(WINDOW_RESOLUTION)

run = True

one_d = True
view_vertical = False
two_d = False
points = True

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)

seed1 = 1
seed2 = 1
depth = 0
resolution = 100
shift = 0


def make_noise(seed):
    random.seed(seed)
    samples = []
    for i in range(4):
        samples.append(random.randint(1, resolution) / resolution)
    return samples


def subdivide(arr, depth, seed):
    if depth <= 0:
        print(f"{len(arr)} {arr}")
        return arr
    random.seed(seed)
    length = len(arr)
    pairs = []

    for i in range(length - 1):
        pairs.append([arr[i], arr[i+1]])

    result = []
    for pair in pairs:
        low = min(pair[0], pair[1])
        high = max(pair[0], pair[1])
        print(low,high)
        new = (random.uniform(low, high))

        if pair == pairs[0]:
            result += [pair[0], new, pair[1]]
        else:
            result += [new, pair[1]]

    return subdivide(result, depth - 1, seed)


def perlin_noise(pos, samples):
    index = pos * (len(samples) - 1)
    i1 = int(index)
    if i1 == len(samples) - 1:
        return samples[i1]
    i2 = int(index) + 1

    k = (samples[i2] - samples[i1])
    m = samples[i1] - k * i1

    return k * index + m



samples1 = subdivide(make_noise(seed1), depth, seed1)
samples2 = subdivide(make_noise(seed2), depth, seed2)


while run:
    transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                depth += 1
                random.seed(seed1)
                samples1 = subdivide(make_noise(seed1), depth, seed1)
                random.seed(seed2)
                samples2 = subdivide(make_noise(seed2), depth, seed2)
            if event.key == pygame.K_s and depth > 0:
                depth -= 1
                random.seed(seed1)
                samples1 = subdivide(make_noise(seed1), depth, seed1)
                random.seed(seed2)
                samples2 = subdivide(make_noise(seed2), depth, seed2)

            if event.key == pygame.K_UP:
                seed1 += 1
                random.seed(seed1)
                samples1 = subdivide(make_noise(seed1), depth, seed1)
            if event.key == pygame.K_DOWN:
                seed1 -= 1
                random.seed(seed1)
                samples1 = subdivide(make_noise(seed1), depth, seed1)

            if event.key == pygame.K_RIGHT:
                seed2 += 1
                random.seed(seed2)
                samples2 = subdivide(make_noise(seed2), depth, seed2)
            if event.key == pygame.K_LEFT:
                seed2 -= 1
                random.seed(seed2)
                samples2 = subdivide(make_noise(seed2), depth, seed2)

            if event.key == pygame.K_1:
                one_d = not one_d
            if event.key == pygame.K_2:
                two_d = not two_d
            if event.key == pygame.K_p:
                points = not points
            if event.key == pygame.K_v:
                view_vertical = not view_vertical

            if event.key == pygame.K_9:
                image_resolution[0] += 10
                image_resolution[1] += 10
            if event.key == pygame.K_0:
                image_resolution[0] -= 10
                image_resolution[1] -= 100

            if event.key == pygame.K_n:
                shift -= 10
            if event.key == pygame.K_m:
                shift += 10

    display.fill(color_black)

    #
    # for i in range(window_resolution[0]):
    #     pygame.draw.rect(display, color_white, [0, window_resolution[1] / 2, window_resolution[0], 1])



    if two_d:
        for x in range(image_resolution[0]):
            p1 = perlin_noise(x / image_resolution[0], samples1)
            for y in range(image_resolution[1]):
                p2 = perlin_noise((y + shift) % image_resolution[1] / image_resolution[1], samples2)

                p = (p1 + p2) / 2
                pygame.draw.rect(display, (p1, 255 * p, 255 - 255 * p), [x * transform_resolution[0], y * transform_resolution[1], transform_resolution[0], transform_resolution[1]])

    if one_d:
        for i in range(WINDOW_RESOLUTION[0]):
            pygame.draw.rect(display, color_white, [i, perlin_noise(i / (WINDOW_RESOLUTION[0]), samples1) * WINDOW_RESOLUTION[1], 1, 1])

    if points and one_d:
        for i, sample in enumerate(samples1):
            pygame.draw.rect(display, color_red, [i * WINDOW_RESOLUTION[0] / (len(samples1) - 1), sample * WINDOW_RESOLUTION[1], 4, 4])

    if view_vertical:
        for i in range(WINDOW_RESOLUTION[1]):
            pygame.draw.rect(display, color_white, [perlin_noise(i / (WINDOW_RESOLUTION[1]), samples2) * WINDOW_RESOLUTION[0], i, 1, 1])

    if points and view_vertical:
        for i, sample in enumerate(samples2):
            pygame.draw.rect(display, color_red, [sample * WINDOW_RESOLUTION[0], i * WINDOW_RESOLUTION[1] / (len(samples2) - 1), 4, 4])








        # for i in range(window_resolution[1]):
        #     pygame.draw.rect(display, color_white, [perlin_noise(i / (window_resolution[1]), samples2) * 100 + 600, i, 1, 1])



    pygame.display.update()

