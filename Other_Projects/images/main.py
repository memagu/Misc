from typing import Tuple
from typing import List

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from melvec.melvec2 import Vec2
from melvec.melvec3 import Vec3

WIDTH = 10
HEIGHT = 10

def gradient(start_color: np.array, end_color: np.array):
    gradient_direction
    print("g", gradient_vector)
    gradient = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = gradient.load()
    for y in range(1, WIDTH):
        for x in range(1, HEIGHT):
            brightness = numpy.array(x, y).normalize().dot(gradient_vector)
            pixels[x, y] = (tuple(end_color * brightness + start_color * (1-brightness)))
    # return gradient

background = Image.new("RGB", (WIDTH, HEIGHT), (255, 0, 0))
foreground = Image.new("RGB", (WIDTH, HEIGHT), (29, 29, 29))
mask = Image.new("1", (WIDTH, HEIGHT))
mask_draw = ImageDraw.Draw(mask)

text = "text"
font_size = 128
text_font = ImageFont.truetype("arial.ttf", font_size)
text_pos = (WIDTH // 2 - text_font.getlength(text) // 2, HEIGHT // 2 - font_size // 2)

mask_draw.text(text_pos, text, 1, text_font)

img = Image.composite(background, foreground, mask)
img.save("img.jpg")

img = gradient((255, 0, 0), (0, 0, 255))
img.save("img.jpg")

