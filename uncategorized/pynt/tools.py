import pygame
import util
from typing import List, Tuple

run_tools = True


def fill_bfs(surface: pygame.Surface, coordinate: Tuple[int, int], color: pygame.Color) -> None:
    width, height = surface.get_width(), surface.get_height()
    sample = surface.get_at(coordinate)
    visited = set()
    queue = [coordinate]

    while queue:
        if not run_tools:
            return

        x, y = queue.pop(0)
        surface.set_at((x, y), color)
        pygame.display.update()

        for new_y, new_x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if not util.in_bounds(new_x, 0, width - 1):
                continue

            if not util.in_bounds(new_y, 0, height - 1):
                continue

            if (new_coord := (new_x, new_y)) in visited or surface.get_at(new_coord) != sample:
                continue

            queue.append(new_coord)
            visited.add(new_coord)


# WIP
def brush(surface: pygame.Surface, coordinate: Tuple[int, int], color: pygame.Color) -> None:
    pygame.draw.circle(surface, color, coordinate, 5)
