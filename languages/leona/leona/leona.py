from math import cos, sin, radians

from .ast import *
from .lexer import Lexer
from .parser import Parser


class Program:
    def __init__(self, program: str) -> None:
        self.program = program
        self.pos = (0, 0)
        self.angle = 0
        self.color = "#0000ff"
        self.pen_active = False

    def on_enter(self, node: ASTNode) -> None:
        match node:
            case ASTNodeMove(distance):
                old_pos = self.pos
                self.pos = (
                    self.pos[0] + distance * cos(radians(self.angle)),
                    self.pos[1] + distance * sin(radians(self.angle))
                )
                if self.pen_active:
                    print(f"#{self.color.upper()} {old_pos[0]:.4f} {old_pos[1]:.4f} {self.pos[0]:.4f} {self.pos[1]:.4f}")
            case ASTNodeRotate(angle_degrees):
                self.angle += angle_degrees
            case ASTNodePen(active):
                self.pen_active = active
            case ASTNodeColor(color):
                self.color = color
            case ASTNodeRepeat(repeats, expressions):
                for expression in expressions * (repeats - 1):
                    self.on_enter(expression)

    def run(self) -> None:
        tokens = Lexer(self.program).tokenize()
        ast = Parser(tokens).parse()
        ast.traverse(self.on_enter, lambda _: None)
