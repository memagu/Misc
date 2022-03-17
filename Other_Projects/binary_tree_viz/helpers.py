import random

import pygame
import time
import math

# Helpful variables
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


# Helpful functions
def show_fps(surface, font, dt, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / dt)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / dt)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


# Your code here
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.__dict__)


def construct_binary_tree(root: Node, depth: int) -> Node:
    if depth != 0:
        root.left = construct_binary_tree(Node(root.value + 'l'), depth - 1)
        root.right = construct_binary_tree(Node(root.value + 'r'), depth - 1)
        return root


def construct_random_binary_tree(root: Node, depth: int, probability: float) -> Node:
    if depth != 0:
        root.left = construct_random_binary_tree(Node(root.value + 'l'), depth - 1, probability * 0.99) if random.randint(0, 100) / 100 <= probability else None
        root.right = construct_random_binary_tree(Node(root.value + 'r'), depth - 1, probability * 0.99) if random.randint(0, 100) / 100 <= probability else None
        return root


def print_binary_tree(root: Node, depth=0):
    print("\t" * depth, root.value, sep='')
    if root.left:
        print_binary_tree(root.left, depth + 1)
    if root.right:
        print_binary_tree(root.right, depth + 1)


def binary_tree_position_list(root: Node, result: [str] = []):
    result.append(root.value)
    if root.left:
        binary_tree_position_list(root.left, result)
    if root.right:
        binary_tree_position_list(root.right, result)
    return result


def string_to_position(string: str, tree_depth: int, window_resolution: [int]) -> [int]:
    char_to_coefficient = {'l': -1, 's': 1, 'r': 1}
    row_height = window_resolution[1] / (tree_depth + 1)

    y = len(string) * row_height
    x = 0

    for i, char in enumerate(string):
        x += (window_resolution[0] / (2 ** (i+1))) * char_to_coefficient[char]

    return [x, y]


def draw_binary_tree(root: Node, tree_depth, window_resolution, surface):
    pygame.draw.circle(surface, color_white, string_to_position(root.value, tree_depth, window_resolution), 5)
    # pygame.display.update()

    if root.left:
        pygame.draw.line(surface,
                         color_white,
                         string_to_position(root.value, tree_depth, window_resolution),
                         string_to_position(root.left.value, tree_depth, window_resolution))
        draw_binary_tree(root.left, tree_depth, window_resolution, surface)

    if root.right:
        pygame.draw.line(surface,
                         color_white,
                         string_to_position(root.value, tree_depth, window_resolution),
                         string_to_position(root.right.value, tree_depth, window_resolution))
        draw_binary_tree(root.right, tree_depth, window_resolution, surface)

























if __name__ == "__main__":
    print("\\".join(__file__.split("\\")[-2::]))
