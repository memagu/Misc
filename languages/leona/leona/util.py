from .ast import *
from .lexer import Lexer
from .parser import Parser


class ASTPrettyPrint:
    def __init__(self, program: str) -> None:
        self.ast = Parser((Lexer(program).tokenize())).parse()
        self.depth_stack = [0]

    @property
    def indent(self) -> str:
        return ' ' * (4 * self.depth_stack[-1])

    def on_enter(self, node: ASTNode) -> None:
        match node:
            case ASTNodeProgram():
                print("--- Program Start ---")
            case ASTNodeMove(distance):
                print(f"{self.indent}{"FORW" if distance >= 0 else "BACK"} {distance}.")
            case ASTNodeRotate(angle_degrees):
                print(f"{self.indent}{"LEFT" if angle_degrees >= 0 else "RIGHT"} {angle_degrees}.")
            case ASTNodePen(active):
                print(f"{self.indent}{"DOWN" if active else "UP"}.")
            case ASTNodeColor(color):
                print(f"{self.indent}COLOR #{color.upper()}.")
            case ASTNodeRepeat(repetitions, expressions):
                if len(expressions) > 1:
                    print(f'{self.indent}REP {repetitions} "')
                    self.depth_stack.append(self.depth_stack[-1] + 1)
                else:
                    print(f'{self.indent}REP {repetitions} ', end='')
                    self.depth_stack.append(0)

    def on_exit(self, node: ASTNode) -> None:
        match node:
            case ASTNodeProgram():
                print("--- Program End ---")
            case ASTNodeRepeat(_, expressions):
                self.depth_stack.pop()
                if len(expressions) > 1:
                    print(f'{self.indent}"')

    def show(self) -> None:
        self.ast.traverse(self.on_enter, self.on_exit)
