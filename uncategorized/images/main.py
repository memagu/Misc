
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from melvec.vec2 import Vec2
from melvec.vec3 import Vec3

WIDTH = 1080
HEIGHT = 1080


def gradient(start_color: Vec3, end_color: Vec3):
    gradient_vector = Vec2(WIDTH, HEIGHT)
    gradient_nvector = gradient_vector / gradient_vector.magnitude()

    gradient = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = gradient.load()
    for y in range(WIDTH):
        for x in range(HEIGHT):
            brightness = (Vec2(x, y) / gradient_vector.magnitude()).dot(gradient_nvector)
            color = end_color * brightness + start_color * (1 - brightness)
            color = int(color.x), int(color.y), int(color.z)
            pixels[x, y] = color
    return gradient


background = gradient(Vec3(0, 255, 255), Vec3(255, 0, 255))
foreground = Image.new("RGB", (WIDTH, HEIGHT), (29, 29, 29))
mask = Image.new("1", (WIDTH, HEIGHT))
mask_draw = ImageDraw.Draw(mask)

text = "text"
font_size = 128
text_font = ImageFont.truetype("arial.ttf", font_size)
text_pos = (WIDTH // 2 - text_font.getlength(text) // 2, HEIGHT // 2 - font_size // 2)

mask_draw.text(text_pos, text, 1, text_font)

img = Image.composite(background, foreground, mask)
background.save("img.jpg", subsampling=0, quality=100)
