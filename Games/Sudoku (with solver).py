import pygame
from copy import deepcopy
import time

pygame.init()

# Settings
resolution = 1200
line_thickness = 2
number_size = 7

# Setup Variables
# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#          [5, 2, 0, 0, 0, 0, 0, 0, 0],
#          [0, 8, 7, 0, 0, 0, 0, 3, 1],
#          [0, 0, 3, 0, 1, 0, 0, 8, 0],
#          [9, 0, 0, 8, 6, 3, 0, 0, 5],
#          [0, 5, 0, 0, 9, 0, 6, 0, 0],
#          [1, 3, 0, 0, 0, 0, 2, 5, 0],
#          [0, 0, 0, 0, 0, 0, 0, 7, 4],
#          [0, 0, 5, 2, 0, 6, 3, 0, 0]]


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


const = deepcopy(board)
running = True
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_blue = (20, 59, 99)
font = pygame.font.SysFont(None, int(resolution / number_size))

color_background = color_white
color_foreground = color_black


# Functions
def make_surface(size, color, alpha):
    surface = pygame.Surface(size)
    surface.set_alpha(alpha)
    surface.fill(color)
    return surface


def draw_select_highlight(x, y, bx, by, ):
    horisontal = make_surface((resolution + 1, resolution / 9 + 1), color_blue, 48)
    vertical = make_surface((resolution / 9 + 1, resolution + 1), color_blue, 48)
    box = make_surface((resolution / 3 + 1, resolution / 3 + 1), color_blue, 48)

    display.blit(horisontal, (0, resolution / 9 * y))
    display.blit(vertical, (resolution / 9 * x, 0))
    display.blit(box, (resolution / 3 * bx, resolution // 3 * by))


def draw_board():
    display.fill(color_background)

    # Selected
    draw_select_highlight(*mouse_pos)

    # Lines
    for i in range(1, 9):
        pygame.draw.rect(display, color_foreground, (resolution * i / 9, 0, line_thickness, resolution))
        pygame.draw.rect(display, color_foreground, (0, resolution * i / 9, resolution, line_thickness))
        if i % 3 == 0:
            pygame.draw.rect(display, color_foreground, (resolution * i / 9, 0, line_thickness * 2, resolution))
            pygame.draw.rect(display, color_foreground, (0, resolution * i / 9, resolution, line_thickness * 2))

    # Numbers
    for y in range(9):
        for x in range(9):
            board_position = board[y][x]
            if board_position != 0:
                display_number(board_position, color_foreground, (resolution * y / 9, resolution * x / 9))

    pygame.display.update()


def display_number(number, color, position):
    message = font.render(str(number), True, color)
    x = position[1] + message.get_rect().width / 2
    y = position[0] + message.get_rect().height / 8
    display.blit(message, (x, y))


def mouse_to_board_pos(mouse_pos):
    mouse_x = mouse_pos[0] // (resolution // 9)
    mouse_y = mouse_pos[1] // (resolution // 9)
    mouse_large_x = mouse_pos[0] // (resolution // 3)
    mouse_large_y = mouse_pos[1] // (resolution // 3)
    return mouse_x, mouse_y, mouse_large_x, mouse_large_y


def validate_single(number, position_x, position_y):
    if number in board[position_y]:
        return False

    for i in range(9):
        if number == board[i][position_x]:
            return False

    for i in range(position_y // 3 * 3, position_y // 3 * 3 + 3):
        for j in range(position_x // 3 * 3, position_x // 3 * 3 + 3):
            if number == board[i][j]:
                return False

    return True


def validate_all():
    # Row
    for i in range(9):
        if sum(set(board[i])) != 45:
            return False

        # Column
        col = set()
        for j in range(9):
            col.add(board[j][i])
        if sum(col) != 45:
            return False

    # Box
    box = set()
    for x in range(3):
        for y in range(3):
            for i in range(y * 3, y * 3 + 3):
                for j in range(x * 3, x * 3 + 3):
                    box.add(board[i][j])
    if sum(box) != 45:
        return False
    # Valid
    return True


def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return False


def solve():
    time.sleep(0.01)
    draw_board()
    found = find_empty()
    if not found:
        return True
    else:
        y, x = found

    for i in range(1, 10):
        if validate_single(i, x, y):
            board[y][x] = i

            if solve():
                return True

            board[y][x] = 0

    return False


# Display Setup
display = pygame.display.set_mode((resolution, resolution), pygame.DOUBLEBUF, 32)
pygame.display.update()
pygame.display.set_caption("Sudoku + Solver by Melker")

# Game
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

        mouse_pos = mouse_to_board_pos(pygame.mouse.get_pos())
        # print(mouse_pos)

        # Scan Edits
        try:
            if event.type == pygame.KEYDOWN and (const[mouse_pos[1]][mouse_pos[0]] == 0 or event.key == pygame.K_SPACE):
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    board[mouse_pos[1]][mouse_pos[0]] = 0
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    board[mouse_pos[1]][mouse_pos[0]] = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    board[mouse_pos[1]][mouse_pos[0]] = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    board[mouse_pos[1]][mouse_pos[0]] = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    board[mouse_pos[1]][mouse_pos[0]] = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    board[mouse_pos[1]][mouse_pos[0]] = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    board[mouse_pos[1]][mouse_pos[0]] = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    board[mouse_pos[1]][mouse_pos[0]] = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    board[mouse_pos[1]][mouse_pos[0]] = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    board[mouse_pos[1]][mouse_pos[0]] = 9
                if event.key == pygame.K_SPACE and mouse_pos == (4, 4, 1, 1):
                    print("solving")
                    solve()
                    running = False
        except Exception:
            pass

        if validate_all():
            print("Correct")
            time.sleep(30)
            running = False

        draw_board()
