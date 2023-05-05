import random
import time

import pygame
from pygame.math import Vector2, Vector3

from quadtree import DataPoint, Rect, Quadtree

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 0
time_prev = time.time()
clock = pygame.time.Clock()
run = True


class Ball:
    def __init__(self,
                 pos: Vector2 = Vector2(),
                 vel: Vector2 = Vector2(),
                 acc: Vector2 = Vector2(),
                 radius: int = 1,
                 color: Vector3 = Vector3(255, 0, 0)):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"Ball(pos={self.pos}, vel={self.vel}, acc={self.acc}, radius={self.radius}, color={self.color})"

    def __str__(self):
        return self.__repr__()

    def update(self, dt: float) -> None:
        self.pos += self.vel * dt
        self.vel += self.acc * dt

    def intersects(self, other) -> bool:
        return (self.pos - other.pos).magnitude_squared() <= (self.radius + other.radius) ** 2

    def draw(self, surface: pygame.surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


def draw_quadtree(qt: Quadtree) -> None:
    pygame.draw.lines(display, (0, 0, 0), False,
                      ((qt.bbox.x, qt.bbox.y + qt.bbox.h), (qt.bbox.x, qt.bbox.y), (qt.bbox.x + qt.bbox.w, qt.bbox.y)))
    # pygame.draw.rect(display, (255, 255, 255), qt.bbox, 1)
    if qt.nw is not None:
        draw_quadtree(qt.nw)
        draw_quadtree(qt.ne)
        draw_quadtree(qt.sw)
        draw_quadtree(qt.se)
        return


balls = [Ball(Vector2(random.randint(0, window_resolution.x), random.randint(0, window_resolution.y)),
              Vector2(random.randint(-128, 128), random.randint(-128, 128)))
         for _ in range(2 ** 14)]

detect_rect_size = 64
attract = False

while run:
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            window_resolution.xy = event.w, event.h
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         pass

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_1]:
        #     pass
        attract = keys[pygame.K_SPACE]

        if event.type == pygame.MOUSEWHEEL:
            detect_rect_size += event.y * 8

    qt = Quadtree(Rect(0, 0, *window_resolution.xy))
    for ball in balls:
        if qt.bbox.contains(ball_data_point := DataPoint(ball.pos.x, ball.pos.y, ball)):
            qt.insert(ball_data_point)

    mouse_pos = Vector2(pygame.mouse.get_pos())
    detect_rect = Rect(mouse_pos.x - detect_rect_size / 2, mouse_pos.y - detect_rect_size / 2, detect_rect_size,
                       detect_rect_size)

    for ball_data_point in qt.query_region(detect_rect):
        ball = ball_data_point.data
        ball.color = (0, 255, 0)
        ball.acc = (mouse_pos - ball.pos) * 8 * attract

    display.fill(Vector3(29, 29, 29))

    draw_quadtree(qt)

    for ball in balls:
        if not (0 <= ball.pos.x - ball.radius and ball.pos.x + ball.radius <= window_resolution.x):
            ball.vel.x *= -1
            ball.acc.x *= -1
        if not (0 <= ball.pos.y - ball.radius and ball.pos.y + ball.radius <= window_resolution.y):
            ball.vel.y *= -1
            ball.acc.y *= -1

        ball.update(dt)

        ball.acc = ball.vel * -0.9

        ball.draw(display)
        ball.color = (255, 0, 0)

    pygame.draw.rect(display, (0, 255, 0), (detect_rect.x, detect_rect.y, detect_rect.w, detect_rect.h), 1)

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
