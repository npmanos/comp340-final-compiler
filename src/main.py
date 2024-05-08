# ruff: noqa: F403, F405

import importlib.util
import os
import sys
from traceback import format_exception, format_exception_only
from typing import NoReturn

from compiler import *
from compiler.simple_baby import BabySyntaxError
from compiler.simple_evaluator import EvaluationError
from compiler.simple_tokenizer import TokenizeError
from compiler.simple_tokens import NumberType


BABY_MODE_ENABLED = True

if BABY_MODE_ENABLED:
    greeting_str = "Hello baby language.\nEnter baby exp and see what you get.\n"
    exit_command = "poopoo"
    goodbye_str = "Now it is time to go poo poo."
    _bottom_text_left = "enther baby wanguage"
    _bottom_text_right = "comp 340 baby woop"

    _pt_avail = importlib.util.find_spec("prompt_toolkit") is not None
    _transl_fmt_open = "<ansiblue><i>" if _pt_avail else ""
    _transl_fmt_close = "</i></ansiblue>" if _pt_avail else ""

    def process_input(user_input: str) -> NumberType:
        math_src = decipher(user_input)
        print(f" {_transl_fmt_open}Evaluating as {math_src}{_transl_fmt_close}")
        return evaluate(parse(tokenize(math_src)))
else:
    greeting_str = ""
    exit_command = "exit"
    goodbye_str = "Now it is time to exit."
    _bottom_text_left = "Enter math expression to evaluate"
    _bottom_text_right = "COMP 340 Math REPL"

    def process_input(user_input: str) -> NumberType:
        return evaluate(parse(tokenize(user_input)))


try:
    from prompt_toolkit import HTML, PromptSession, print_formatted_text
    from prompt_toolkit.formatted_text import PygmentsTokens
    from prompt_toolkit.lexers import PygmentsLexer
    from pygments import lex
    from pygments.lexers.python import PythonConsoleLexer

    _width, _ = os.get_terminal_size()

    _bottom_text_right = f"{_bottom_text_right:>{_width - len(_bottom_text_left)}}"

    _bottom_text = HTML(f"<b>{_bottom_text_left}{_bottom_text_right}</b>")

    _session = PromptSession(
        lexer=PygmentsLexer(PythonConsoleLexer),
        bottom_toolbar=_bottom_text,
    )
    input = _session.prompt

    _lexer = PythonConsoleLexer()

    def print(*values: object, sep: str | None = " ", end: str | None = "\n"):
        if sep is None:
            sep = ""

        if end is None:
            end = ""

        src_code = sep.join(map(str, values))

        print_formatted_text(HTML(src_code), end=end)

    def print_ans(*values: object, sep: str | None = "", end: str | None = ""):
        print("<ansibrightgreen>", *values, "</ansibrightgreen>", sep, end)

    def print_exc(*values: object, sep: str | None = " ", end: str | None = ""):
        if sep is None:
            sep = ""

        if end is None:
            end = ""

        src_code = sep.join(map(str, values))

        tokens = list(lex(src_code, _lexer))
        print_formatted_text(PygmentsTokens(tokens), end=end)
except ImportError:
    print_ans = print_exc = print

__all__ = []

PROMPT = ">>> "


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def repl() -> NoReturn:
    clear()
    print(greeting_str, end="")
    while True:
        try:
            user_input: str = input(PROMPT).lower()

            if not user_input or user_input.isspace():
                continue

            if user_input == exit_command:
                raise EOFError
        except KeyboardInterrupt:
            continue
        except EOFError:
            print(goodbye_str)
            sys.exit(0)
        else:
            try:
                print_ans(process_input(user_input))
            except (BabySyntaxError, TokenizeError, EvaluationError) as e:
                e.filename = "<stdin>"
                e.lineno = 1
                e.offset = e.offset or 1
                e.text = e.text or user_input
                e.end_lineno = 1
                e.end_offset = e.end_offset or len(user_input) + 1

                print_exc(*format_exception_only(e), sep="", end="")
            except Exception as e:
                print_exc(*format_exception(e), sep="", end="")


if __name__ == "__main__":
    repl()
