import time

import pygame
from pygame.math import Vector2, Vector3

FRAMERATE = 480

COLOR_BLACK = Vector3()
COLOR_RED = Vector3(255, 0, 0)
COLOR_WHITE = Vector3(255, 255, 255)
COLOR_ORANGE = Vector3(255, 128, 0)
COLOR_PURPLE = Vector3(255, 0, 255)
COLOR_GREEN = Vector3(0, 255, 0)
COLOR_DARK_GREEN = Vector3(0, 128, 0)
COLOR_CYAN = Vector3(0, 255, 255)
COLOR_KC_GRAY = Vector3(29, 29, 29)

pygame.init()


def calculate_vertex(vertex: Vector2, origin: Vector2, scale: float, angle_degrees: float) -> Vector2:
    return origin + (vertex * scale).rotate(angle_degrees)


def calculate_vertices(vertices: tuple[Vector2, ...], origin: Vector2, scale: float, angle_degrees: float) -> tuple[
    Vector2, ...]:
    return tuple(calculate_vertex(vertex, origin, scale, angle_degrees) for vertex in vertices)


class Arrow:
    _body = (Vector2(0, 0), Vector2(6, 0))
    _left_head = (Vector2(0, 0), Vector2(1, -1))
    _right_head = (Vector2(0, 0), Vector2(1, 1))

    def __init__(self, origin: Vector2, scale: float, angle_degrees: float, color: Vector3):
        self.origin = origin
        self.scale = scale
        self.angle_degrees = angle_degrees
        self.color = color

    def draw(self):
        pygame.draw.aaline(display, self.color,
                           *calculate_vertices(self.__class__._body, self.origin, self.scale, self.angle_degrees))
        pygame.draw.aaline(display, self.color,
                           *calculate_vertices(self.__class__._left_head, self.origin, self.scale, self.angle_degrees))
        pygame.draw.aaline(display, self.color,
                           *calculate_vertices(self.__class__._right_head, self.origin, self.scale, self.angle_degrees))


class HorseshoeMagnet:
    _south_polygon = (Vector2(0, 0),
                      Vector2(1, 0),
                      Vector2(1, 5),
                      Vector2(3, 5),
                      Vector2(3, 6),
                      Vector2(0, 6))

    _north_polygon = (Vector2(6, 0),
                      Vector2(5, 0),
                      Vector2(5, 5),
                      Vector2(3, 5),
                      Vector2(3, 6),
                      Vector2(6, 6))

    _arrow_origins = (Vector2(2, 0),
                      Vector2(2, 1),
                      Vector2(2, 2),
                      Vector2(2, 3),
                      Vector2(2, 4))

    def __init__(self, pos: Vector2, scale: float, angle_degrees: float):
        self.pos = pos
        self.scale = scale
        self.angle_degrees = angle_degrees

    def draw(self):
        pygame.draw.polygon(display, COLOR_WHITE,
                            calculate_vertices(self.__class__._south_polygon, self.pos, self.scale, self.angle_degrees))
        pygame.draw.polygon(display, COLOR_RED,
                            calculate_vertices(self.__class__._north_polygon, self.pos, self.scale, self.angle_degrees))

        for arrow_origin in self.__class__._arrow_origins:
            Arrow(calculate_vertex(arrow_origin, self.pos, self.scale, self.angle_degrees), self.scale / 3,
                  self.angle_degrees, COLOR_ORANGE).draw()


class Conductor:
    _cross_lurd = (Vector2(-1, 1), Vector2(1, -1))
    _cross_ldru = (Vector2(-1, -1), Vector2(1, 1))

    def __init__(self, center: Vector2, radius: float, current_out_of_screen: bool, powered: bool):
        self.center = center
        self.radius = radius
        self.current_out_of_screen = current_out_of_screen
        self.powered = powered

    def draw(self):
        pygame.draw.circle(display, COLOR_PURPLE, self.center, self.radius)

        if not self.powered:
            return

        if self.current_out_of_screen:
            pygame.draw.circle(display, COLOR_WHITE, self.center, self.radius / 4)
        else:
            pygame.draw.aaline(display, COLOR_WHITE,
                               *calculate_vertices(self.__class__._cross_lurd, self.center, self.radius / 4, 0))
            pygame.draw.aaline(display, COLOR_WHITE,
                               *calculate_vertices(self.__class__._cross_ldru, self.center, self.radius / 4, 0))

        for i in range(2, 20):
            magnetic_field_radius = self.radius * i
            pygame.draw.circle(display, COLOR_GREEN, self.center, magnetic_field_radius, 1)
            for j in range(8):
                angle = 360 / 8 * j
                Arrow(self.center + Vector2(0, magnetic_field_radius).rotate(angle + 180 * self.current_out_of_screen),
                      self.radius / 16, angle, COLOR_CYAN).draw()


window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

time_prev = time.time()
clock = pygame.time.Clock()
run = True

m = HorseshoeMagnet(Vector2(400, 400), 50, -90)
m2 = HorseshoeMagnet(Vector2(800, 800), 50, 0)
# a = Arrow(Vector2(400, 400), 100, 0, COLOR_ORANGE)
c = Conductor(Vector2(400, 400), 50, False, False)

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                c.current_out_of_screen = not c.current_out_of_screen

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                c.powered = not c.powered

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        c.center = Vector2(pygame.mouse.get_pos())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        m.pos = Vector2(pygame.mouse.get_pos())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        m.angle_degrees = pygame.mouse.get_pos()[0]

    display.fill(COLOR_KC_GRAY)

    m.draw()
    m2.draw()
    c.draw()

    pygame.display.update()
    if abs(FRAMERATE):
        clock.tick(FRAMERATE)
