import pygame
import time
import random
from pygame.math import Vector3
from pygame.math import Vector2
import math
from typing import List
from collections import deque

from peppered_moth import PepperedMoth
from util import *

pygame.init()

SEED = 30
ANGLE_VELOCITY = 0.1

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('leelawadeeuisemilight', 16)

random.seed(SEED)

reproduce_counter = 0
death_counter = 0
average = deque(maxlen=20)


def make_peppermoths(amount: int) -> List[PepperedMoth]:
    return [PepperedMoth(10, Vector2(random.randint(150, 1050), random.randint(150, 750))) for _ in range(amount)]


def population_reproduction(population: List[PepperedMoth], p_reproduce: float = 0.05) -> None:
    global reproduce_counter
    for i in range(len(population)):
        if p_reproduce >= random.random():
            population.append(population[i].reproduce())
            reproduce_counter += 1


def population_reduction(population: List[PepperedMoth]) -> None:
    global death_counter
    i = 0
    while i < len(population):
        p_death = abs(population[i].color[0] - sin_angle) / 20
        average.append(p_death)
        if p_death >= random.uniform(0, 1):
            population.pop(i)
            death_counter += 1
            continue
        i += 1


population = make_peppermoths(10_000)

angle = math.pi / 2

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
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = Vector2(event.w, event.h)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_1:

    sin_angle = math.sin(angle) * 0.5 + 0.5
    angle += ANGLE_VELOCITY * dt

    display.fill(sin_angle * WHITE)

    for pepper_moth in population:
        pepper_moth.draw(display)

    population_reproduction(population)

    population_reduction(population)

    display.blit(font.render(f'Reproduce counter: {reproduce_counter}', True, RED), (130, 0))
    display.blit(font.render(f'Death counter: {death_counter}', True, RED), (600, 0))
    display.blit(font.render(f'Average p_death: {sum(average) / len(average):.2%}', True, RED), (600, 40))
    display.blit(font.render(f'Population size: {len(population)}', True, RED), (130, 40))

    show_fps(display, font, dt)
    pygame.display.update()
    clock.tick(60)
