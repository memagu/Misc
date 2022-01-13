import pygame
import time
import random

pygame.init()

resolution = [800, 600]
display = pygame.display.set_mode(resolution)
framerate = 60
run = True

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

pipe_thickness = 50
gravity = 800


def sign(a):
    return (a > 0) - (a < 0)


class Object:
    def __init__(self, mass, velocity, radius, position):
        self.mass = mass
        self.velocity = velocity
        self.radius = radius
        self.diameter = radius * 2
        self.position = [position[0] - radius, position[1] - radius]
        self.in_collision = False

    def update_position(self):
        self.position = [self.position[0] + self.velocity, self.position[1]]

    def check_collision(self, other):
        if (self.position[0] == other.position[0] + other.diameter or self.position[0] + self.diameter ==
            other.position[0]) and not self.in_collision:
            self.in_collision = True
            return other
        self.in_collision = False
        return None

    def collide(self, other):
        m1 = self.mass
        v1 = self.velocity
        m2 = other.mass
        v2 = other.velocity
        p1 = ((m1 - m2) / (m1 + m2)) * v1
        p2 = ((2 * m2) / (m1 + m2)) * v2
        v = p1 + p2
        self.velocity = v

    def draw(self):
        pygame.draw.rect(display, color_white, [*self.position, self.diameter, self.diameter])


o1 = Object(10, 1, 20, [200, 300])
o2 = Object(10, -1, 20, [600, 300])

objects = [o1, o2]

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    display.fill(color_black)

    for i, object_self in enumerate(objects):
        for object_other in objects:
            if object_self == object_other:
                pass
            if object_self.check_collision(object_other):
                object_self.collide(object_other)
        object_self.update_position()
        object_self.draw()

    pygame.display.update()
    time.sleep(1 / framerate)
