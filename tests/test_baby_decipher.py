from pytest import mark
from ._test_constants import BABY_TEST_MAP
from compiler.simple_baby import decipher


@mark.parametrize("baby_expr,expected_decipher", BABY_TEST_MAP.items())
def test_decipher(baby_expr: str, expected_decipher: str):
    assert expected_decipher == decipher(baby_expr)
