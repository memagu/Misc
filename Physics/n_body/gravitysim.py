import pygame
import random

pygame.init()

resolution = (1200, 1200)
planet_amount = 50
planet_min_mass = 25
planet_max_mass = 50
player_mass = 10000
player = False
run = True
collide = True
softening = 1000
f_scale = 100000
color_r = (255, 0, 0)
color_g = (0, 255, 0)
color_b = (0, 0, 255)
color_void = (0, 0, 0)
color_white = (255, 255, 255)
draw_triangles = False
draw_forces = False
high_contrast = False
draw_resulting_forces = False
draw_path = False

display = pygame.display.set_mode(resolution)
pygame.display.update()

# G = 6.67 * 10 ** -11
G = 0.0667

def newtonian_gravity(m1, m2, r):
    global softening
    return (m1 * m2 * G) / (r ** 2 + softening)


def color_random():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def add_elements(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        temp.append(arr1[i] + arr2[i])
    return temp


def unit_scale(vector, scale_factor = 1):
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
        self.vectors = []

    def clear_vectors(self):
        self.vectors = []

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
                    and self.in_bounds:
                self.in_bounds = False
                self.bounce(True, False)
            elif (resolution[0] - self.radius < self.position[1] or self.position[1] < self.radius) \
                    and self.in_bounds:
                self.in_bounds = False
                self.bounce(False, True)
            else:
                self.in_bounds = True

        self.vector = unit_scale((self.dx, self.dy), self.fg * f_scale)
        self.vectors.append([self.vector, other.color])


    def draw_triangles(self, other):
        pygame.draw.line(display, color_white, self.position, other.position)
        pygame.draw.line(display, color_white, self.position, [self.position[0] + self.dx, self.position[1]])
        pygame.draw.line(display, color_white, [self.position[0] + self.dx, self.position[1]], other.position)

    def draw_force(self, other):
        if self == other:
            pass
        if high_contrast:
            current_color = color_g
        else:
            current_color = other.color
        pygame.draw.line(display, current_color, self.position, [self.position[0] + self.vector[0],
                                                           self.position[1] + self.vector[1]])

    def draw_resulting_force(self):

        accx = 0
        accy = 0

        for vector in self.vectors:
            accx += vector[0][0]
            accy += vector[0][1]


        pygame.draw.line(
            display,
            color_r,
            self.position,
            [
                self.position[0] + accx,
                self.position[1] + accy
            ]
        )

    def update_position(self):
        self.position = add_elements(self.position, self.velocity)

    def draw(self):
        pygame.draw.circle(display, self.color, self.position, self.radius)


def create_planet(i, min_mass, max_mass, res):
    return Planet(chr(i + 48), (random.randint(max_mass, res[0] - max_mass),
                                random.randint(max_mass, res[1] - max_mass)), [0.0001, 0.0001],
                  random.randint(min_mass, max_mass), color_random())


def create_planets(n, min_mass, max_mass, res):
    planets = []
    for i in range(n):
        planets.append(create_planet(i, min_mass, max_mass, res))

    return planets


planets = create_planets(planet_amount, planet_min_mass, planet_max_mass, resolution)
planets.sort(key=lambda x: x.mass, reverse=True)
a = Planet("mouse", [0, 0], [0, 0], player_mass, color_g)
a.radius = 30

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            continue
        mouse_pos = pygame.mouse.get_pos()
        a.position = mouse_pos
        if event.type == pygame.KEYDOWN:
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
                planets.append(create_planet(planet_amount, planet_min_mass, planet_max_mass, resolution))
                planets.sort(key=lambda x: x.mass, reverse=True)
            if event.key == pygame.K_DOWN and planet_amount > 1:
                planet_amount -= 1
                planets.pop()
            if event.key == pygame.K_p:
                draw_path = not draw_path
            if event.key == pygame.K_LEFT:
                G *= 10
            if event.key == pygame.K_LEFT:
                G /= 10
            if event.key == pygame.K_h:
                high_contrast = not high_contrast

    if not draw_path:
        display.fill(color_void)

    if player:
        a.draw()

    for planet in planets:
        drawn = False
        planet.clear_vectors()
        if planet == a:
            continue
        for other_planet in planets:
            planet.change_velocity(other_planet)
            if not drawn:
                planet.draw()
                drawn = True
            if draw_triangles:
                planet.draw_triangles(other_planet)
            if draw_forces:
                planet.draw_force(other_planet)
        if draw_resulting_forces:
            planet.draw_resulting_force()
        planet.update_position()

    pygame.display.update()
