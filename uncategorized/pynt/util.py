import math


def in_bounds(value, min, max):
    return min <= value <= max


def rainbow(angle: float, scale: float = 255):
    r = math.sin(angle) * 0.5 + 0.5
    g = math.sin(angle + math.pi * 2 / 3) * 0.5 + 0.5
    b = math.sin(angle + math.pi * 4 / 3) * 0.5 + 0.5
    return r * scale, g * scale, b * scale
