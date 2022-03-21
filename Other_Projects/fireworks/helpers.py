import pygame
import random
import math

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


def rainbow(angle):
    r = ((math.sin(angle) + 1) / 2) * 255
    g = ((math.sin(angle + math.pi / 3) + 1) / 2) * 255
    b = ((math.sin(angle + 2 * math.pi / 3) + 1) / 2) * 255
    return r, g, b


class Particle:
    def __init__(self, pos, velocity, acceleration, fuse_time, radius, color, color_decay_rate):
        self.pos = pos
        self.velocity = velocity
        self.acceleration = acceleration
        self.fuse_time = fuse_time
        self.radius = radius
        self.color = color
        self.color_decay_rate = color_decay_rate

    def update_position(self, dt):
        self.pos = [self.pos[0] + self.velocity[0] * dt, self.pos[1] + self.velocity[1] * dt]
        self.velocity = [self.velocity[0] + self.acceleration[0] * dt, self.velocity[1] + self.acceleration[1] * dt]
        self.fuse_time -= dt

    def update_color(self, dt):
        r = self.color[0] - self.color[0] * self.color_decay_rate * dt
        g = self.color[1] - self.color[1] * self.color_decay_rate * dt
        b = self.color[2] - self.color[2] * self.color_decay_rate * dt
        self.color = r, g, b

    def explode(self, amount, velocity):
        pi_halves = math.pi / 2
        separation = 2 * math.pi / amount
        color_angle = random.randint(-158, 158) / 100
        new_particles = []
        for i in range(amount):
            new_particles.append(Particle(self.pos,
                                          [self.velocity[0] + math.cos(pi_halves + separation * i) * velocity, self.velocity[1] - math.sin(pi_halves + separation * i) * velocity],
                                          [0, 491],
                                          5,
                                          self.radius / 1.5,
                                          rainbow(color_angle + separation * i),
                                          0.5))

        return new_particles

    def is_visible(self, min_x, max_x, min_y, max_y):
        if self.pos[0] + self.radius < min_x \
                or self.pos[0] - self.radius > max_x \
                or self.pos[1] + self.radius < min_y \
                or self.pos[1] - self.radius > max_y:
            return False
        return True

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
