import pygame
import time
import math
import random
from Math.melutil.melvec import *

# Misc variables

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


# Functions
def show_fps(surface, font, dt, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / dt)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / dt)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


def color_rainbow(angle):
    r = (math.sin(angle) + 1) / 2
    g = (math.sin(angle + math.pi / 1.5) + 1) / 2
    b = (math.sin(angle + 2 * math.pi / 1.5) + 1) / 2
    return [255 * r, 255 * g, 255 * b]


def distance(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))]) ** 0.5


def distance_squared(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))])


# Classes
class Slider:
    def __init__(self, pos: [int, int], tag: str, angle: float = 0, length: float = 200, min_value: float = 0,
                 max_value: float = 1, value: float = 0.5):
        self.pos = pos
        self.tag = tag
        self.angle = angle
        self.length = length
        self.end = [self.pos[0] + math.cos(self.angle) * self.length, self.pos[1] + math.sin(self.angle) * self.length]
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.value_amplitude = (self.value - self.min_value) / (self.max_value - self.min_value) * self.length
        self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                          self.pos[1] + math.sin(self.angle) * self.value_amplitude]
        self.font = pygame.font.SysFont("leelawadeeuisemilight", 16)

    def draw_slider(self, surface, color: [int, int, int] = color_white,):
        pygame.draw.aaline(surface, color, self.pos, self.end)
        pygame.draw.circle(surface, color, self.value_pos, 8)

        value_text = self.font.render(str(round(self.value, 3)), True, color)
        value_text_rect = value_text.get_rect(center=[self.value_pos[0], self.value_pos[1] - 24])
        surface.blit(value_text, value_text_rect)

        tag_text = self.font.render(self.tag, True, color)
        tag_text_rect = tag_text.get_rect(center=[(self.pos[0] + self.end[0]) / 2,
                                                  (self.pos[1] + self.end[1]) / 2 + 24])
        surface.blit(tag_text, tag_text_rect)

    def pos_to_value(self, pos):
        d1 = distance_squared(self.pos, pos) if distance_squared(pos, self.end) <= self.length ** 2 else 0
        d2 = distance(self.pos, self.end)
        return d1 ** 0.5 / d2 * (self.max_value - self.min_value) - abs(self.min_value)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and distance_squared(mouse_pos, self.value_pos) <= 32 ** 2:
            self.value = max(min(self.pos_to_value(mouse_pos), self.max_value), self.min_value)
            self.value_amplitude = (self.value - self.min_value) / (self.max_value - self.min_value) * self.length
            self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                              self.pos[1] + math.sin(self.angle) * self.value_amplitude]

    def update_angle(self):
        self.end = [self.pos[0] + math.cos(self.angle) * self.length, self.pos[1] + math.sin(self.angle) * self.length]
        self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                          self.pos[1] + math.sin(self.angle) * self.value_amplitude]


# Your code here


class Planet:
    def __init__(self, pos: Vec2, vel: Vec2, mass, color: Vec3):
        self.pos = pos
        self.vel = vel
        self.acc = Vec2()
        self.mass = mass
        self.radius = math.sqrt(mass/math.pi)
        self.color = color

    def calc_force(self, other, G=6.67*10**-11, padding=10):
        return G * self.mass * other.mass / (self.pos.distance_to_squared(other.pos) + padding)

    def calculate_acceleration(self, others, G=6.67*10**-11, padding=10):
        self.acc *= 0
        for other in others:
            if other != self:
                self.acc += (other.pos - self.pos).normalize() * (self.calc_force(other, G, padding) / self.mass)

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt

    def draw(self, surface):
        pygame.draw.circle(surface, self.color.as_list(), self.pos.as_list(), self.radius)



if __name__ == "__main__":
    print(__file__.split("\\")[-1])
