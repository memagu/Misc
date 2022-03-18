import pygame
import time
import math

# Misc variables

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)


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


class Piece:
    def __init__(self, team: str, type: str, letter: str, symbol: str, value: float,):
        self.team = team
        self.type = type
        self.letter = letter
        self.symbol = symbol
        self.value = value

    def __str__(self):
        return f"{self.team} {self.type}"

    def __repr__(self):
        return self.__dict__


class King(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♚'
            letter = 'K'
        else:
            symbol = '♔'
            letter = 'k'
        super().__init__(team, "king", letter, symbol, 1_000_000)


class Queen(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♛'
            letter = 'Q'
        else:
            symbol = '♕'
            letter = 'q'
        super().__init__(team, "queen", letter, symbol, 9)


class Rook(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♜'
            letter = 'R'
        else:
            symbol = '♖'
            letter = 'r'
        super().__init__(team, "rook", letter, symbol, 5)


class Bishop(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♝'
            letter = 'B'
        else:
            symbol = '♗'
            letter = 'b'
        super().__init__(team, "bishop", letter, symbol, 3.25)


class Knight(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♞'
            letter = 'N'
        else:
            symbol = '♘'
            letter = 'n'
        super().__init__(team, "knight", letter, symbol, 3)


class Pawn(Piece):
    def __init__(self, team):
        if team == "white":
            symbol = '♟'
            letter = 'P'
        else:
            symbol = '♙'
            letter = 'p'
        super().__init__(team, "pawn", letter, symbol, 1)


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
            if char != '0':
                to_create = letter_to_piece[char]
                self.board[y][x] = eval(f"{to_create[0]}('{to_create[1]}')")
            x += 1

    def get_piece(self, pos: [int, int]):
        return self.board[pos[1]][pos[0]]

    def set_piece(self, pos: [int, int], piece: Piece):
        self.board[pos[1]][pos[0]] = piece



if __name__ == "__main__":
    print(__file__.split("\\")[-1])
    b = Board()
    b.set_piece([0, 6], Pawn("white"))
    b.set_piece([3, 0], King("black"))
    print(b.generate_board_code())
    b.set_board_from_code("rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR")
    print(b)

