from dataclasses import dataclass, field
from typing import Any


@dataclass
class DataPoint:
    x: float
    y: float
    data: Any


@dataclass
class Rect:
    x: float
    y: float
    w: float
    h: float

    def intersects(self, other_rect) -> bool:
        return not (self.x > other_rect.x + other_rect.w or
                    self.x + self.w < other_rect.x or
                    self.y > other_rect.y + other_rect.h or
                    self.y + self.h < other_rect.y)

    def contains(self, data_point: DataPoint) -> bool:
        return self.x <= data_point.x <= self.x + self.w and self.y <= data_point.y <= self.y + self.h


@dataclass
class Quadtree:
    bbox: Rect
    region_point_limit: int = 16
    data_points: list[DataPoint] = field(default_factory=list)
    nw = None
    ne = None
    sw = None
    se = None

    def insert(self, data_point: DataPoint) -> None:
        if self.nw is None:
            if any(check_data_point.x == data_point.x and check_data_point.y == data_point.y
                   for check_data_point in self.data_points):
                self.data_points.append(data_point)
                return

            if len(self.data_points) < self.region_point_limit:
                self.data_points.append(data_point)
                return

            self.nw = Quadtree(Rect(self.bbox.x, self.bbox.y, self.bbox.w / 2, self.bbox.h / 2))
            self.ne = Quadtree(Rect(self.bbox.x + self.bbox.w / 2, self.bbox.y, self.bbox.w / 2, self.bbox.h / 2))
            self.sw = Quadtree(Rect(self.bbox.x, self.bbox.y + self.bbox.h / 2, self.bbox.w / 2, self.bbox.h / 2))
            self.se = Quadtree(
                Rect(self.bbox.x + self.bbox.w / 2, self.bbox.y + self.bbox.h / 2, self.bbox.w / 2, self.bbox.h / 2))

            for own_point in self.data_points:
                if own_point.x < self.bbox.x + self.bbox.w / 2:
                    if own_point.y < self.bbox.y + self.bbox.h / 2:
                        self.nw.insert(own_point)
                        continue

                    self.sw.insert(own_point)
                    continue

                if own_point.y < self.bbox.y + self.bbox.h / 2:
                    self.ne.insert(own_point)
                    continue

                self.se.insert(own_point)

            self.data_points.clear()

        if data_point.x < self.bbox.x + self.bbox.w / 2:
            if data_point.y < self.bbox.y + self.bbox.h / 2:
                self.nw.insert(data_point)
                return

            self.sw.insert(data_point)
            return

        if data_point.y < self.bbox.y + self.bbox.h / 2:
            self.ne.insert(data_point)
            return

        self.se.insert(data_point)

    def query_region(self, region: Rect) -> list[DataPoint]:
        if not region.intersects(self.bbox):
            return []

        if self.nw is None:
            return list(filter(region.contains, self.data_points))

        return self.nw.query_region(region) + self.ne.query_region(region) + self.sw.query_region(
            region) + self.se.query_region(region)


if __name__ == "__main__":
    import random

    qt = Quadtree(Rect(0, 0, 128, 128))
    for i in range(8):
        x = random.randint(0, 128)
        y = random.randint(0, 128)
        # print(f"{i}. ({x=}, {y=})")
        qt.insert(DataPoint(x, y, i))

    print(repr(qt))
    print(qt.query_region(Rect(0, 0, 128, 128)))
