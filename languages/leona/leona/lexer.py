from dataclasses import dataclass
from enum import Enum
import string
from typing import Optional


class TokenType(Enum):
    EOF = 0
    ERROR = 1

    FORW = 2
    BACK = 3
    LEFT = 4
    RIGHT = 5
    DOWN = 6
    UP = 7
    COLOR = 8
    REP = 9

    DECIMAL = 10
    HEX = 11

    PERIOD = 12
    QUOTE = 13


@dataclass
class Token:
    type: TokenType
    value: Optional[str] = None
    line_number: Optional[int] = None


class Lexer:
    def __init__(self, program: str) -> None:
        self.program = program.lower()
        self.tokens = []
        self.pos = self.line_number = 0

    def add_token(self, token_type: TokenType, value: Optional[str] = None) -> None:
        self.tokens.append(Token(token_type, value, self.line_number))

    def skip_whitespace(self) -> None:
        while self.pos < len(self.program) and (char := self.program[self.pos]) in string.whitespace:
            self.line_number += char == '\n'
            self.pos += 1

    def skip_until_newline(self) -> None:
        while self.pos < len(self.program) and self.program[self.pos] != '\n':
            self.pos += 1

    def is_valid_multichar(self) -> bool:
        return self.program[self.pos] in string.whitespace + '.'

    def consume_alpha(self) -> str:
        lexeme = []
        while self.pos < len(self.program) and (char := self.program[self.pos]).isalpha():
            lexeme.append(char)
            self.pos += 1
        return ''.join(lexeme)

    def consume_numeric(self) -> str:
        lexeme = []
        while self.pos < len(self.program) and (char := self.program[self.pos]).isnumeric():
            lexeme.append(char)
            self.pos += 1
        return ''.join(lexeme)

    def consume_hex(self) -> str:
        lexeme = []
        while self.pos < len(self.program) and (char := self.program[self.pos]) in string.hexdigits:
            lexeme.append(char)
            self.pos += 1
        return ''.join(lexeme)

    def consume_char(self) -> str:
        lexeme = self.program[self.pos]
        self.pos += 1
        return lexeme

    def tokenize(self) -> list[Token]:
        while True:
            self.skip_whitespace()

            if self.pos >= len(self.program):
                self.add_token(TokenType.EOF)
                return self.tokens

            char = self.program[self.pos]

            if char.isalpha():
                lexeme = self.consume_alpha()

                if not self.is_valid_multichar():
                    self.add_token(TokenType.ERROR)
                    return self.tokens

                match lexeme:
                    case "forw":
                        self.add_token(TokenType.FORW)
                    case "back":
                        self.add_token(TokenType.BACK)
                    case "left":
                        self.add_token(TokenType.LEFT)
                    case "right":
                        self.add_token(TokenType.RIGHT)
                    case "down":
                        self.add_token(TokenType.DOWN)
                    case "up":
                        self.add_token(TokenType.UP)
                    case "color":
                        self.add_token(TokenType.COLOR)
                    case "rep":
                        self.add_token(TokenType.REP)
                    case _:
                        self.add_token(TokenType.ERROR)
                        return self.tokens
                continue

            if char.isnumeric():
                lexeme = self.consume_numeric()

                if not self.is_valid_multichar():
                    self.add_token(TokenType.ERROR)
                    return self.tokens

                if int(lexeme):
                    self.add_token(TokenType.DECIMAL, lexeme)
                else:
                    self.add_token(TokenType.ERROR)
                continue

            match self.consume_char():
                case '#':
                    lexeme = self.consume_hex()

                    if not self.is_valid_multichar() or len(lexeme) != 6:
                        self.add_token(TokenType.ERROR)
                        return self.tokens

                    self.add_token(TokenType.HEX, lexeme)
                case '%':
                    self.skip_until_newline()
                case '"':
                    self.add_token(TokenType.QUOTE)
                case '.':
                    self.add_token(TokenType.PERIOD)
                case _:
                    self.add_token(TokenType.ERROR)
                    return self.tokens
