import os
import shutil
import keyboard
import mouse
from PIL import Image
from google_images_download import google_images_download
import time

brush_sizes = [3, 7, 19, 41]
color_pos_val = {'white': (110, 640, (255, 255, 255)), 'black': (110, 664, (0, 0, 0)),
                 'gray': (110 + 24, 640, (158, 158, 158)), 'dark_gray': (110 + 24, 664, (76, 76, 76)),
                 'red': (110 + 24 * 2, 640, (239, 19, 11)), 'dark_red': (110 + 24 * 2, 664, (116, 11, 7)),
                 'orange': (110 + 24 * 3, 640, (255, 113, 0)), 'dark_orange': (110 + 24 * 3, 664, (194, 56, 0)),
                 'yellow': (110 + 24 * 4, 640, (255, 228, 0)), 'dark_yellow': (110 + 24 * 4, 664, (232, 162, 0)),
                 'green': (110 + 24 * 5, 640, (0, 204, 0)), 'dark_green': (110 + 24 * 5, 664, (0, 85, 16)),
                 'cyan': (110 + 24 * 6, 640, (0, 178, 255)), 'dark_cyan': (110 + 24 * 6, 664, (0, 86, 158)),
                 'blue': (110 + 24 * 7, 640, (35, 31, 211)), 'dark_blue': (110 + 24 * 7, 664, (14, 8, 101)),
                 'purple': (110 + 24 * 8, 640, (163, 0, 186)), 'dark_purple': (110 + 24 * 8, 664, (85, 0, 105)),
                 'pink': (110 + 24 * 9, 640, (211, 124, 170)), 'dark_pink': (110 + 24 * 9, 664, (167, 85, 116)),
                 'brown': (110 + 24 * 10, 640, (160, 82, 45)), 'dark_brown': (110 + 24 * 10, 664, (99, 58, 13))}


def rgb_distance(rgb1: (int, int, int), rgb2: (int, int, int)) -> int:
    return ((rgb2[0] - rgb1[0]) ** 2 + (rgb2[1] - rgb1[1]) ** 2 + (rgb2[2] - rgb1[2]) ** 2) ** 0.5


def closest_color_coord(rgb: (int, int, int)) -> (int, int):
    minimum = [512, 0, 0]
    for (key, value) in color_pos_val.items():
        dist = rgb_distance(value[2], rgb)
        if minimum[0] > dist:
            minimum[0] = dist
            minimum[1], minimum[2] = value[0], value[1]

    return minimum[1:]


scribble_window_size = (800, 600)

google_images_download.googleimagesdownload().single_image(input('Enter image url: '))

image = Image.open('downloads/' + os.listdir("downloads")[0], 'r').resize(scribble_window_size).convert('RGB')
image_width, image_height = image.size

for i in range(4, 0, -1):
    print(f"Position mouse, drawing starts in {i} seconds!")
    time.sleep(1)

print('Starting to draw!')

start_x, start_y = mouse.get_position()

brush_size = brush_sizes[2]

for y in range(0, image_height, brush_size):
    for x in range(0, image_width, brush_size):

        if keyboard.is_pressed('q'):
            quit()

        pixel = image.getpixel((x, y))

        r, g, b = pixel[:3]

        color_x, color_y = closest_color_coord((r, g, b))
        mouse.move(color_x + start_x, color_y + start_y)
        mouse.click(button='left')

        mouse.move(x + start_x, y + start_y)
        mouse.click(button='left')

        time.sleep(0.015)

shutil.rmtree('downloads', ignore_errors=False, onerror=None)
quit()
