import pygame
import time
import math
from abc import ABC, abstractmethod

# Misc variables

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
color_killer_red = (186, 18, 31)


# Functions
def show_fps(surface, font, dt, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = font.render(f"FPS: {int(1 / dt)}", True, text_color)
    fps_outline = font.render(f"FPS: {int(1 / dt)}", True, outline_color)
    surface.blit(fps_outline, (-1, -1))
    surface.blit(fps_outline, (-1, 1))
    surface.blit(fps_outline, (1, -1))
    surface.blit(fps_outline, (1, 1))
    surface.blit(fps_text, (0, 0))


def rainbow(angle):
    r = (math.sin(angle) + 1) / 2
    g = (math.sin(angle + math.pi / 1.5) + 1) / 2
    b = (math.sin(angle + 2 * math.pi / 1.5) + 1) / 2
    return [255 * r, 255 * g, 255 * b]


def distance(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))]) ** 0.5


def distance_squared(point: [int], point2: [int]) -> float:
    return sum([(point2[i] - point[i]) ** 2 for i in range(len(point))])


class Piece(ABC):
    def __init__(self, team: str, type: str, letter: str, symbol: str, value: float, image):
        self.team = team
        self.type = type
        self.letter = letter
        self.symbol = symbol
        self.value = value
        self.image = image

    def __str__(self):
        return f"{self.team} {self.type}"

    def __repr__(self):
        return str(self.__dict__)

    @abstractmethod
    def can_move(self, piece_pos, target_pos):
        pass


class King(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♚'
            letter = 'K'
        else:
            symbol = '♔'
            letter = 'k'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-king.png")
        super().__init__(team, "king", letter, symbol, 1_000_000, image)

    def can_move(self, piece_pos, target_pos):
        return abs(piece_pos[0] - target_pos[0]) <= 1 and abs(piece_pos[1] - target_pos[1]) <= 1


class Queen(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♛'
            letter = 'Q'
        else:
            symbol = '♕'
            letter = 'q'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-queen.png")
        super().__init__(team, "queen", letter, symbol, 9, image)

    def can_move(self, piece_pos, target_pos):
        return target_pos[0] == piece_pos[0] \
               or target_pos[1] == piece_pos[1] \
               or abs(piece_pos[0] - target_pos[0]) == abs(piece_pos[1] - target_pos[1])


class Rook(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♜'
            letter = 'R'
        else:
            symbol = '♖'
            letter = 'r'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-rook.png")
        super().__init__(team, "rook", letter, symbol, 5, image)

    def can_move(self, piece_pos, target_pos):
        return target_pos[0] == piece_pos[0] or target_pos[1] == piece_pos[1]


class Bishop(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♝'
            letter = 'B'
        else:
            symbol = '♗'
            letter = 'b'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-bishop.png")
        super().__init__(team, "bishop", letter, symbol, 3.25, image)

    def can_move(self, piece_pos, target_pos):
        return abs(piece_pos[0] - target_pos[0]) == abs(piece_pos[1] - target_pos[1])


class Knight(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♞'
            letter = 'N'
        else:
            symbol = '♘'
            letter = 'n'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-knight.png")
        super().__init__(team, "knight", letter, symbol, 3, image)

    def can_move(self, piece_pos, target_pos):
        return (target_pos[0] - piece_pos[0]) ** 2 + (target_pos[1] - piece_pos[1]) ** 2 == 5


class Pawn(Piece):
    def __init__(self, team: str):
        if team == "white":
            symbol = '♟'
            letter = 'P'
        else:
            symbol = '♙'
            letter = 'p'
        image = pygame.image.load(f"../Resources/pieces/{team[0]}-pawn.png")
        super().__init__(team, "pawn", letter, symbol, 1, image)

    def can_move(self, piece_pos, target_pos):
        if self.team == "white":
            if piece_pos[0] == target_pos[0]:
                if piece_pos[1] == 6 and 0 < piece_pos[1] - target_pos[1] < 3:
                        return True

                if piece_pos[1] - target_pos[1] == 1:
                    return True
                return False

        if piece_pos[0] == target_pos[0]:
            if piece_pos[1] == 1 and 0 < target_pos[1] - piece_pos[1] < 3:
                return True

            if target_pos[1] - piece_pos[1] == 1:
                return True
            return False

        return False


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        turn = 0

    def __str__(self):
        result = "-" * (8 * 4 + 1) + '\n'
        for y in range(8):
            temp = "|"
            for x in range(8):
                square = self.board[y][x]
                to_string = " " if y % 2 != x % 2 else '▒'
                if square:
                    to_string = square.symbol
                temp += f" {to_string} |"
            result += temp + '\n' + "-" * (8 * 4 + 1) + '\n'
        return result

    def __repr__(self):
        result = ""
        for row in self.board:
            result += str(row) + '\n'
        return result

    def generate_board_code(self):
        result = ""
        for row in range(8):
            for col in range(8):
                square = self.board[row][col]
                if square:
                    result += square.letter
                    continue
                result += '0'
            if row < 7:
                result += '/'
        return result

    def set_board_from_code(self, board_code: str):
        letter_to_piece = {'K': ["King", "white"],
                           'Q': ["Queen", "white"],
                           'R': ["Rook", "white"],
                           'B': ["Bishop", "white"],
                           'N': ["Knight", "white"],
                           'P': ["Pawn", "white"],
                           'k': ["King", "black"],
                           'q': ["Queen", "black"],
                           'r': ["Rook", "black"],
                           'b': ["Bishop", "black"],
                           'n': ["Knight", "black"],
                           'p': ["Pawn", "black"]}
        x = 0
        y = 0

        for char in board_code:
            if char == '/':
                x = 0
                y += 1
                continue

            if char == '0':
                self.board[y][x] = None
            else:
                to_create = letter_to_piece[char]
                self.board[y][x] = eval(f"{to_create[0]}('{to_create[1]}')")
            x += 1

    def get_piece(self, pos: [int, int]):
        return self.board[pos[1]][pos[0]]

    def set_piece(self, pos: [int, int], piece: Piece):
        self.board[pos[1]][pos[0]] = piece

    def is_clear_path(self, pos_from, pos_to):
        dx = pos_to[0] - pos_from[0]
        dir_x = 0 if not dx else dx // abs(dx)
        dy = pos_to[1] - pos_from[1]
        dir_y = 0 if not dy else dy // abs(dy)

        for i in range(1, max(abs(dx), abs(dy))):
            x, y = pos_from[0] + dir_x * i, pos_from[1] + dir_y * i
            if self.board[y][x]:
                return False
        return True

    def try_move(self, pos_from, pos_to):
        if pos_from == pos_to:
            return False

        piece_from = self.get_piece(pos_from)

        if not piece_from:
            return False

        piece_to = self.get_piece(pos_to)

        if piece_to and piece_from.team == piece_to.team:
            return False

        if piece_from.type == "knight":
            return piece_from.can_move(pos_from, pos_to)

        if not (pos_from[0] == pos_to[0] or pos_from[1] == pos_to[1] or abs(pos_to[0] - pos_from[0]) == abs(pos_to[1] - pos_from[1])):
            return False

        return self.is_clear_path(pos_from, pos_to) and piece_from.can_move(pos_from, pos_to)

if __name__ == "__main__":
    print(__file__.split("\\")[-1])
    b = Board()
    b.set_piece([0, 6], Pawn("white"))
    b.set_piece([3, 0], King("black"))
    print(b.generate_board_code())
    b.set_board_from_code("rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQK0NR")
    b.set_board_from_code("rnbqkbnr/00000000/000N0N00/000b0000/00NNr000/00000000/00000000/RNBQKBNR")
    b.set_board_from_code("rnbqkbnr/00000000/000N0N00/000b0000/00NNr000/00000000/000Q0000/RNB0KBNR")
    print(b.get_piece([1, 0]))
    print(repr(b.get_piece([1, 0])))
    print(b.try_move([1, 0], [0, 2]))
    print(b.try_move([0, 0], [0, 2]))
    print(b.try_move([3, 2], [4, 3]))
    print(b.try_move([4, 7], [5, 0]))
    print(Queen("king").can_move([4, 7], [5, 0]))
    print(b.is_clear_path([4, 7], [5, 0]))

    print(b)
    print(b.generate_board_code())

