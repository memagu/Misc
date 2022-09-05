import math

from melvec import Vector


class Vec2(Vector):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @staticmethod
    def from_angle(angle=0, magnitude=0):
        return Vec2(math.cos(angle) * magnitude, math.sin(angle) * magnitude)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __pow__(self, scalar, modulo=None):
        return Vec2(self.x ** scalar, self.y ** scalar)

    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vec2(self.x // scalar, self.y // scalar)

    def __mod__(self, scalar):
        return Vec2(self.x % scalar, self.y % scalar)

    def __bool__(self):
        return (self.x or self.y) != 0

    def __abs__(self):
        return self.magnitude()

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def magnitude_squared(self) -> float:
        return self.x ** 2 + self.y ** 2

    def normalize(self) -> Vector:
        return self / self.magnitude()

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> float:
        return self.conv_vec3() \
            .cross(other.conv_vec3) \
            .magnitude()

    def scale_to_magnitude(self, magnitude) -> Vector:
        return self.normalize() * magnitude

    def reflect(self, normal_vector) -> Vector:
        return self - normal_vector * (2 * self.dot(normal_vector))

    def distance_to(self, other) -> float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def distance_to_squared(self, other) -> float:
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2

    def lerp(self, other, alpha) -> Vector:
        return self + (other - self) * alpha

    def apply(self, func) -> Vector:
        return Vec2(func(self.x), func(self.y))

    def rotate(self, angle) -> Vector:
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        return Vec2(self.x * cos_angle - self.y * sin_angle, self.x * sin_angle + self.y * cos_angle)

    def angle_to(self, other) -> float:
        return math.acos(self.dot(other) / (abs(self) * abs(other)))

    def conv_vec3(self, z: float = 0) -> Vector:
        return Vec3(self.x, self.y)

    def as_list(self) -> [float]:
        return [self.x, self.y]


if __name__ == '__main__':
    d = Vec2(1, -1)
    n = Vec2(0, 1)
    print(d.reflect(n))
    print(d.dot(n))