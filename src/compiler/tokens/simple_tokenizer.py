# from typing import Literal, NamedTuple

from compiler.tokens.simple_tokens import (
    Precedence,
    TokenBase,
    Operator,
    PrefixOperator,
    InfixOperator,
    LeftParen,
    RightParen,
    Mult,
    Div,
    Plus,
    Minus,
    Number,
)

# type TokenType = Literal['NUMB', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN']

# class Token(NamedTuple):
#     value: str
#     type: TokenType

#     @property
#     def precedence(self) -> int:
#         match self.type:
#             case 'LPAREN' | 'RPAREN':
#                 return 3
#             case 'MULT' | 'DIV':
#                 return 2
#             case 'PLUS' | 'MINUS':
#                 return 1
#             case _:
#                 return -1

#     # def __repr__(self):
#         # return f'{self.value}\t{self.type}'
#         # return f"Token({self.value}, '{self.type}')"

#     def __str__(self) -> str:
#         return self.value


class TokenizeError(Exception):
    pass


def tokenize(srcCode: str) -> list[TokenBase]:
    tokenize_list: list[TokenBase] = []  # Initialize empty list

    for c in srcCode:
        match c:
            case c if c.isdigit():
                if len(tokenize_list) > 0 and isinstance(tokenize_list[-1], Number):
                    tokenize_list[-1].value += c
                else:
                    tokenize_list.append(Number(c))
            case "+":
                tokenize_list.append(Plus())
            case "-":
                tokenize_list.append(Minus())
            case "*":
                tokenize_list.append(Mult())
            case "/":
                tokenize_list.append(Div())
            case "(":
                tokenize_list.append(LeftParen())
            case ")":
                tokenize_list.append(RightParen())
            case c if c.isspace():
                continue
            case _:
                # If c doesn't match any of these cases, raise an error
                raise TokenizeError(f"Unknown token {c} in {srcCode}")

    return tokenize_list


if __name__ == "__main__":
    __package__ = __package__ or "compiler"

    test_src = "(5 + 2) * (60 / 15) - 10"

    tokens = tokenize(test_src)

    print(test_src)

    for token in tokens:
        print(repr(token))
