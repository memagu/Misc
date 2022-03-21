import pygame
import math
import random

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
    def __init__(self, position, velocity, grip, dimensions, up_key, down_key, color, moving=0):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.velocity = velocity
        self.grip = grip
        self.dimensions = dimensions
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.up_key = eval(f"pygame.K_{up_key}")
        self.down_key = eval(f"pygame.K_{down_key}")
        self.color = color
        self.moving = moving

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

    def collides_with_ball(self, balls: []):
        for other in balls:
            if other is not self:
                distance = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
                if distance <= self.radius + other.radius:
                    return other
        return

    def bounce(self, other, do_other=True):
        sum_m = self.radius + other.radius
        p1_1_x = ((self.radius - other.radius) / sum_m) * self.x_vel
        p1_2_x = (other.radius * 2 / sum_m) * other.x_vel

        p1_1_y = ((self.radius - other.radius) / sum_m) * self.y_vel
        p1_2_y = (other.radius * 2 / sum_m) * other.y_vel

        if do_other:
            other.bounce(self, False)
            try:
                angle = math.atan((other.y - self.y) / (other.x - self.x))
            except ZeroDivisionError:
                angle = math.pi / 2 * (1 if (other.y < self.y) else 3)
            if self.x < other.x:
                angle += math.pi
            self.x = other.x + math.cos(angle) * (self.radius + other.radius + (2 >> 31))
            self.y = other.y + math.sin(angle) * (self.radius + other.radius + (2 >> 31))
            self.position = [self.x, self.y]

        self.x_vel = p1_1_x + p1_2_x
        self.y_vel = p1_1_y + p1_2_y

    def collides_with_paddle(self, paddles: []):
        for paddle in paddles:
            if paddle.y < self.y < paddle.y + paddle.height and abs(
                    self.x - (paddle.x + (paddle.width >> 1))) <= self.radius + (paddle.width >> 1):
                return paddle
        return

    def update_position(self, dt):
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt
        self.position = [self.x, self.y]

    def reset(self, window_resolution, new_vel_min, new_vel_max):
        self.x = window_resolution[0] >> 1
        self.y = window_resolution[1] >> 1
        self.x_vel *= -1
        self.y_vel = random.randint(new_vel_min, new_vel_max)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius)


def main():
    print(__file__.split("\\")[-1])


if __name__ == "__main__":
    main()
