import time

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.perf_counter()
clock = pygame.time.Clock()
run = True
show_velocity = False
show_velocity_x = False
show_velocity_y = False
show_acceleration = False

BACKGROUND = Vector3(29, 29, 29)
FOREGROUND = Vector3(255, 255, 0)
g = Vector2(0, 982/4)

mouse_held = False
projectile_origin = Vector2()
projectile_velocity = Vector2()
projectiles = []
pop_list = []


class Projectile:
    def __init__(self, position: Vector2, velocity: Vector2, radius: float = 4):
        self.position = position
        self.velocity = velocity
        self.radius = radius

    def update(self, dt: float):
        self.velocity += g * dt
        self.position += self.velocity * dt

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, FOREGROUND, self.position, self.radius)


class UIArrow:
    def __init__(self, point: Vector2, vector: Vector2):
        self.point = point
        self.vector = vector

    def draw(self, surface: pygame.Surface, scale: float = 1, color: Vector3 = FOREGROUND):
        # main line
        pygame.draw.aaline(surface, color, self.point, end := self.point + self.vector * scale)

        # left head
        pygame.draw.aaline(surface, color, end, end + self.vector.rotate(-165) * 0.05)

        # right head
        pygame.draw.aaline(surface, color, end, end + self.vector.rotate(165) * 0.05)


while run:

    time_now = time.perf_counter()
    dt = time_now - time_prev
    time_prev = time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode(window_resolution := Vector2(event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectiles.append(Projectile(Vector2() + projectile_origin, Vector2() + projectile_velocity))
            if event.key == pygame.K_a:
                show_acceleration = not show_acceleration
            if event.key == pygame.K_v:
                show_velocity = not show_velocity
            if event.key == pygame.K_x:
                show_velocity_x = not show_velocity_x
            if event.key == pygame.K_y:
                show_velocity_y = not show_velocity_y

    if pygame.key.get_pressed()[pygame.K_c]:
        projectiles.append(Projectile(Vector2() + projectile_origin, Vector2() + projectile_velocity))

    mouse_pos = Vector2(pygame.mouse.get_pos())
    left_click_pressed = pygame.mouse.get_pressed()[0]

    if left_click_pressed and not mouse_held:
        projectile_origin = mouse_pos

    if mouse_held := left_click_pressed:
        projectile_velocity = mouse_pos - projectile_origin

    display.fill(BACKGROUND)

    UIArrow(projectile_origin, projectile_velocity).draw(display)
    UIArrow(projectile_origin, Vector2(projectile_velocity.x, 0)).draw(display, color=Vector3(255, 0, 0))
    UIArrow(projectile_origin, Vector2(0, projectile_velocity.y)).draw(display, color=Vector3(0, 255, 0))

    for projectile in projectiles:
        projectile.update(dt)
        projectile.draw(display)

        if show_velocity:
            UIArrow(projectile.position, projectile.velocity).draw(display)
        if show_velocity_x:
            UIArrow(projectile.position, Vector2(projectile.velocity.x, 0)).draw(display, color=Vector3(255, 0, 0))
        if show_velocity_y:
            UIArrow(projectile.position, Vector2(0, projectile.velocity.y)).draw(display, color=Vector3(0, 255, 0))

        if show_acceleration:
            UIArrow(projectile.position, g).draw(display, color=Vector3(0, 255, 255))

        if not 0 - projectile.radius < projectile.position.x < window_resolution.x + projectile.radius:
            pop_list.append(projectile)

        if not projectile.position.y < window_resolution.y + projectile.radius:
            pop_list.append(projectile)

    for projectile in pop_list:
        if projectile in projectiles:
            projectiles.remove(projectile)

    pop_list = []

    print(len(projectiles))

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
