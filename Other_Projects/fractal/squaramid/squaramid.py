from dataclasses import dataclass
import time
from typing import Sequence

import pygame
from pygame.math import Vector2, Vector3

pygame.init()

window_resolution = Vector2(1200, 900)
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

framerate = 480
time_prev = time.time()
clock = pygame.time.Clock()
run = True


@dataclass
class Segment:
    origin: Vector2
    length: float
    direction: Vector2

    @property
    def end(self) -> Vector2:
        return self.direction * self.length + self.origin

    @property
    def normal(self) -> Vector2:
        return self.direction.rotate(90)


class Squaramid:
    def __init__(self, segments: Sequence[Segment], color: Vector3 = Vector3(255)):
        self.segments = segments
        self.color = color

    def subdivide(self):
        new_segments = []
        for segment in self.segments:
            new_segment_length = segment.length / 3
            new_segments.append(Segment(segment.origin, new_segment_length, segment.direction))
            new_segments.append(Segment(new_segments[-1].end, new_segment_length, -segment.normal))
            new_segments.append(Segment(new_segments[-1].end, new_segment_length, segment.direction))
            new_segments.append(Segment(new_segments[-1].end, new_segment_length, segment.normal))
            new_segments.append(Segment(new_segments[-1].end, new_segment_length, segment.direction))

        self.segments = new_segments

    def draw(self, surface: pygame.Surface):
        for segment in self.segments:
            pygame.draw.line(surface, self.color, segment.origin, segment.end)


s = Squaramid([Segment(Vector2(10, 600), 1180, Vector2(1, 0))])

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
            if event.key == pygame.K_SPACE:
                s.subdivide()
                print(len(s.segments))

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_1]:
        #     pass

    display.fill(Vector3(0, 0, 0))

    s.draw(display)

    pygame.display.update()
    if abs(framerate):
        clock.tick(framerate)
