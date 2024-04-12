from typing import Sequence

from .lexer import Token, TokenType
from .ast import ASTNodeProgram, ASTNodeExpression, ASTNodeMove, ASTNodeRotate, ASTNodePen, ASTNodeColor, ASTNodeRepeat


class Parser:
    def __init__(self, tokens: Sequence[Token]) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def match(self, token_type: TokenType) -> Token:
        token = self.peek()
        if token.type != token_type:
            print(f"Syntaxfel på rad {self.peek().line_number + 1}")
            exit()
        self.pos += 1

        return token

    def expression(self) -> ASTNodeExpression:
        token = self.peek()

        match token.type:
            case TokenType.FORW:
                self.match(TokenType.FORW)
                distance = self.match(TokenType.DECIMAL).value
                self.match(TokenType.PERIOD)
                return ASTNodeMove(int(distance))
            case TokenType.BACK:
                self.match(TokenType.BACK)
                distance = self.match(TokenType.DECIMAL).value
                self.match(TokenType.PERIOD)
                return ASTNodeMove(-int(distance))
            case TokenType.LEFT:
                self.match(TokenType.LEFT)
                angle_degrees = self.match(TokenType.DECIMAL).value
                self.match(TokenType.PERIOD)
                return ASTNodeRotate(int(angle_degrees))
            case TokenType.RIGHT:
                self.match(TokenType.RIGHT)
                angle_degrees = self.match(TokenType.DECIMAL).value
                self.match(TokenType.PERIOD)
                return ASTNodeRotate(-int(angle_degrees))
            case TokenType.DOWN:
                self.match(TokenType.DOWN)
                self.match(TokenType.PERIOD)
                return ASTNodePen(True)
            case TokenType.UP:
                self.match(TokenType.UP)
                self.match(TokenType.PERIOD)
                return ASTNodePen(False)
            case TokenType.COLOR:
                self.match(TokenType.COLOR)
                color = self.match(TokenType.HEX).value
                self.match(TokenType.PERIOD)
                return ASTNodeColor(color)
            case TokenType.REP:
                self.match(TokenType.REP)
                repetitions = self.match(TokenType.DECIMAL).value
                if self.peek().type == TokenType.QUOTE:
                    self.match(TokenType.QUOTE)
                    expressions = self.expressions()
                    self.match(TokenType.QUOTE)
                else:
                    expressions = [self.expression()]

                return ASTNodeRepeat(int(repetitions), expressions)

    def expressions(self) -> list[ASTNodeExpression]:
        expression = self.expression()
        if self.peek().type in {TokenType.FORW, TokenType.BACK, TokenType.LEFT, TokenType.RIGHT, TokenType.DOWN,
                                TokenType.UP, TokenType.COLOR, TokenType.REP}:
            return [expression] + self.expressions()
        return [expression]

    def program(self) -> ASTNodeProgram:
        expressions = self.expressions()
        self.match(TokenType.EOF)
        return ASTNodeProgram(expressions)

    def parse(self) -> ASTNodeProgram:
        return self.program()
