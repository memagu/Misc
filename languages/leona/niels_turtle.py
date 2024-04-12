from pathlib import Path

from leona.leona import Program
from leona.util import ASTPrettyPrint

from leona.lexer import Lexer
from leona.parser import Parser


def main() -> None:
    # program_path = Path(input("Program path: "))
    program_path = Path("./square.turtle")

    with open(program_path, "r") as f:
        program = f.read()

    # # ASTPrettyPrint(program).show()
    # # Program(program).run()
    # print(repr(program))
    # tokens = Lexer(program).tokenize()
    # #print(*(token for token in tokens), sep='\n')
    # ast = Parser(tokens).parse()

    ASTPrettyPrint(program).show()



if __name__ == '__main__':
    main()
