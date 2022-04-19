import pygame
from helpers import *

pygame.init()

window_resolution = [1200, 900]
image_resolution = [1200, 900]
transform_resolution = (window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

vertical_separation = 72
sliders = []

sliders.append(Slider([32, 40 + vertical_separation * 0], "x", min_value=0, max_value=window_resolution[0], value=window_resolution[0] / 2))
sliders.append(Slider([32, 40 + vertical_separation * 1], "y", min_value=0, max_value=window_resolution[1], value=window_resolution[1] / 2))
sliders.append(Slider([32, 40 + vertical_separation * 2], "angle", min_value=-math.pi, max_value=math.pi, value=0))
sliders.append(Slider([32, 40 + vertical_separation * 3], "length", min_value=0, max_value=1000, value=200))
sliders.append(Slider([32, 40 + vertical_separation * 4], "min_value", min_value=-100, max_value=100, value=-50))
sliders.append(Slider([32, 40 + vertical_separation * 5], "max_value", min_value=-100, max_value=100, value=50))

main_slider = Slider([sliders[0].value, sliders[1].value], "", sliders[2].value, sliders[3].value, sliders[4].value, sliders[5].value, 0)

while run:

    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = [event.w, event.h]
            transform_resolution = (window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])


        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    # Draw
    display.fill(color_black)

    for slider in sliders:
        slider.update()
        slider.draw_slider(display, color_white)

    main_slider.update()
    main_slider.pos = [sliders[0].value, sliders[1].value]
    main_slider.angle = sliders[2].value
    main_slider.length = sliders[3].value
    main_slider.min_value = sliders[4].value
    main_slider.max_value = sliders[5].value
    main_slider.update_angle()

    main_slider.draw_slider(display, color_white)

    # show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
