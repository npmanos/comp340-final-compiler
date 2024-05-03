from abc import ABC, abstractmethod
from typing import Literal, TypeAlias

__all__ = [
    "Precedence",
    "NumberType",
    "TokenBase",
    "PrefixOperator",
    "InfixOperator",
    "LeftParen",
    "RightParen",
    "Mult",
    "Div",
    "Plus",
    "Minus",
    "Number",
]

Precedence: TypeAlias = Literal[0, 1, 2, 3]
NumberType: TypeAlias = int | float


class TokenBase(ABC):
    value: str
    precedence: Precedence

    def __eq__(self, value: object) -> bool:
        return isinstance(value, TokenBase) and self.value == value.value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={repr(self.value)})"


class PrefixOperator(TokenBase):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return hasattr(subclass, "eval_prefix") and callable(subclass.eval_prefix)

    @abstractmethod
    def eval_prefix(self, operand: NumberType) -> NumberType:
        raise NotImplementedError


class InfixOperator(TokenBase):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return hasattr(subclass, "eval_infix") and callable(subclass.eval_infix)

    @abstractmethod
    def eval_infix(
        self, left_operand: NumberType, right_operand: NumberType
    ) -> NumberType:
        raise NotImplementedError


class LeftParen(TokenBase):
    def __init__(self) -> None:
        self.value = "("
        self.precedence = 3


class RightParen(TokenBase):
    def __init__(self) -> None:
        self.value = ")"
        self.precedence = 3


class Mult(InfixOperator):
    def __init__(self) -> None:
        self.value = "*"
        self.precedence = 2

    def eval_infix(
        self, left_operand: NumberType, right_operand: NumberType
    ) -> NumberType:
        return left_operand * right_operand


class Div(InfixOperator):
    def __init__(self) -> None:
        self.value = "/"
        self.precedence = 2

    def eval_infix(
        self, left_operand: NumberType, right_operand: NumberType
    ) -> NumberType:
        return left_operand / right_operand


class Plus(InfixOperator):
    def __init__(self) -> None:
        self.value = "+"
        self.precedence = 1

    def eval_infix(
        self, left_operand: NumberType, right_operand: NumberType
    ) -> NumberType:
        return left_operand + right_operand


class Minus(PrefixOperator, InfixOperator):
    def __init__(self) -> None:
        self.value = "-"
        self.precedence = 1

    def eval_prefix(self, operand: NumberType) -> NumberType:
        return -operand

    def eval_infix(
        self, left_operand: NumberType, right_operand: NumberType
    ) -> NumberType:
        return left_operand - right_operand


class Number(TokenBase):
    def __init__(self, value: str) -> None:
        self.value = value
        self.precedence = 0

    def __float__(self) -> float:
        return float(self.value)

    def __int__(self) -> int:
        return int(self.value)
