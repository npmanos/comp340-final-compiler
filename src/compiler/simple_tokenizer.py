from typing import Literal, NamedTuple

type TokenType = Literal['NUMB', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN']

class Token(NamedTuple):
    value: str
    type: TokenType
    
    @property
    def precedence(self) -> int:
        match self.type:
            # case 'LPAREN' | 'RPAREN':
            #     return 1
            case 'MULT' | 'DIV':
                return 2
            case 'PLUS' | 'MINUS':
                return 1
            case _:
                return 10

    # def __repr__(self):
        # return f'{self.value}\t{self.type}'
        # return f"Token({self.value}, '{self.type}')"
    
    def __str__(self) -> str:
        return self.value

def tokenize(srcCode: str) -> list[Token]:
    tokenize_list: list[Token] = [] # Initialize empty list

    for c in srcCode: # Iterate through each character in srcCode
        match c:
            case c if c.isdigit():
                if len(tokenize_list) > 0 and tokenize_list[-1].type == 'NUMB':
                    tokenize_list[-1] = Token(tokenize_list[-1].value + c, 'NUMB')
                else:
                    tokenize_list.append(Token(c, 'NUMB'))
            case '+':
                tokenize_list.append(Token(c, 'PLUS'))
            case '-':
                tokenize_list.append(Token(c, 'MINUS'))
            case '*':
                tokenize_list.append(Token(c, 'MULT'))
            case '/':
                tokenize_list.append(Token(c, 'DIV'))
            case '(':
                tokenize_list.append(Token(c, 'LPAREN'))
            case ')':
                tokenize_list.append(Token(c, 'RPAREN'))
            case _:
                # If c doesn't match any of these cases, skip it
                continue

    return tokenize_list

if __name__ == '__main__':
    __package__ = __package__ or 'compiler'

    test_src = '(5 + 2) * (60 / 15) - 10'

    tokens = tokenize(test_src)

    print(test_src)

    for token in tokens:
        print(repr(token))