from pathlib import Path
import time

import pygame as pg
from pygame import Vector2, Vector3

import data_processing as dp
from data_visualizer import DataVisualiser

pg.init()

COLOR_BACKGROUND = Vector3()

SPEED_SLOW = 1
SPEED_NORMAL = 8
SPEED_FAST = 64

blue = DataVisualiser(
    dp.load_float_csv(Path("../data/blue.data"), '\t'),
    Vector2(16),
    (dp.normalize, dp.filter_highpass)
).scale_rgba(0, 0, 1, 1)

red = DataVisualiser(
    dp.load_float_csv(Path("../data/red.data"), '\t'),
    Vector2(16),
    (dp.normalize, dp.filter_highpass)
).scale_rgba(1, 0, 0, 1)

window_resolution = Vector2(1200, 900)
display = pg.display.set_mode(window_resolution, pg.RESIZABLE)
pg.display.set_caption(Path(__file__).name)

time_prev = time.time()
draw_scale = 4

run = True

while run:

    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                run = False
                break

            case pg.VIDEORESIZE:
                window_resolution.xy = event.w, event.h
                display = pg.display.set_mode(window_resolution, pg.RESIZABLE)

            case pg.KEYDOWN:
                match event.key:
                    case pg.K_COMMA:
                        draw_scale -= 0.5

                    case pg.K_PERIOD:
                        draw_scale += 0.5

                    case pg.K_MINUS:
                        draw_scale = 1

                    case pg.K_SPACE:
                        merged_data = dp.merge_data(
                            blue.data,
                            red.data,
                            blue.data_intersection_indices(red),
                            red.data_intersection_indices(blue)
                        )
                        dp.save_float_csv(merged_data, delimiter='\t')
                        print(f"Saved data with shape: {merged_data.shape}")

                    case _:
                        continue

            case _:
                continue

    keys = pg.key.get_pressed()

    speed = SPEED_NORMAL
    if keys[pg.K_LSHIFT]:
        speed = SPEED_FAST
    if keys[pg.K_LALT]:
        speed = SPEED_SLOW

    if keys[pg.K_w]:
        blue.position += Vector2(0, -1) * speed * dt

    if keys[pg.K_s]:
        blue.position += Vector2(0, 1) * speed * dt

    if keys[pg.K_a]:
        blue.position += Vector2(-1, 0) * speed * dt

    if keys[pg.K_d]:
        blue.position += Vector2(1, 0) * speed * dt

    if keys[pg.K_UP]:
        red.position += Vector2(0, -1) * speed * dt

    if keys[pg.K_DOWN]:
        red.position += Vector2(0, 1) * speed * dt

    if keys[pg.K_LEFT]:
        red.position += Vector2(-1, 0) * speed * dt

    if keys[pg.K_RIGHT]:
        red.position += Vector2(1, 0) * speed * dt

    display.fill(COLOR_BACKGROUND)

    blue.draw(display, draw_scale)
    red.draw(display, draw_scale)

    pg.display.update()
