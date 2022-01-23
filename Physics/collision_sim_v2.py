import pygame
import time
import random

pygame.init()

WINDOW_RESOLUTION = (1200, 900)
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()
framerate = 120

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

scale = 40
speed_multiplier = 30

pygame.font.init()
font = pygame.font.SysFont(None, WINDOW_RESOLUTION[0] // 32)


class Object:
    def __init__(self, mass, velocity, x, color):
        self.mass = mass
        self.velocity = velocity
        self.x = x
        self.color = color
        self.radius = (mass * scale) ** 0.5
        self.diameter = self.radius * 2
        self.x_c = self.x + self.radius

    def update_position(self):
        self.x += self.velocity * dt
        self.x_c = self.x + self.radius

        if self.x < 0 or WINDOW_RESOLUTION[0] - self.diameter < self.x:
            self.velocity *= -1
            self.x += self.velocity * dt

    def check_collision(self, other):
        if abs(self.x_c - other.x_c) < self.radius + other.radius:
            self.x += self.velocity * -dt * 4
            other.x += other.velocity * -dt * 4
            self.update_position()
            other.update_position()
            return True
        return False

    def collide(self, other):
        sum_m = self.mass + other.mass
        p1_1 = ((self.mass - other.mass) / sum_m) * self.velocity
        p1_2 = (other.mass * 2 / sum_m) * other.velocity
        return p1_1 + p1_2

    def draw(self):
        pygame.draw.rect(display, self.color,
                         [self.x, WINDOW_RESOLUTION[1] / 2 - self.radius, self.diameter, self.diameter])

    def draw_telemetry(self):
        msg_m = font.render(f"mass: {self.mass}", True, self.color)
        msg_v = font.render(f"velocity: {round(self.velocity, 3)}", True, self.color)
        msg_v_rect = msg_v.get_rect(center=(self.x_c, WINDOW_RESOLUTION[1] / 2 - self.radius - 30))
        msg_m_rect = msg_m.get_rect(center=(self.x_c, WINDOW_RESOLUTION[1] / 2 - self.radius - 30 - msg_v_rect.height))

        if msg_m_rect.x <= 0:
            msg_m_rect.x = 0

        if msg_m_rect.x + msg_m_rect.width >= WINDOW_RESOLUTION[0]:
            msg_m_rect.x = WINDOW_RESOLUTION[0] - msg_m_rect.width

        if msg_v_rect.x <= 0:
            msg_v_rect.x = 0

        if msg_v_rect.x + msg_v_rect.width >= WINDOW_RESOLUTION[0]:
            msg_v_rect.x = WINDOW_RESOLUTION[0] - msg_v_rect.width

        display.blit(msg_m, msg_m_rect)
        display.blit(msg_v, msg_v_rect)

def make_objects(n, seed, min_mass, max_mass, min_vel, max_vel):
    n += 2
    random.seed(seed)
    objects = []
    for i in range(1, n - 1):
        objects.append(
            Object(random.randint(min_mass, max_mass), random.randint(min_vel, max_vel), i * WINDOW_RESOLUTION[0] / n,
                   (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
    return objects


# objects = [*make_objects(20, 1, 5, 100, -20, 20)]
objects = [Object(3, 4, 300, color_green), Object(2, -3, 900, color_blue)]

collisions = 0

while run:

    # Calculate dt
    time_now = time.time()
    dt = (time_now - time_prev) * speed_multiplier
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WINDOW_RESOLUTION = [event.w, event.h]

    display.fill(color_black)

    for i, o1 in enumerate(objects):
        for o2 in objects[:i] + objects[i + 1:]:
            if o1 == o2:
                continue
            if o1.check_collision(o2):
                collisions += 1
                print(collisions)
                o1.x -= o1.velocity * dt * 2
                o2.x -= o2.velocity * dt * 2
                v1 = o1.collide(o2)
                v2 = o2.collide(o1)
                o1.velocity = v1
                o2.velocity = v2

        o1.update_position()
        o1.draw()

    for o in objects:
        o.draw_telemetry()

    pygame.display.update()
    clock.tick(framerate)
