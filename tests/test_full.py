from ._test_constants import BABY_TEST_MAP
from compiler.simple_evaluator import evaluate
from compiler.simple_parser import parse
from compiler.simple_tokenizer import tokenize
from compiler.simple_baby import decipher
from pytest import mark

py_eval = eval


@mark.parametrize(
    "src_str",
    [
        "1 * (2 + 5)",
        "(1 + 2) * 5 + 4",
        "23 * ((1 + 5) * 33)",
        "5 - 13 / 21 + 21 * 6",
        "24",
        "125",
        "-5",
        "--5",
        "- 5 + 6 * 19",
    ],
)
def test_tokenize_parse_evaluate(src_str: str):
    assert py_eval(src_str) == evaluate(parse(tokenize(src_str)))

@mark.parametrize("baby_expr,src_str", BABY_TEST_MAP.items())
def test_decipher_tokenize_parse_evaluate(baby_expr: str, src_str: str):
    assert py_eval(src_str) == evaluate(parse(tokenize(decipher(baby_expr))))
