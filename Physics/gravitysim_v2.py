 import math
import pygame
import random

pygame.init()

resolution = (1200, 1200)
planet_amount = 20
planet_max_mass = 50
player_mass = 200
player = False
run = True
collide = True
softening = 200
f_scale = 100000
color_r = (255, 0, 0)
color_g = (0, 255, 0)
color_b = (0, 0, 255)
color_void = (0, 0, 0)
color_white = (255, 255, 255)
draw_triangles = False
draw_forces = False
draw_resulting_forces = False

display = pygame.display.set_mode(resolution)
pygame.display.update()

# G = 6.67 * 10 ** -11
G = 0.001


def newtonian_gravity(m1, m2, r):
    return (m1 * m2 * G) / (r ** 2 + softening)


def color_random():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def add_elements(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        temp.append(arr1[i] + arr2[i])
    return temp


def unit_scale(vector, scale_factor=1):
    length = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    if length == 0:
        return vector
    nvx, nvy = vector[0] / length, vector[1] / length
    return nvx * scale_factor, nvy * scale_factor


class Planet:
    def __init__(self, tag, position, velocity, mass, color):
        self.tag = tag
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = mass
        self.color = color
        self.in_bounds = True
        self.colliding = False
        self.dx = 0
        self.dy = 0
        self.distance = 0
        self.fg = 0
        self.a = 0
        self.vector = [0, 0]
        self.saved = []

    def clear_saved(self):
        self.saved = []

    def bounce(self, x, y):
        if x:
            self.velocity[0] *= -1
        if y:
            self.velocity[1] *= -1

    def change_velocity(self, other):
        if self == other:
            pass
        else:
            self.dx = other.position[0] - self.position[0]
            self.dy = other.position[1] - self.position[1]
            self.distance = (self.dx ** 2 + self.dy ** 2) ** 0.5

            if self.distance == 0:
                pass
            else:
                self.fg = newtonian_gravity(self.mass, other.mass, self.distance)
                self.a = self.fg / self.mass
                self.velocity = add_elements(self.velocity,
                                             [self.a * self.dx / self.distance, self.a * self.dy / self.distance])

                if collide and self.distance <= self.radius + other.radius and not self.colliding:
                    self.bounce(True, True)
                    self.colliding = True
                elif self.distance >= self.radius + other.radius:
                    self.colliding = False

            if (resolution[0] - self.radius < self.position[0] or self.position[0] < self.radius) \
                    and self.in_bounds == True:
                self.in_bounds = False
                self.bounce(True, False)
            elif (resolution[0] - self.radius < self.position[1] or self.position[1] < self.radius) \
                    and self.in_bounds == True:
                self.in_bounds = False
                self.bounce(False, True)
            else:
                self.in_bounds = True

        self.vector = unit_scale((self.dx, self.dy), self.fg * f_scale)
        self.saved.append([self.vector, [self.dx, self.dy], [self.position, other.position], other.color, other])

    def draw_triangles(self):
        for save in self.saved:
            pygame.draw.line(display, color_white, self.position, save[2][1])
            pygame.draw.line(display, color_white, self.position, [self.position[0] + save[1][0], self.position[1]])
            pygame.draw.line(display, color_white, [self.position[0] + save[1][0], self.position[1]], save[2][1])

    def draw_force(self):
        for save in self.saved:
            pygame.draw.line(display, save[3], self.position, [self.position[0] + save[0][0],
                                                               self.position[1] + save[0][1]])

    def draw_resulting_force(self):
        for save in self.saved:
            accx = 0
            accy = 0

            accx += save[0][0]
            accy += save[0][1]
        pygame.draw.line(display, color_r, self.position, [self.position[0] + accx, self.position[1] + accy])

    def update_position(self):
        self.position = add_elements(self.position, self.velocity)

    def draw(self):
        pygame.draw.circle(display, self.color, self.position, self.radius)


def create_planet(i, max_mass, res):
    return Planet(chr(i + 48), (random.randint(max_mass, res[0] - max_mass),
                                random.randint(max_mass, res[1] - max_mass)), [0.0001, 0.0001],
                  random.randint(1, max_mass), color_random())


def create_planets(n, max_mass, res):
    planets = []
    for i in range(n):
        planets.append(create_planet(i, max_mass, res))

    return planets




planets = create_planets(planet_amount, planet_max_mass, resolution)
a = Planet("player", [0, 0], [0, 0], player_mass, color_g)
a.radius = 30

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            continue
        mouse_pos = pygame.mouse.get_pos()
        a.position = mouse_pos
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_SPACE:
                player = not player
                if player:
                    planets.insert(0, a)
                else:
                    planets.pop(0)
            if event.key == pygame.K_t:
                draw_triangles = not draw_triangles
            if event.key == pygame.K_f:
                draw_forces = not draw_forces
            if event.key == pygame.K_r:
                draw_resulting_forces = not draw_resulting_forces
            if event.key == pygame.K_c:
                collide = not collide
            if event.key == pygame.K_UP:
                planet_amount += 1
                planets.append(create_planet(planet_amount, planet_max_mass, resolution))
            if event.key == pygame.K_DOWN and planet_amount > 1:
                planet_amount -= 1
                planets.pop()

    for planet in planets:
        planet.clear_saved()
        if planet == a:
            continue
        for other_planet in planets:
            planet.change_velocity(other_planet)
            planet.update_position()

    display.fill(color_void)

    if player:
        a.draw()

    for planet in planets:
        planet.draw()
        if draw_triangles:
            planet.draw_triangles()
        if draw_forces:
            planet.draw_force()
        if draw_resulting_forces:
            planet.draw_resulting_force()

    pygame.display.update()
