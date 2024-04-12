import random
import pygame
from pygame.math import Vector2, Vector3
from typing import Optional


class PepperedMoth:
    def __init__(self, radius, pos, color: Optional[Vector3] = None):
        self.radius = radius
        self.pos = pos
        self.color = color or random.choice((Vector3(1, 1, 1), Vector3(0, 0, 0)))

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def reproduce(self):
        return PepperedMoth(self.radius, [random.randint(150, 1050), random.randint(150, 750)], self.color)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color * 255, self.pos, self.radius)
