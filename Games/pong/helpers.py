import pygame
import math

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


def show_fps(surface, delta_time, font, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


class Paddle:
    def __init__(self, position, velocity, dimensions, up_key, down_key, color):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.velocity = velocity
        self.dimensions = dimensions
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.up_key = eval(f"pygame.K_{up_key}")
        self.down_key = eval(f"pygame.K_{down_key}")
        self.color = color

    def move_up(self, dt):
        self.y -= self.velocity * dt
        self.position = [self.x, self.y]

    def move_down(self, dt):
        self.y += self.velocity * dt
        self.position = [self.x, self.y]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])


class Ball:
    def __init__(self, position, velocity, radius, color):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.velocity = velocity
        self.x_vel = velocity[0]
        self.y_vel = velocity[1]
        self.radius = radius
        self.color = color

    def collides_with_ball(self, other):
        distance = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        if distance <= self.radius - other.radius:
            return True
        return False

    def collides_with_paddle(self, paddles: []):
        for paddle in paddles:
            if paddle.y < self.y < paddle.y + paddle.height and abs(self.x - (paddle.x + (paddle.width >> 1))) <= self.radius + (paddle.width >> 1):
                return True
        return False

    def update_position(self, dt):
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt
        self.position = [self.x, self.y]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)
