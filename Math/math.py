import math

class Circle():
    def __init__(self, x, y ,r):
        self.x = x
        self.y = y
        self.r = r

    def point_comp_circle(self, ax, ay):
        ad = (ax-self.x)**2 + (ay-self.y)**2
        r_squared = self.r**2
        state = ""
        if ad < r_squared:
            state = "in"
        elif ad == r_squared:
            state = "on"
        else:
            state = "out"
        return state


def cosine_abc(a, b, c):
    return math.acos((a**2 + b**2 - c**2) / (2 * a * b))


def cosine_abC(a, b, C):
    return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))


print(cosine_abC(3.9,4.4,math.radians(41)))