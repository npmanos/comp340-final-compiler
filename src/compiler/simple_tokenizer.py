from .simple_tokens import (
    Div,
    LeftParen,
    Minus,
    Mult,
    Number,
    Plus,
    RightParen,
    TokenBase,
)


class TokenizeError(SyntaxError):
    pass


def tokenize(srcCode: str) -> list[TokenBase]:
    tokenize_list: list[TokenBase] = []  # Initialize empty list

    for idx, c in enumerate(srcCode, 1):
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
                raise TokenizeError(f"Unknown token {c}", (None, None, idx, srcCode, None, idx))

    return tokenize_list
