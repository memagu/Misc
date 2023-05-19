import pygame as pg
import data_processing as dp

import numpy as np

from typing import Sequence, Callable


class DataVisualiser:
    def __init__(self, data: np.ndarray, position: pg.Vector2 = None,
                 rgba_data_preprocessing: Sequence[Callable[[np.ndarray], np.ndarray]] = None):
        self.data = data
        self.position = position or pg.Vector2()

        pre_rgba_data = data.copy()
        for function in rgba_data_preprocessing or []:
            pre_rgba_data = function(pre_rgba_data)

        self.rgba_data = dp.data_to_rgba(pre_rgba_data)

        print(self.data.shape)
        print(self.rgba_data.shape)

        self.surface = pg.image.frombuffer(self.rgba_data.tobytes(), self.data.shape, "RGBA")

    def scale_rgba(self, r: float = 1, g: float = 1, b: float = 1, a: float = 1) -> "DataVisualiser":
        self.rgba_data = dp.scale_rgba(self.rgba_data, r, g, b, a)
        self.surface = pg.image.frombuffer(self.rgba_data.tobytes(), self.data.shape, "RGBA")
        return self

    def data_intersection_indices(self, other: "DataVisualiser") -> tuple[int, int, int, int]:
        start_row = max(int(other.position.y) - int(self.position.y), 0)
        start_col = max(int(other.position.x) - int(self.position.x), 0)
        end_row = min(self.data.shape[0] + int(other.position.y) - int(self.position.y), self.data.shape[0])
        end_col = min(self.data.shape[1] + int(other.position.x) - int(self.position.x), self.data.shape[1])

        return start_row, start_col, end_row, end_col

    def draw(self, surface: pg.Surface, scale: float = 1, blend_mode: int = pg.BLEND_RGBA_MAX) -> "DataVisualiser":
        scaled_surface = pg.transform.scale_by(self.surface, scale)
        scaled_position = self.position * scale
        surface.blit(scaled_surface, scaled_position, special_flags=blend_mode)
        return self
