import pygame
import time
from planet import Planet


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    try:
        fps = int(1 / delta_time)
    except ZeroDivisionError:
        fps = "∞"
    fps_text = font.render(f"FPS: {fps}", True, text_color)
    fps_outline = font.render(f"FPS: {fps}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


def start():
    global display
    global font
    global planets
    global time_prev

    pygame.init()

    window_resolution = [1200, 900]
    display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
    pygame.display.set_caption(__file__.split("\\")[-1])

    pygame.font.init()
    font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

    time_prev = time.time()

    planets = [Planet(500, [40, 40], [100, 100])]


def update():
    global display
    global dt
    global planets
    global time_prev

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_1:

    # Draw
    display.fill((0, 0, 0))


    for planet in planets:
        pygame.draw.circle(display, planet.color, [planet.posx, planet.posy], planet.radius)
        planet.update_position(dt)


    show_fps(dt)
    pygame.display.update()

    return True


if __name__ == "__main__":
    start()
    while update():
        pass
