from melvec2 import *
from abc import ABC, abstractmethod

class Coordsys(ABC):
    def __str__(self):
        return str(self.__dict__)

    @abstractmethod
    def local_to_world(self, point: Vector) -> Vector:
        pass

    @abstractmethod
    def world_to_local(self, point: Vector) -> Vector:
        pass


class Coordsys2d(Coordsys):
    def __init__(self, i_hat: Vec2, j_hat: Vec2, offset: Vec2):
        self.i_hat = i_hat.normalize()
        self.j_hat = j_hat.normalize()
        self.offset = offset

    def local_to_world(self, point: Vec2) -> Vec2:
        return self.i_hat * point.x + self.j_hat * point.y + self.offset

    def world_to_local(self, point: Vec2) -> Vec2:
        relative_point = point - self.offset
        x = relative_point.dot(self.i_hat)
        y = relative_point.dot(self.j_hat)
        return Vec2(x, y)


class Coordsys3d(Coordsys):
    def __init__(self, i_hat: Vec3, j_hat: Vec3, k_hat: Vec3, offset: Vec3):
        self.i_hat = i_hat.normalize()
        self.j_hat = j_hat.normalize()
        self.k_hat = k_hat.normalize()
        self.offset = offset

    def local_to_world(self, point: Vec3) -> Vec3:
        return self.i_hat * point.x + self.j_hat * point.y + self.k_hat * point.z + self.offset

    def world_to_local(self, point: Vec3) -> Vec3:
        relative_point = point - self.offset
        x = relative_point.dot(self.i_hat)
        y = relative_point.dot(self.j_hat)
        z = relative_point.dot(self.k_hat)
        return Vec3(x, y, z)
