import pygame
import abc
import copy

pygame.init()

WINDOW_RESOLUTION = (1200, 1200)
image_resolution = [8, 8]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE, depth=32)
pygame.display.set_caption("SET CAPTION HERE")

run = True

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)
color_cream = (255, 253, 208)
color_walnut = (93, 67, 44)
color_select_blue = (37, 122, 253)

pygame.font.init()
font = pygame.font.SysFont('leelawadeeuisemilight', WINDOW_RESOLUTION[0] // 64)


class Piece(metaclass=abc.ABCMeta):
    def __init__(self, pos, team, image_name):
        self.team = team
        self.pos = pos
        self.image = pygame.image.load(image_name)

    def __str__(self):
        return self.__dict__['name']

    def __repr__(self):
        return self.__dict__

    @abc.abstractmethod
    def possible(self, target_pos):
        pass

    def draw(self, display):
        scaled = pygame.transform.scale(self.image, [transform_resolution[0], transform_resolution[1]])
        display.blit(scaled, [self.pos[0] * transform_resolution[0], self.pos[1] * transform_resolution[1]])

    def place(self, pos):
        if 0 <= pos <= 7:
            self.pos = pos
        else:
            raise Exception


class Movable(Piece):
    def __init__(self, pos, team, image_name):
        self.moved = False
        super().__init__(pos, team, image_name)


class King(Movable):
    def __init__(self, pos, team):
        self.name = 'King'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        return abs(self.pos[0] - target_pos[0]) <= 1 and abs(self.pos[1] - target_pos[1]) <= 1


class Queen(Piece):
    def __init__(self, pos, team):
        self.name = 'Queen'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        return target_pos[0] == self.pos[0] \
               or target_pos[1] == self.pos[1] \
               or abs(self.pos[0] - target_pos[0]) == abs(self.pos[1] - target_pos[1])


class Rook(Movable):
    def __init__(self, pos, team):
        self.name = 'Rook'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        return target_pos[0] == self.pos[0] or target_pos[1] == self.pos[1]


class Bishop(Piece):
    def __init__(self, pos, team):
        self.name = 'Bishop'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        return abs(self.pos[0] - target_pos[0]) == abs(self.pos[1] - target_pos[1])


class Knight(Piece):
    def __init__(self, pos, team):
        self.name = 'Knight'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        return (target_pos[0] - self.pos[0]) ** 2 + (target_pos[1] - self.pos[1]) ** 2 == 25


class Pawn(Movable):
    def __init__(self, pos, team):
        self.name = 'Pawn'
        super().__init__(pos, team, f"../Resources/pieces/{team[0]}-{self.name.lower()}.png")

    def possible(self, target_pos):
        if target_pos[0] != self.pos[0]:
            return False

        if self.team == "white":
            if (self.pos[1] - target_pos[1] == 1) or (self.pos[1] == 6 and target_pos[1] == 4):
                return True

            if self.pos[1] - target_pos[1] == 1 and \
                    ((target_pos[0] - self.pos[0]) ** 2 + (target_pos[1] - self.pos[1]) ** 2) ** 0.5 == 2 ** 0.5 \
                    and (b.board[target_pos[1]][target_pos[0]] and b.board[target_pos[1]][target_pos[0]].team == "black"):
                return True

            return False

        if (target_pos[1] - self.pos[1] == 1) or (self.pos[1] == 1 and target_pos[1] == 3):
            return True
        return False


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.pieces = Board.create_pieces()
        self.selected_piece = None
        for piece in self.pieces:
            self.board[piece.pos[1]][piece.pos[0]] = piece

    def __str__(self) -> str:

        return "\n".join([", ".join(y) for y in [[str(piece) for piece in self.board[row]] for row in range(8)]])

    def draw(self, display, light_square_color, dark_square_color, t_resx, t_resy):
        for y, rows in enumerate(self.board):
            for x, piece in enumerate(rows):

                square_color = list(light_square_color if y % 2 == x % 2 else dark_square_color)
                text_color = list(dark_square_color if y % 2 == x % 2 else light_square_color)

                pygame.draw.rect(display, square_color, [x * t_resx, y * t_resy, t_resx, t_resy])
                msg = font.render(chr(97 + x) + str(8 - y), True, text_color)

                display.blit(msg, (
                    x * t_resx + transform_resolution[0] // 10, y * t_resy + transform_resolution[1] // 10 * 8))

                if self.selected_piece:
                    if self.selected_piece.possible([x, y]):
                        alpha = 0.4
                        surface = pygame.Surface((t_resx, t_resy))
                        surface.set_alpha(255 * alpha)
                        surface.fill(color_select_blue)
                        display.blit(surface, (x * t_resx, y * t_resy))

                # pygame.draw.rect(display, (color_cyan), [x * t_resx, y * t_resy, t_resx, t_resy], 1)

                if piece:
                    piece.draw(display)



    @classmethod
    def create_pieces(cls):
        return [
            King([4, 0], "black"), King([4, 7], "white"),
            Queen([3, 0], "black"), Queen([3, 7], "white"),
            Rook([0, 0], "black"), Rook([7, 0], "black"),
            Rook([0, 7], "white"), Rook([7, 7], "white"),
            Bishop([2, 0], "black"), Bishop([5, 0], "black"),
            Bishop([2, 7], "white"), Bishop([5, 7], "white"),
            Knight([1, 0], "black"), Knight([6, 0], "black"),
            Knight([1, 7], "white"), Knight([6, 7], "white"),
            *[Pawn([x, 1], "black") for x in range(8)],
            *[Pawn([x, 6], "white") for x in range(8)],
            Pawn([4, 3], "black"), Pawn([3, 4], "white")
        ]
    # rnbqkbkrpppppppp000000000000000000000000000000000000000000000000pppppppppprnbqkbkr

    def select_by_pos(self, pos):
        self.selected_piece = self.board[pos[1]][pos[0]]


b = Board()
print(str(b))
cursor_on = [-1, -1]

while run:



    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            minimum = min(event.w, event.h)
            display = pygame.display.set_mode((minimum, minimum), pygame.RESIZABLE)
            WINDOW_RESOLUTION = (minimum, minimum)
            transform_resolution = (
                WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
            font = pygame.font.SysFont(None, WINDOW_RESOLUTION[0] // 32)

    mouse_pos = list(map(lambda x: int(x // transform_resolution[0]), pygame.mouse.get_pos()))
    if cursor_on != mouse_pos:
        cursor_on = mouse_pos
        b.select_by_pos(cursor_on)

    # Keypresses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            pass

    display.fill(color_black)

    # draw_board(color_cream, color_walnut, *transform_resolution)
    b.draw(display, color_cream, color_walnut, *transform_resolution)

    pygame.display.update()
