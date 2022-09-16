import functools

import pygame
import time
import math
import random

pygame.init()

WINDOW_RESOLUTION = (900, 900)
image_resolution = [1200, 900]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption("shadowsim_v2_3d")

run = True
time_prev = time.time()
clock = pygame.time.Clock()
framerate = 60

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

# constats

player_move_velocity = 20
player_rotation_velocity = 5

number_of_rays = 50
field_of_view = math.pi / 3

bounces = 8

minimap_ratio = 0.4


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


class LineSegment:
    def __init__(self, p1, p2):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]

    def draw(self):
        pygame.draw.aaline(display, color_white, (self.x1 * minimap_ratio, self.y1 * minimap_ratio),
                           (self.x2 * minimap_ratio, self.y2 * minimap_ratio))


class Ray:
    def __init__(self, point, angle):
        self.x1 = point[0]
        self.y1 = point[1]
        self.x2 = self.x1 + math.cos(angle)
        self.y2 = self.y1 + math.sin(angle)
        self.angle = angle
        # self.k = math.tan(self.angle) if math.tan(self.angle) != 0 else 0.000001
        # self.m = self.y1 / (self.k * self.x1)

    def intersect(self, ls: LineSegment):
        denominator = (self.x1 - self.x2) * (ls.y1 - ls.y2) - (self.y1 - self.y2) * (ls.x1 - ls.x2)
        if denominator == 0:
            return None

        t = ((self.x1 - ls.x1) * (ls.y1 - ls.y2) - (self.y1 - ls.y1) * (ls.x1 - ls.x2)) / denominator
        u = ((self.x1 - ls.x1) * (self.y1 - self.y2) - (self.y1 - ls.y1) * (self.x1 - self.x2)) / denominator
        if 0 <= t and 0 <= u <= 1:
            return self.x1 + t * (self.x2 - self.x1), self.y1 + t * (self.y2 - self.y1)

        return None

    def closest_intersect_old(self, lss: [LineSegment]):
        closest_hit = None
        for ls in lss:
            intersection = self.intersect(ls)
            if not closest_hit and not intersection:
                closest_hit = intersection
            else:
                distance_intersect = ((self.x1 - intersection[0]) ** 2 + (self.y1 - intersection[1]) ** 2) ** 0.5
                distance_closest = ((self.x1 - closest_hit[0]) ** 2 + (self.y1 - closest_hit[1]) ** 2) ** 0.5
                if distance_intersect < distance_closest:
                    closest_hit = intersection

        return closest_hit

    def closest_intersect(self, lss: [LineSegment]):
        closest = (10000, 10000)
        l = list(filter(lambda x: x is not None, map(self.intersect, lss)))

        for hit in l:
            if dist((self.x1, self.y1), hit) < dist((self.x1, self.y1), closest):
                closest = hit

        return closest if closest != (10000, 10000) else None

    def draw(self, target):
        if target:
            pygame.draw.aaline(display, color_white, (self.x1 * minimap_ratio, self.y1 * minimap_ratio),
                               list(map(lambda x: x * minimap_ratio, target)))


class RaySource:
    def __init__(self, pos, heading, fov):
        self.x = pos[0]
        self.y = pos[1]
        self.heading = heading
        self.fov = fov

    def cast_rays(self, n):
        start_angle = self.heading - self.fov / 2
        # stop_angle = self.heading + self.fov / 2
        ray_separation = self.fov / n
        rays = []
        for i in range(n):
            angle = start_angle + ray_separation * (i + 0.5)
            rays.append(Ray((self.x, self.y), angle))

        return rays

    def draw(self):
        pygame.draw.circle(display, color_red, (self.x * minimap_ratio, self.y * minimap_ratio), 10 * minimap_ratio)
        pygame.draw.aaline(display, color_red, (self.x * minimap_ratio, self.y * minimap_ratio),
                           ((math.cos(self.heading) * 20 + self.x) * minimap_ratio,
                            (math.sin(self.heading) * 20 + self.y) * minimap_ratio))

    def move_forward(self, amount):
        self.x += math.cos(self.heading) * amount
        self.y += math.sin(self.heading) * amount

    def move_backward(self, amount):
        self.x -= math.cos(self.heading) * amount
        self.y -= math.sin(self.heading) * amount

    def move_right(self, amount):
        self.x += math.cos(self.heading + math.pi / 2) * amount
        self.y += math.sin(self.heading + math.pi / 2) * amount

    def move_left(self, amount):
        self.x += math.cos(self.heading - math.pi / 2) * amount
        self.y += math.sin(self.heading - math.pi / 2) * amount


def make_line_segments(amt, seed=0):
    random.seed(seed)
    line_segments = []
    for i in range(amt):
        line_segments.append(
            LineSegment((random.randint(0, WINDOW_RESOLUTION[0]), random.randint(0, WINDOW_RESOLUTION[1])),
                        (random.randint(0, WINDOW_RESOLUTION[0]), random.randint(0, WINDOW_RESOLUTION[1]))))

    return line_segments


def polygon(points: [(float, float)]):
    shape = []
    for i in range(1, len(points)):
        shape.append(LineSegment(points[i - 1], points[i]))

    shape.append(LineSegment(points[-1], points[0]))
    return shape


def distance_color(distance, color):
    return list(map(lambda c: int(c / ((distance + 200) / 200) ** 2), color))


def distance_height(distance, screen_h):
    return screen_h / ((distance + 200) / 200)


# Define screen walls

screen_walls = [
    LineSegment((0, 0), (WINDOW_RESOLUTION[0], 0)),
    LineSegment((0, WINDOW_RESOLUTION[1]), (WINDOW_RESOLUTION[0], WINDOW_RESOLUTION[1])),
    LineSegment((0, 0), (0, WINDOW_RESOLUTION[1])),
    LineSegment((WINDOW_RESOLUTION[0], 0), (WINDOW_RESOLUTION[0], WINDOW_RESOLUTION[1])),
]

# List of all "interactable" line segments

shape_coords = [(433.20097, 749.13513), (194.34557, 579.51318), (312.04243, 221.23008), (639.17048, 269.69349),
                (400, 500),
                (647.82466, 636.63078)]

obstacles = [*make_line_segments(5, 1), *screen_walls]

ray_source = RaySource((450, 450), 0, field_of_view)

# Game loop

while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        mouse_pos = pygame.mouse.get_pos()

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Keyboard input

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        player_move_velocity_t = player_move_velocity * 5
    else:
        player_move_velocity_t = player_move_velocity

    if keys[pygame.K_w]:
        ray_source.move_forward(player_move_velocity_t * dt)

    if keys[pygame.K_a]:
        ray_source.move_left(player_move_velocity_t * dt)

    if keys[pygame.K_s]:
        ray_source.move_backward(player_move_velocity_t * dt)

    if keys[pygame.K_d]:
        ray_source.move_right(player_move_velocity_t * dt)

    if keys[pygame.K_LEFT]:
        ray_source.heading -= player_rotation_velocity * dt

    if keys[pygame.K_RIGHT]:
        ray_source.heading += player_rotation_velocity * dt

    if keys[pygame.K_UP] and ray_source.fov < math.pi * 2:
        ray_source.fov += player_rotation_velocity / 2 * dt

    if keys[pygame.K_DOWN] and ray_source.fov > 0:
        ray_source.fov -= player_rotation_velocity / 2 * dt

    # Calculate

    rays = ray_source.cast_rays(number_of_rays)

    # Draw

    display.fill(color_black)

    for i, ray in enumerate(rays):
        hit_point = ray.closest_intersect(obstacles)
        if hit_point:
            distance = dist((ray.x1, ray.y1), hit_point) * abs(math.cos(ray.angle - ray_source.heading))
            height = distance_height(distance, WINDOW_RESOLUTION[1])
            pygame.draw.rect(
                display,
                distance_color(distance, color_white),
                [i * WINDOW_RESOLUTION[0] / number_of_rays, (WINDOW_RESOLUTION[1] - height) * 0.5,
                 WINDOW_RESOLUTION[0] / number_of_rays,
                 height]
            )

        # pygame.draw.rect(display, color_black,
        # [0, 0, window_resolution[0] * minimap_ratio, window_resolution[1] * minimap_ratio])

        ray.draw(hit_point)

    for obstacle in obstacles:
        obstacle.draw()

    ray_source.draw()

    # Update frame and wait
    pygame.display.update()
    clock.tick(framerate)
