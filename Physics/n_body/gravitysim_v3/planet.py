import random
import math


class Planet:
    def __init__(self, mass, position, velocity, min_color=0, max_color=255):
        self.mass = mass
        self.posx = position[0]
        self.posy = position[1]
        self.velx = velocity[0]
        self.vely = velocity[1]
        self.accx = 0
        self.accy = 0
        self.radius = math.log(mass, 2)
        self.color = (random.randint(min_color, max_color), random.randint(min_color, max_color), random.randint(min_color, max_color))

    def update_position(self, dt):
        self.velx, self.vely = self.velx + self.accx * dt, self.vely + self.accy * dt
        self.posx, self.posy = self.posx + self.velx * dt, self.posy + self.vely * dt

    def collide(self, other, elasticity):
        sum_m = self.mass + other.mass
        p1_1_x = ((self.mass - other.mass) / sum_m) * self.velx
        p1_2_x = (other.mass * 2 / sum_m) * other.x_vel

        p1_1_y = ((self.mass - other.mass) / sum_m) * self.vely
        p1_2_y = (other.mass * 2 / sum_m) * other.y_vel

        self.velx = (p1_1_x + p1_2_x) * elasticity
        self.vely = (p1_1_y + p1_2_y) * elasticity