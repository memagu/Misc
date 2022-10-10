import pygame.draw
from pygame import Surface
from pygame.math import Vector3
from random import randint


class Body:
    def __init__(self, mass: float, radius: float, pos: Vector3, vel: Vector3 = Vector3(), color: Vector3 = None):
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.vel = vel
        self.color = color or Vector3(randint(0, 255), randint(0, 255), randint(0, 255))
        self.acc = Vector3()

    def update(self, dt: float):
        self.vel += self.acc * dt
        self.pos += self.vel * dt

    def draw(self, surface: Surface, scale_distance: float, scale_radius: float, center: Vector3 = Vector3()):
        pygame.draw.circle(surface, self.color, (center + self.pos * scale_distance).xy, self.radius * scale_radius)





