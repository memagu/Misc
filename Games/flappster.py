import pygame
import time
import random

pygame.init()

resolution = [600, 800]
display = pygame.display.set_mode(resolution)
framerate = 60
run = True
color_green = (0, 255, 0)
color_yellow = (255, 255, 0)
color_red = (255, 0, 0)

pipe_thickness = 50
gravity = 800


class Bird():
    def __init__(self, position, velocity, color):
        self.position = position
        self.velocity = velocity
        self.color = color
        self.corners = []

    def update_position(self):
        self.position[1] += self.velocity / framerate
        self.corners = [tuple(self.position), (self.position[0] + pipe_thickness, self.position[1]),
                        (self.position[0], self.position[1] + pipe_thickness),
                        (self.position[0] + pipe_thickness, self.position[1] + pipe_thickness)]

    def draw(self):
        pygame.draw.rect(display, self.color, [*self.position, pipe_thickness, pipe_thickness])


class Pipe():
    def __init__(self, position, velocity, pipe_thickness, gap_size, gap_height, color, display):
        self.position = position
        self.velocity = velocity
        self.pipe_thickness = pipe_thickness
        self.gap_size = gap_size
        self.gap_height = gap_height
        self.color = color
        self.display = display
        self.cleared = False

    def update_position(self):
        self.position[0] += self.velocity / framerate

    def draw(self):
        pygame.draw.rect(self.display, self.color,
                         [self.position[0], 0, self.pipe_thickness,
                          (resolution[1] - self.gap_size) / 2 - self.gap_height])
        pygame.draw.rect(self.display, self.color,
                         [self.position[0], (resolution[1] + self.gap_size) / 2 - self.gap_height, self.pipe_thickness,
                          (resolution[1] - self.gap_size) / 2 + self.gap_height])


def make_pipe():
    return Pipe([resolution[0], 0], -100, pipe_thickness, 200,
                random.randint(-1 * resolution[1] // 3, resolution[1] // 3),
                color_green, display)


def defeat():
    global run
    run = False
    time.sleep(0.5)


player = Bird([resolution[0] / 2, resolution[1] / 2], 0, color_yellow)
pipes = []
count = 0
points = 0
temp = 0

while run:
    count += 1
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.velocity = -400

    display.fill((0, 0, 0))
    if count % (framerate * 3) == 0:
        pipes.append(make_pipe())

    for corner in player.corners:
        if resolution[1] < corner[1] or corner[1] < 0:
            defeat()
        for pipe in pipes:
            if pipe.position[0] < corner[0] < pipe.position[0] + pipe_thickness and (
                    0 < corner[1] < (resolution[1] - pipe.gap_size) / 2 - pipe.gap_height or (
                    resolution[1] + pipe.gap_size) / 2 - pipe.gap_height < corner[1] < (
                            resolution[1] + pipe.gap_size) / 2 - pipe.gap_height + (
                            resolution[1] - pipe.gap_size) / 2 + pipe.gap_height):
                defeat()

    for pipe in pipes:
        pipe.update_position()
        if pipe.position[0] < player.position[0] and not pipe.cleared:
            pipe.cleared = True
            temp += 1
            if temp != points:
                print(temp)
            points = temp
        if pipe.position[0] < -pipe_thickness:
            pipes.remove(pipe)

    player.velocity += gravity / framerate
    player.update_position()

    for pipe in pipes:
        pipe.draw()
    player.draw()

    pygame.display.update()
    time.sleep(1 / framerate)
