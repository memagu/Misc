
import time
from typing import List
import os
from dataclasses import dataclass


class Frame:
    def __init__(self, width: int, height: int, *, horizontal_spacing: bool = False):
        self.width = width
        self.height = height
        self.horizontal_spacing = horizontal_spacing
        self.pixels = [0 for _ in range(self.width * self.height)]
        self.brightness_map = {0: " ",
                               1: "@"}

    def __str__(self):
        s = ""

        for i, pixel in enumerate(self.pixels):
            if not i % self.width:
                s += "\n"

            s += " " + self.brightness_map[pixel] if self.horizontal_spacing else self.brightness_map[pixel]

        return s

    def flatten_coordinate(self, x: int, y: int):
        return x + self.width * y

    def set_pixel(self, x: int, y: int, value: int):
        if value < 0:
            raise ValueError
        self.pixels[self.flatten_coordinate(x, y)] = value

    def get_pixel(self, x, y):
        return self.pixels[self.flatten_coordinate(x, y)]

    def draw_rect(self, x: int, y: int, width: int, height: int, brightness: int):
        for dy in range(height):
            for dx in range(width):
                self.set_pixel(x + dx, y + dy, brightness)

    def draw_circle(self, x: int, y: int, radius: int, brightness: int):
        for px in range(self.width):
            for py in range(self.height):
                if (x - px) ** 2 + (y - py) ** 2 < radius ** 2:
                    self.set_pixel(px, py, brightness)

    def clear(self):
        self.pixels = [0 for _ in range(self.width * self.height)]


class Ball:
    def __init__(self, x, y, radius, *, x_vel = 0, y_vel = 0):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update(self):
        self.x, self.y = self.x + self.x_vel, self.y + self.y_vel


if __name__ == "__main__":
    WIDTH = 64
    HEIGHT = 32

    frame = Frame(WIDTH, HEIGHT, horizontal_spacing=True)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 5, x_vel=1, y_vel=2)

    while True:
        if ball.x + ball.radius > WIDTH:
            ball.x_vel *= -1

        if ball.x - ball.radius < 0:
            ball.x_vel *= -1

        if ball.y + ball.radius > HEIGHT:
            ball.y_vel *= -1

        if ball.y - ball.radius < 0:
            ball.y_vel *= -1

        ball.update()

        os.system("cls")
        frame.clear()
        frame.draw_circle(ball.x, ball.y, ball.radius, 1)
        print(frame)

        time.sleep(0.033)





