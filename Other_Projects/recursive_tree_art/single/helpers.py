import pygame
import time
import math
import random


# Misc variables

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


# Functions
def show_fps(surface, font, dt, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / dt)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / dt)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


def color_rainbow(angle):
    r = (math.sin(angle) + 1) / 2
    g = (math.sin(angle + math.pi / 1.5) + 1) / 2
    b = (math.sin(angle + 2 * math.pi / 1.5) + 1) / 2
    return [255 * r, 255 * g, 255 * b]


def distance(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))]) ** 0.5


def distance_squared(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))])


# Classes
class Slider:
    def __init__(self, pos: [int, int], tag: str, angle: float = 0, length: float = 200, min_value: float = 0,
                 max_value: float = 1, value: float = 0.5):
        self.pos = pos
        self.tag = tag
        self.angle = angle
        self.length = length
        self.end = [self.pos[0] + math.cos(self.angle) * self.length, self.pos[1] + math.sin(self.angle) * self.length]
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.value_amplitude = (self.value - self.min_value) / (self.max_value - self.min_value) * self.length
        self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                          self.pos[1] + math.sin(self.angle) * self.value_amplitude]
        self.font = pygame.font.SysFont("leelawadeeuisemilight", 16)

    def draw_slider(self, surface, color: [int, int, int] = color_white,):
        pygame.draw.aaline(surface, color, self.pos, self.end)
        pygame.draw.circle(surface, color, self.value_pos, 8)

        value_text = self.font.render(str(round(self.value, 3)), True, color)
        value_text_rect = value_text.get_rect(center=[self.value_pos[0], self.value_pos[1] - 24])
        surface.blit(value_text, value_text_rect)

        tag_text = self.font.render(self.tag, True, color)
        tag_text_rect = tag_text.get_rect(center=[(self.pos[0] + self.end[0]) / 2,
                                                  (self.pos[1] + self.end[1]) / 2 + 24])
        surface.blit(tag_text, tag_text_rect)

    def pos_to_value(self, pos):
        d1 = distance_squared(self.pos, pos) if distance_squared(pos, self.end) <= self.length ** 2 else 0
        d2 = distance(self.pos, self.end)
        return d1 ** 0.5 / d2 * (self.max_value - self.min_value) - abs(self.min_value)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and distance_squared(mouse_pos, self.value_pos) <= 32 ** 2:
            self.value = max(min(self.pos_to_value(mouse_pos), self.max_value), self.min_value)
            self.value_amplitude = (self.value - self.min_value) / (self.max_value - self.min_value) * self.length
            self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                              self.pos[1] + math.sin(self.angle) * self.value_amplitude]

    def update_angle(self):
        self.end = [self.pos[0] + math.cos(self.angle) * self.length, self.pos[1] + math.sin(self.angle) * self.length]
        self.value_pos = [self.pos[0] + math.cos(self.angle) * self.value_amplitude,
                          self.pos[1] + math.sin(self.angle) * self.value_amplitude]


# Your code here
class Branch:
    def __init__(self, pos, length, angle):
        self.pos = pos
        self.length = length
        self.angle = angle
        self.end = [self.pos[0] + math.cos(angle) * length, self.pos[1] + math.sin(angle) * -length]
        self.left = None
        self.right = None


def construct_tree(root: Branch, tree_depth: int, branching_probability: float, angle_noise_amplitude: float = 0, branch_legth_coefficient: float = 1, left_branch_angle: float = math.pi / 36, right_branch_angle: float = -math.pi / 36) -> Branch:
    if tree_depth:
        root.left = construct_tree(Branch(root.end, root.length * branch_legth_coefficient, root.angle + left_branch_angle),
                                   tree_depth - 1,
                                   branching_probability,
                                   angle_noise_amplitude,
                                   branch_legth_coefficient,
                                   left_branch_angle + random.randint(-100, 100) / 100 * angle_noise_amplitude,
                                   right_branch_angle - random.randint(-100, 100) / 100 * angle_noise_amplitude) if random.randint(0, 100) / 100 <= branching_probability else None

        root.right = construct_tree(Branch(root.end, root.length * branch_legth_coefficient, root.angle + right_branch_angle),
                                    tree_depth - 1,
                                    branching_probability,
                                    angle_noise_amplitude,
                                    branch_legth_coefficient,
                                    left_branch_angle + random.randint(-100, 100) / 100 * angle_noise_amplitude,
                                    right_branch_angle - random.randint(-100, 100) / 100 * angle_noise_amplitude) if random.randint(0, 100) / 100 <= branching_probability else None

        return root


def traverse_tree(root: Branch, function, *args):
    function(root, *args)
    if root.left:
        traverse_tree(root.left, function, *args)
    if root.right:
        traverse_tree(root.right, function, *args)


def draw_tree(root: Branch, surface: pygame.surface, color: (int, int, int) = color_white, rainbow: bool = False):
    color = color if not rainbow else color_rainbow(root.angle)
    pygame.draw.aaline(surface, color, root.pos, root.end)

    if root.left:
        draw_tree(root.left, surface, color, rainbow)

    if root.right:
        draw_tree(root.right, surface, color, rainbow)

    if not (root.right or root.left):
        pygame.draw.circle(surface, color, root.end, 5)


def draw_branch(root: Branch, surface: pygame.surface, color: (int, int, int) = color_white, rainbow: bool = False):
    color = color if not rainbow else color_rainbow(root.angle)
    pygame.draw.aaline(surface, color, root.pos, root.end)

    if not (root.right or root.left):
        pygame.draw.circle(surface, color, root.end, 5)


def draw_branch_polygon(root: Branch, surface: pygame.surface, base_width_ratio: float = 0.1,
                        color: (int, int, int) = color_white, rainbow: bool = False):

    color = color if not rainbow else color_rainbow(root.angle)

    half_base_width = root.length * base_width_ratio / 2

    if root.left:
        half_top_width = root.left.length * base_width_ratio / 2
    elif root.right:
        half_top_width = root.right.length * base_width_ratio / 2
    else:
        half_top_width = 0

    if half_base_width > 0.6:
        cos_normal = math.cos(root.angle + math.pi / 2)
        sin_normal = -math.sin(root.angle + math.pi / 2)

        bl = [root.pos[0] - cos_normal * half_base_width, root.pos[1] - sin_normal * half_base_width]
        br = [root.pos[0] + cos_normal * half_base_width, root.pos[1] + sin_normal * half_base_width]
        tl = [root.end[0] - cos_normal * half_top_width, root.end[1] - sin_normal * half_top_width]
        tr = [root.end[0] + cos_normal * half_top_width, root.end[1] + sin_normal * half_top_width]

        pygame.draw.polygon(surface, color, [bl, br, tr, tl])
    else:
        pygame.draw.aaline(surface, color, root.pos, root.end)

    pygame.draw.circle(surface, color, root.end, half_top_width)

    if not (root.right or root.left):
        pygame.draw.circle(surface, color, root.end, 5)


def main():
    display = pygame.display.set_mode([1600, 1200], pygame.RESIZABLE)

    root = Branch([1600 / 2, 1200 - (1200 >> 3)],
                  3 / 4 * 1200 / sum(
                      [0.7 ** i for i in range(12)]),
                  math.pi / 2)

    tree = construct_tree(root,
                          12,
                          1,
                          0.3,
                          0.7,
                          math.pi / 4,
                          7 * math.pi / 4)

    for i in range(100):
        display.fill(color_black)
        # draw_tree(tree, display, color_white, True)
        traverse_tree(root, draw_branch_polygon, display, 0.2, color_white, True)
        pygame.display.update()



if __name__ == "__main__":
    print(__file__.split("\\")[-1])

    import cProfile
    cProfile.run("main()", "output.dat")

    import pstats
    from pstats import SortKey

    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()

    with open("output_calls.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()

