from __future__ import annotations
from abc import ABC
from typing import Callable


class ASTNode(ABC):
    def traverse(self, on_enter: Callable[[ASTNode], None], on_exit: Callable[[ASTNode], None]) -> None:
        on_enter(self)

        match self:
            case ASTNodeProgram(expressions):
                for expression in expressions:
                    expression.traverse(on_enter, on_exit)
            case ASTNodeRepeat(_, expressions):
                for expression in expressions:
                    expression.traverse(on_enter, on_exit)

        on_exit(self)


class ASTNodeExpression(ASTNode):
    def __init__(self):
        super().__init__()


class ASTNodeProgram(ASTNode):
    __match_args__ = ("expressions",)

    def __init__(self, expressions: list[ASTNodeExpression]) -> None:
        super().__init__()
        self.expressions = expressions


class ASTNodeMove(ASTNodeExpression):
    __match_args__ = ("distance",)

    def __init__(self, distance: int) -> None:
        super().__init__()
        self.distance = distance


class ASTNodeRotate(ASTNodeExpression):
    __match_args__ = ("angle_degrees",)

    def __init__(self, angle_degrees: int) -> None:
        super().__init__()
        self.angle_degrees = angle_degrees


class ASTNodePen(ASTNodeExpression):
    __match_args__ = ("active",)

    def __init__(self, active: bool) -> None:
        super().__init__()
        self.active = active


class ASTNodeColor(ASTNodeExpression):
    __match_args__ = ("color",)

    def __init__(self, color: str) -> None:
        super().__init__()
        self.color = color


class ASTNodeRepeat(ASTNodeExpression):
    __match_args__ = ("repetitions", "expressions")

    def __init__(self, repetitions: int, expressions: list[ASTNodeExpression]) -> None:
        super().__init__()
        self.repetitions = repetitions
        self.expressions = expressions
