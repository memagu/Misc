import math

from melvec import Vector



class Vec3(Vector):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def from_angle(direction_vector=Vec2(), magnitude=0):
        pass

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __pow__(self, scalar, modulo=None):
        return Vec3(self.x ** scalar, self.y ** scalar, self.z ** scalar)

    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __floordiv__(self, scalar):
        return Vec3(self.x // scalar, self.y // scalar, self.z // scalar)

    def __mod__(self, scalar):
        return Vec3(self.x % scalar, self.y % scalar, self.z % scalar)

    def __bool__(self):
        return (self.x or self.y or self.z) != 0

    def __abs__(self):
        return self.magnitude()

    def __iter__(self):
        for component in (self.x, self.y, self.z):
            yield component

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def magnitude_squared(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self) -> Vector:
        return self / (self.magnitude() if self.magnitude() else 1)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other) -> Vector:
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.z)

    def scale_to_magnitude(self, magnitude) -> Vector:
        return self.normalize() * magnitude

    def reflect(self, normal_vector) -> Vector:
        return self - 2 * self.dot(normal_vector) * normal_vector

    def distance_to(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5

    def distance_to_squared(self, other) -> float:
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2

    def lerp(self, other, alpha) -> Vector:
        return self + (other - self) * alpha

    def apply(self, func) -> Vector:
        return Vec3(func(self.x), func(self.y), func(self.z))

    def rotate(self, angle, vector) -> Vector:
        pass

    def rotate_x(self, angle) -> Vector:
        return self.rotate(angle, Vec3(1, 0, 0))

    def rotate_y(self, angle) -> Vector:
        return self.rotate(angle, Vec3(0, 1, 0))

    def rotate_z(self, angle) -> Vector:
        return self.rotate(angle, Vec3(0, 0, 1))

    def angle_to(self, other) -> float:
        return math.acos(self.dot(other) / (abs(self) * abs(other)))


if __name__ == '__main__':
    pass
