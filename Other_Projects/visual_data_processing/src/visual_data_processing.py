from pathlib import Path
import time

import pygame as pg

import data_processing as dp
from data_visualization import DataVisualiser

pg.init()

COLOR_BACKGROUND = pg.Vector3()

SPEED_FAST = 64
SPEED_NORMAL = 8
SPEED_SLOW = 1


def main() -> None:
    window_resolution = pg.Vector2(1200, 900)
    display = pg.display.set_mode(window_resolution, pg.RESIZABLE)
    pg.display.set_caption(Path(__file__).name)

    run = True

    blue = DataVisualiser(
        dp.load_float_csv(Path("../data/blue.data"), '\t'),
        pg.Vector2(16),
        (dp.normalize, dp.filter_highpass)
    ).scale_rgba(0, 0, 1, 1)

    red = DataVisualiser(
        dp.load_float_csv(Path("../data/red.data"), '\t'),
        pg.Vector2(16),
        (dp.normalize, dp.filter_highpass)
    ).scale_rgba(1, 0, 0, 1)

    draw_scale = 800 // (blue.data.shape[0])

    time_prev = time.time()

    while run:

        time_now = time.time()
        dt, time_prev = time_now - time_prev, time_now

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
                            draw_scale /= 1.25

                        case pg.K_PERIOD:
                            draw_scale *= 1.25

                        case pg.K_MINUS:
                            draw_scale = 1

                        case pg.K_SPACE:
                            blue.save_intersection(red)

                        case _:
                            continue

                case pg.MOUSEWHEEL:
                    match event.y:
                        case 1:
                            draw_scale *= 1.05

                        case -1:
                            draw_scale /= 1.05

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
            blue.position += pg.Vector2(0, -1) * speed * dt

        if keys[pg.K_a]:
            blue.position += pg.Vector2(-1, 0) * speed * dt

        if keys[pg.K_s]:
            blue.position += pg.Vector2(0, 1) * speed * dt

        if keys[pg.K_d]:
            blue.position += pg.Vector2(1, 0) * speed * dt

        if keys[pg.K_UP]:
            red.position += pg.Vector2(0, -1) * speed * dt

        if keys[pg.K_LEFT]:
            red.position += pg.Vector2(-1, 0) * speed * dt

        if keys[pg.K_DOWN]:
            red.position += pg.Vector2(0, 1) * speed * dt

        if keys[pg.K_RIGHT]:
            red.position += pg.Vector2(1, 0) * speed * dt

        display.fill(COLOR_BACKGROUND)

        blue.draw(display, draw_scale)
        red.draw(display, draw_scale)

        pg.display.update()


if __name__ == '__main__':
    main()
