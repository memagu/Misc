import math
import pygame
import time

from typing import Tuple


class PendulumArm:
    def __init__(self, origin_point: Tuple[float, float], length: float = 1, mass: float = 2, angle: float = 0,
                 angle_velocity: float = 0, angle_acceleration: float = 0):
        self.origin_point = origin_point
        self.length = length
        self.mass = mass
        self.angle = angle
        self.angle_velocity = angle_velocity
        self.angle_acceleration = angle_acceleration
        self.previous_end_point = (math.cos(self.angle) * self.length, math.sin(self.angle) * self.length)

    def end_point(self, scale: float = 1) -> Tuple[float, float]:
        x = self.origin_point[0] + math.sin(self.angle) * self.length * scale
        y = self.origin_point[1] + math.cos(self.angle) * self.length * scale
        return x, y

    def update(self, dt, elasticity: float = 1):
        self.previous_end_point = self.end_point()
        self.angle_velocity += self.angle_acceleration * dt * elasticity
        self.angle += self.angle_velocity * dt * elasticity

    def draw(self, surface: pygame.Surface, color: Tuple[float, float, float] = (255, 255, 255), draw_scale: float = 1):
        pygame.draw.aaline(surface, color, self.origin_point, self.end_point(scale=draw_scale))


class DoublePendulum:
    def __init__(self, arm1: PendulumArm, arm2: PendulumArm, g=9.82, draw_scale: float = 1):
        self.arm1 = arm1
        self.arm2 = arm2
        self.g = g
        self.draw_scale = draw_scale

    def calc_inner_arm_acceleration(self):
        p1 = -self.g * (2 * self.arm1.mass + self.arm2.mass) * math.sin(self.arm1.angle)
        p2 = self.arm2.mass * self.g * math.sin(self.arm1.angle * self.arm2.angle)
        p3 = 2 * math.sin(self.arm1.angle - self.arm2.angle) * self.arm2.mass * (self.arm2.angle_velocity ** 2 * self.arm2.length + self.arm1.angle_velocity ** 2 * self.arm1.length * math.cos(self.arm1.angle - self.arm2.angle))
        d = self.arm1.length * (2 * self.arm1.mass + self.arm2.mass - self.arm2.mass * math.cos(2 * self.arm1.angle - 2 * self.arm2.angle))
        return (p1 - p2 - p3) / d

    def calc_outer_arm_acceleration(self):
        p1 = 2 * math.sin(self.arm1.angle - self.arm2.angle)
        p2 = self.arm1.angle_velocity ** 2 * self.arm1.length * (self.arm1.mass + self.arm2.mass)
        p3 = self.g * (self.arm1.mass + self.arm2.mass) * math.cos(self.arm1.angle)
        p4 = self.arm2.angle_velocity ** 2 * self.arm2.length * self.arm2.mass * math.cos(self.arm1.angle - self.arm2.angle)
        d = self.arm2.length * (2 * self.arm1.mass + self.arm2.mass - self.arm2.mass * math.cos(2 * self.arm1.angle - 2 * self.arm2.angle))
        return (p1 * (p2 + p3 + p4)) / d

    def update(self, dt, elasticity: float = 1):
        self.arm1.angle_acceleration = self.calc_inner_arm_acceleration()
        self.arm2.angle_acceleration = self.calc_outer_arm_acceleration()
        self.arm1.update(dt, elasticity)
        self.arm2.update(dt, elasticity)
        self.arm2.origin_point = self.arm1.end_point(scale=self.draw_scale)

    def draw(self, surface: pygame.Surface):
        self.arm1.draw(surface, color=rainbow(self.arm1.angle), draw_scale=self.draw_scale)
        self.arm2.draw(surface, color=rainbow(self.arm2.angle), draw_scale=self.draw_scale)


def rainbow(angle):
    r = (0.5 * math.sin(angle) + 0.5) * 255
    g = (0.5 * math.sin(angle + 2 * math.pi / 3) + 0.5) * 255
    b = (0.5 * math.sin(angle + 4 * math.pi / 3) + 0.5) * 255
    return r, g, b


pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution)
pygame.display.set_caption(__file__.split("\\")[-1])

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)

# Text
pygame.font.init()
font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

###########################################

a1 = PendulumArm((window_resolution[0] / 2, window_resolution[1] / 4), angle=2*math.pi/3)
a2 = PendulumArm(a1.end_point(), angle=math.pi/2)

dp = DoublePendulum(a1, a2, draw_scale=200)

trail = []

###########################################

time_prev = time.perf_counter()

while True:

    time_now = time.perf_counter()
    dt, time_prev = time_now - time_prev, time_now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    display.fill(BLACK)

    ###########################################

    dp.update(dt, 0.9)
    dp.draw(display)
    trail.append()

    """
    FIXA TRAIL
    """

    ###########################################

    pygame.display.update()
