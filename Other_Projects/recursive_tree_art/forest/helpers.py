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


def draw_tree(root: Branch, surface: pygame.surface, color: (int, int, int) = color_white, rainbow: bool = False):
    color = color if not rainbow else color_rainbow(root.angle)
    pygame.draw.aaline(surface, color, root.pos, root.end)

    if root.left:
        draw_tree(root.left, surface, color, rainbow)

    if root.right:
        draw_tree(root.right, surface, color, rainbow)

    if not (root.right or root.left):
        pygame.draw.circle(surface, color, root.end, 5)


if __name__ == "__main__":
    print(__file__.split("\\")[-1])
