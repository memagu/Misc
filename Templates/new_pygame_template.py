import pygame
import time
from typing import List


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)


class Game:
    def __init__(self, *, window_resolution: List[int] = None,
                resizable: bool = True,
                window_caption: str = __file__.split("\\")[-1],
                sub_resolution: List[int] = None):

        pygame.init()
        self.window_resolution = window_resolution or [1200, 900]
        self.display = pygame.display.set_mode(self.window_resolution, resizable)
        pygame.display.set_caption(window_caption)
        self.sub_resolution = sub_resolution or [1200, 900]
        self.transform_resolution = (window_resolution[0] / sub_resolution[0], window_resolution[1] / sub_resolution[1])

        pygame.font.init()
        self.font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)

        self.time_prev = time.perf_counter()
        self.time_now = 0
        self.dt = 0

    def show_fps(self, delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
        fps_text = self.font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
        fps_outline = self.font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
        self.display.blit(fps_outline, (-1, -1))
        self.display.blit(fps_outline, (-1, 1))
        self.display.blit(fps_outline, (1, -1))
        self.display.blit(fps_outline, (1, 1))
        self.display.blit(fps_text, (0, 0))

    def run(self):
        while True:
            self.time_now = time.perf_counter()
            self.dt, self.time_prev = self.time_now - self.time_prev, time_now

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                # Resize window event
                if event.type == pygame.VIDEORESIZE:
                    self.window_resolution = [event.w, event.h]
                    self.transform_resolution = [window_resolution[0] / sub_resolution[0], window_resolution[1] / sub_resolution[1]]
                    self.display = pygame.display.set_mode(self.window_resolution, pygame.RESIZABLE)

                # Keypresses
                # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_1:

            # Draw
            display.fill(color_black)

            show_fps(dt)
            pygame.display.update()
            if fps > 0:
                clock.tick(fps)








if __name__ == "__main__":
    print(Color.blue)

    while run:

        # Calculate dt
        time_now = time.time()
        dt, time_prev = time_now - time_prev, time_now

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Resize window event
            if event.type == pygame.VIDEORESIZE:
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Draw
        display.fill((0, 0, 0))

        show_fps(dt)
        pygame.display.update()
        if fps > 0:
            clock.tick(fps)
