from abc import ABC, abstractmethod
import math



class Vector(ABC):
    def __str__(self):
        return str(self.__dict__)

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, scalar):
        pass

    @abstractmethod
    def __pow__(self, scalar, modulo=None):
        pass

    @abstractmethod
    def __truediv__(self, scalar):
        pass

    @abstractmethod
    def __floordiv__(self, scalar):
        pass

    @abstractmethod
    def __mod__(self, scalar):
        pass

    @abstractmethod
    def __bool__(self):
        pass

    @abstractmethod
    def __abs__(self):
        pass

    @abstractmethod
    def magnitude(self):
        pass

    @abstractmethod
    def magnitude_squared(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def dot(self, other):
        pass

    @abstractmethod
    def cross(self, other):
        pass

    @abstractmethod
    def scale_to_magnitude(self, magnitude):
        pass

    @abstractmethod
    def reflect(self, normal_vector):
        pass

    @abstractmethod
    def distance_to(self, other):
        pass

    @abstractmethod
    def distance_to_squared(self, other):
        pass

    @abstractmethod
    def lerp(self, other, alpha):
        pass

    @abstractmethod
    def apply(self, func):
        pass

    @abstractmethod
    def angle_to(self, other):
        pass

    @abstractmethod
    def as_list(self):
        pass

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
        return self.conv_vec3()\
            .cross(other.conv_vec3)\
            .magnitude()

    def scale_to_magnitude(self, magnitude) -> Vector:
        return self.normalize() * magnitude

    def reflect(self, normal_vector) -> Vector:
        return self - 2 * self.dot(normal_vector) * normal_vector

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

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def magnitude_squared(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self) -> Vector:
        return self / self.magnitude()

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other) -> Vector:
        return Vec3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.z)

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

    def conv_vec2(self) -> Vector:
        return Vec2(self.x, self.y)

    def as_list(self):
        return [self.x, self.y, self.z]


if __name__ == '__main__':
    pass

