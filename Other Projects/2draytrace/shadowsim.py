import pygame
import time
import math


pygame.init()

WINDOW_RESOLUTION = (1200, 900)
image_resolution = [1200, 900]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption("SET CAPTION HERE")

#window bounding lines
padding = 100

b0x = padding
b1x = WINDOW_RESOLUTION[0] - padding
b0y = padding
b1y = WINDOW_RESOLUTION[1] - padding

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

#constats
number_of_rays = 6
bounces = 8
ray_separation = 2 * math.pi / number_of_rays
# ray_separation = 0.0000001
TWO_PI = 2 * math.pi

c_1q = TWO_PI / 4
c_2q = TWO_PI / 2
c_3q = TWO_PI * 3 / 4


class Shape:
 None

class Ray:
    def __init__(self, point, angle):
        self.point = point
        self.angle = angle

    def collides_with(self, other):
        pass



def vector_box_intersect(angle, vector_origin, corner_tl, corner_br):

    vox, voy = vector_origin

    c0x, c0y = corner_tl
    c1x, c1y = corner_br

    k = 0.000001 if math.tan(angle) == 0 else math.tan(angle)
    # k = math.tan(angle)
    m = voy - k * vox


    if angle > c_3q:
        hit1 = (c1x, k * c1x + m)
        hit2 = ((c0y - m) / k, c0y)

    elif angle > c_2q:
        hit1 = (c0x, c0x * k + m)
        hit2 = ((c0y - m) / k, c0y)

    elif angle > c_1q:
        hit1 = (c0x, c0x * k + m)
        hit2 = ((c1y - m) / k, c1y)

    else:
        hit1 = (c1x, k * c1x + m)
        hit2 = ((c1y - m) / k, c1y)

    d1 = ((vox - hit1[0]) ** 2 + (voy - hit1[1]) ** 2) ** 0.5
    d2 = ((vox - hit2[0]) ** 2 + (voy - hit2[1]) ** 2) ** 0.5

    if d1 < d2:
        # vertical
        return hit1, math.pi - angle if angle <= math.pi else math.pi * 2 - (angle - math.pi)
    else:
        # horizontal
        return hit2, math.pi * 2 - angle


def draw_ray(pos, angle, boundry_corner_0, boundry_corner_1, bounce_depth):
    if bounce_depth < 1:
        return
    bounce_depth -= 1

    intersect, angle_reflected = vector_box_intersect(angle, pos, boundry_corner_0, boundry_corner_1)

    pygame.draw.aaline(display, color_white, pos, intersect)

    draw_ray(intersect, angle_reflected, boundry_corner_0, boundry_corner_1, bounce_depth)


while run:

    #if ray_separation < TWO_PI / number_of_rays:
    #    ray_separation += 0.00001

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        mouse_pos = pygame.mouse.get_pos()

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Keypresses
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT]:
    #    ray_separation += 0.001
    #
    #if keys[pygame.K_RIGHT]:
    #    ray_separation -= 0.001

    display.fill(color_black)

    pygame.draw.rect(display, color_red, [b0x, b0y, b1x - 100, b1y - 100], True)

    for i in range(1, number_of_rays + 1):
        angle = ray_separation * i

        draw_ray(mouse_pos, angle, (b0x, b0y), (b1x, b1y), 20)

       # intersect, angle_reflected = vector_box_intersect(angle, mouse_pos, (b0x, b0y), (b1x, b1y))

       # pygame.draw.aaline(display, color_white, mouse_pos, intersect)

       # intersect2, _ = vector_box_intersect(angle_reflected, intersect, (b0x, b0y), (b1x, b1y))

       # pygame.draw.aaline(display, color_blue, intersect, intersect2)




    pygame.display.update()
    clock.tick(480)
