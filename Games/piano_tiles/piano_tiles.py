from dataclasses import dataclass
from pathlib import Path
from random import randint

import pygame
from pygame.math import Vector2

pygame.init()

WINDOW_RESOLUTION = Vector2(1024, 256)
DISPLAY = pygame.display.set_mode(WINDOW_RESOLUTION)
pygame.display.set_caption(Path(__file__).name)

FRAME_RATE = 240
CLOCK = pygame.time.Clock()

TILES = 16
ROW_HEIGHT = WINDOW_RESOLUTION.y / 4
TILE_WIDTH = WINDOW_RESOLUTION.x / TILES
TILE_HEIGHT = ROW_HEIGHT
SCORE_LINE = 7 * WINDOW_RESOLUTION.x / 8
HIT_LINE = TILE_WIDTH / 2


@dataclass
class Tile:
    x: float
    y: float
    width: float = TILE_WIDTH
    height: float = TILE_HEIGHT
    active: bool = False


def draw_grid() -> None:
    pygame.draw.line(DISPLAY, (255, 255, 255), (SCORE_LINE, 0), (SCORE_LINE, 256))

    for i in range(1, 4):
        y = i * WINDOW_RESOLUTION.y / 4
        pygame.draw.line(DISPLAY, (255, 255, 255), (0, y), (SCORE_LINE, y))

    pygame.draw.line(DISPLAY, (255, 0, 0), (HIT_LINE, 0), (HIT_LINE, 256))


tiles = [
    Tile(
        SCORE_LINE + i * TILE_WIDTH,
        randint(0, 3) * ROW_HEIGHT,
        TILE_WIDTH,
        TILE_HEIGHT,
        False
    ) for i in range(TILES + 1)
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    DISPLAY.fill((29, 29, 29))

    for i, tile in enumerate(tiles):
        # Aktivera var 3:e tile
        if i % 3 == 0 and tile.x >= SCORE_LINE - TILE_WIDTH:
            tile.active = True

        # Simulera att man prickar en tile
        if tile.x <= HIT_LINE <= tile.x + tile.width:
            tile.active = False

        # Färglägg olika beroende på aktiv/inaktiv och om utanför spelplan
        if tile.active and tile.x <= SCORE_LINE - TILE_WIDTH:
            pygame.draw.rect(DISPLAY, (255, 255, 255), (tile.x, tile.y, tile.width, tile.height))
        else:
            pygame.draw.rect(DISPLAY, (64, 64, 64), (tile.x, tile.y, tile.width, tile.height))

        # Flytta tilen och "resetta" om utanför skärm
        tile.x -= 1
        if tile.x + tile.width < 0:
            tile.x = WINDOW_RESOLUTION.x
            tile.y = randint(0, 3) * ROW_HEIGHT

    # Rita ut spelplanen
    draw_grid()

    pygame.display.update()

    if max(0, FRAME_RATE):
        CLOCK.tick(FRAME_RATE)
