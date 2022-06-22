import pygame
import time
from typing import List

class Game:
    def __int__(self, *, window_resolution: List[int] = None,
                resizable: bool = True,
                window_caption: str = __file__.split("\\")[-1],
                sub_resolution: List[int] = None):

        self.window_resolution = window_resolution or [1200, 900]
        self.display = pygame.display.set_mode(self.window_resolution, resizable)
        self.sub_resolution = sub_resolution or [1200, 900]
        self.transform_resolution = (window_resolution[0] / sub_resolution[0], window_resolution[1] / sub_resolution[1])

    def run(self):
        raise NotImplementedError

def setup():
    pygame.init()

    window_resolution = [1200, 900]
    display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
    pygame.display.set_caption(__file__.split("\\")[-1])

    run = True
    time_prev = time.time()

    # Text
    pygame.font.init()
    font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))





if __name__ == "__main__":
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
