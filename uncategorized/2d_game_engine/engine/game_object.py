from abc import ABC
from typing import List

class Transform:
    def __init__(self, x=0, y=0, width=0, height=0, scale_x=1, scale_y=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y

    @property
    def center(self):
        x = self.x + self.width / 2
        y = self.y + self.height / 2
        return x, y

    def set_position(self, x, y):
        self.x = x or self.x
        self.y = y or self.y

    def change_position(self, dx, dy, scale=1):
        self.x += dx * scale
        self.y += dy * scale

    def set_dimensions(self, width, height):
        self.width = width or self.width
        self.height = height or self.height

    def change_dimensions(self, dwidth, dheight, scale=1):
        self.width += dwidth * scale
        self.height += dheight * scale

    def set_scale(self, scale_x, scale_y):
        self.scale_x = scale_x or self.scale_x
        self.scale_y = scale_y or self.scale_y

    def change_scale(self, dwidth, dheight, scale=1):
        self.width += dwidth * scale
        self.height += dheight * scale


class AbstractGameObject(ABC):
    def __init__(self, transform: Transform, tags: List[str] = None, name: str = None):
        self._transform: Transform = transform or Transform()
        self._tags = tags if tags is not None else []
        self._name = name

    @property
    def transform(self):
        return self._transform

    @property
    def tag(self):
        return self._tags

    @property
    def name(self):
        return self._name

    def input(self):
        pass

    def update(self):
        pass

    def fixed_update(self):
        pass

    def render(self):
        pass


class GameObject(AbstractGameObject):
    def __init__(self, transform: Transform, tags: List[str] = None, name: str = None):
        super().__init__(transform=transform, tags=tags, name=name)

        self.started = False
        self.destroyed = False

    def start(self):
        self.started = True

    def destroy(self):
        self.destroyed = True


if __name__ == "__main__":
    print(__file__)



