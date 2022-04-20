import pygame
from helpers import *

pygame.init()

window_resolution = [1200, 1200]
image_resolution = [8, 8]
transform_resolution = (window_resolution[0] / image_resolution[0], window_resolution[1] / image_resolution[1])
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

background_layer = pygame.Surface(window_resolution)
piece_layer = pygame.Surface(window_resolution, pygame.SRCALPHA, 32)
move_layer = pygame.Surface(window_resolution, pygame.SRCALPHA, 32)

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

# Text
pygame.font.init()
fps_font = pygame.font.SysFont("leelawadeeuisemilight", window_resolution[1] // 32)
square_font = pygame.font.SysFont("leelawadeeuisemilight", int(transform_resolution[1] / 8))


def draw_background(surface, font, light_square_color, dark_square_color, square_size):
    sqsize_x, sqsize_y = square_size
    for y in range(8):
        for x in range(8):
            square_color = list(light_square_color if y % 2 == x % 2 else dark_square_color)
            text_color = list(dark_square_color if y % 2 == x % 2 else light_square_color)

            pygame.draw.rect(surface, square_color, [x * sqsize_x, y * sqsize_y, sqsize_x, sqsize_y])
            square_text = font.render(chr(97 + x) + str(8 - y), True, text_color)
            square_text_width = square_text.get_width()
            square_text_height = square_text.get_height()
            square_text_rect = square_text.get_rect(
                center=[x * sqsize_x + square_text_width, (y + 1) * sqsize_y - square_text_height])
            surface.blit(square_text, square_text_rect)


def draw_pieces(surface, board, square_size, scale):
    sqsize_x, sqsize_y = square_size
    for y in range(8):
        for x in range(8):
            if board.board[y][x]:
                image = board.get_piece([x, y]).image
                image = pygame.transform.scale(image, [sqsize_x * scale, sqsize_y * scale])
                image_rect = image.get_rect(center=[x * sqsize_x + sqsize_x / 2, y * sqsize_y + sqsize_y / 2])
                surface.blit(image, image_rect)


def draw_moves(surface, board, square_size, target):
    sqsize_x, sqsize_y = square_size
    target_x, target_y = target
    piece = board.get_piece([target_x, target_y])
    if piece:
        for y in range(8):
            for x in range(8):
                if board.try_move(target, [x, y]):
                    color = color_killer_red if board.get_piece([x, y]) else color_select_blue
                    pygame.draw.circle(surface, color,
                                       [x * sqsize_x + sqsize_x / 2, y * sqsize_y + sqsize_y / 2], sqsize_y / 8)


b = Board()
# b.set_board_from_code("rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR")
b.set_board_from_code("rnbqkbnr/00000000/000N0N00/000b0000/00NNr000/00000000/000Q0000/RNB0KBNR")

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
            new_w = (int(event.w) // 8) * 8
            new_h = (int(event.h) // 8) * 8
            window_resolution = [new_w, new_h]
            display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
            background_layer = pygame.Surface(window_resolution)
            piece_layer = pygame.Surface(window_resolution, pygame.SRCALPHA, 32)
            move_layer = pygame.Surface(window_resolution, pygame.SRCALPHA, 32)
            transform_resolution = (new_w / image_resolution[0], new_h / image_resolution[1])
            square_font = pygame.font.SysFont("leelawadeeuisemilight", int(transform_resolution[1] / 8))

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:

    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = [mouse_pos[0] // int(transform_resolution[0]), mouse_pos[1] // int(transform_resolution[1])]
    # print(mouse_pos, b.get_piece(mouse_pos))

    # Draw

    display.fill(color_black)

    draw_background(display, square_font, color_cream, color_walnut, transform_resolution)
    draw_pieces(display, b, transform_resolution, 0.9)
    draw_moves(display, b, transform_resolution, mouse_pos)

    # show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
