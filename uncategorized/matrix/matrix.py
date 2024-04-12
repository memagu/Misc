import pygame
import time
import random

pygame.init()

WINDOW_RESOLUTION = (1280, 720)
char_height = 16
image_resolution = [WINDOW_RESOLUTION[0] // char_height * 2, WINDOW_RESOLUTION[1] // char_height]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

# Text
pygame.font.init()
font = pygame.font.Font("matrix_code_nfi.ttf", int(transform_resolution[1]))

fps_font = pygame.font.SysFont(None, WINDOW_RESOLUTION[0] // 32)




charachters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$',
               '+', '-', '*', '/', '=', '"', "'", '#', '&', '_', '(', ')', ',', '.', ';', ':', '?', '!', '\\', '|', '{',
               '}', '<', '>', '[', ']', '^', '~']

charachters = ['0', '1']

print(font.size("M"))

class Codedrop:
    def __init__(self, char, pos, is_child=True, decay_speed=128):
        self.char = char
        self.pos = pos
        self.is_child = is_child
        self.decay_speed = decay_speed
        self.r = 255
        self.g = 255
        self.b = 255
        self.color = self.r, self.g, self.b
        self.children = 0

    def update_color(self, dt):
        self.r = max(0, self.r - self.decay_speed * 16 * dt)
        self.g = max(0, self.g - self.decay_speed * dt)
        self.b = max(0, self.b - self.decay_speed * 16 * dt)
        self.color = self.r, self.g, self.b

    def update_char(self, char_set):
        self.char = random.choice(char_set)

    def update_position(self):
        self.pos = (self.pos[0], self.pos[1] + 1)

    def crate_child(self):
        return Codedrop(random.choice(self.char), self.pos)

    def draw(self, font, transform_resolution):
        font_size = font.size(self.char)
        x_offset = (transform_resolution[0] - font_size[0]) / 2
        y_offset = (transform_resolution[1] - font_size[1]) / 2
        display.blit(font.render(self.char, True, self.color), (
            self.pos[0] * transform_resolution[0] + x_offset, self.pos[1] * transform_resolution[1] + y_offset))


code_drops = []
tick = 0
ticks_per_second = 64


def show_fps(delta_time, font, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    last_tick = tick
    tick = (tick + ticks_per_second * dt) % 1000000007

    tick_int = int(tick)
    last_tick_int = int(last_tick)
    different_tick = last_tick_int != tick_int

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WINDOW_RESOLUTION = event.w, event.h
            image_resolution = [WINDOW_RESOLUTION[0] // char_height * 2, WINDOW_RESOLUTION[1] // char_height]
            transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])


    if tick_int % 3 == 0 and different_tick:
        code_drops.append(Codedrop(random.choice(charachters), (random.randint(0, image_resolution[0]), 0), False, 0))


    display.fill(color_black)

    # for i in range(image_resolution[0]):
    #     pygame.draw.line(display, (29, 29, 29), (i * transform_resolution[0], 0),
    #                      (i * transform_resolution[0], window_resolution[1]))
    # for i in range(image_resolution[1]):
    #     pygame.draw.line(display, (29, 29, 29), (0, i * transform_resolution[1]),
    #                      (window_resolution[0], i * transform_resolution[1]))

    temp_add = []
    temp_remove = []

    for code_drop in code_drops:

        if code_drop.pos[1] == image_resolution[1]:
            temp_remove.append(code_drop)

        if tick_int % 4 == 0 and different_tick and not code_drop.is_child:
            temp_add.append(code_drop.crate_child())
            code_drop.update_char(charachters)
            code_drop.update_position()

        code_drop.draw(font, transform_resolution)
        if random.randint(0, 750) == 0:
            code_drop.update_char(charachters)

        code_drop.update_color(dt)

        if code_drop.g == 0:
            temp_remove.append(code_drop)

    for code_drop in temp_add:
        # print("to_add: ", code_drop)
        code_drops.append(code_drop)

    for code_drop in temp_remove:
        # print("to_remove: ", code_drop)
        code_drops.remove(code_drop)

    print(len(code_drops))

    # show_fps(dt, fps_font)
    pygame.display.update()
    clock.tick(480)
