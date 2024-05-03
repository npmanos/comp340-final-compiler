# ruff: noqa: F403, F405

import os
import sys
from traceback import format_exception, format_exception_only
from typing import NoReturn

from compiler import *
from compiler.simple_evaluator import EvaluationError
from compiler.simple_tokenizer import TokenizeError

try:
    from prompt_toolkit import HTML, PromptSession, print_formatted_text
    from prompt_toolkit.formatted_text import PygmentsTokens
    from prompt_toolkit.lexers import PygmentsLexer
    from pygments import lex
    from pygments.lexers.python import PythonConsoleLexer

    _width, _ = os.get_terminal_size()

    _bottom_text_left = "Enter math expression to evaluate"
    _bottom_text_right = f'{"COMP 340 Math REPL":>{_width - len(_bottom_text_left)}}'

    _bottom_text = HTML(f"<b>{_bottom_text_left}{_bottom_text_right}</b>")

    _session = PromptSession(
        lexer=PygmentsLexer(PythonConsoleLexer),
        bottom_toolbar=_bottom_text,
    )  # style=_style)
    input = _session.prompt

    _lexer = PythonConsoleLexer()

    def print(*values: object, sep: str | None = " ", end: str | None = ""):
        if sep is None:
            sep = ""

        if end is None:
            end = ""

        src_code = sep.join(map(str, values))

        tokens = list(lex(src_code, _lexer))
        print_formatted_text(PygmentsTokens(tokens), end=end)
except ImportError:
    pass

__all__ = ()

PROMPT = ">>> "


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def repl() -> NoReturn:
    clear()
    while True:
        try:
            user_input: str = input(PROMPT)

            if user_input.lower() == "exit":
                raise EOFError
        except KeyboardInterrupt:
            continue
        except EOFError:
            print("Now it is time to exit.")
            sys.exit(0)
        else:
            try:
                print(evaluate(parse(tokenize(user_input))))
            except (TokenizeError, EvaluationError) as e:
                e.filename = "<stdin>"
                e.lineno = 1
                e.offset = e.offset or 1
                e.text = e.text or user_input
                e.end_lineno = 1
                e.end_offset = e.end_offset or len(user_input) + 1

                print(*format_exception_only(e), sep="", end="")
            except Exception as e:
                print(*format_exception(e), sep="", end="")


if __name__ == "__main__":
    repl()
