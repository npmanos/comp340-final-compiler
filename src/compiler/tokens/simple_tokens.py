from abc import ABC, abstractmethod
from typing import Literal, overload

__all__ = [
    'Precedence',
    'TokenBase',
    'Operator',
    'PrefixOperator',
    'InfixOperator',
    'LeftParen',
    'RightParen',
    'Mult',
    'Div',
    'Plus',
    'Minus',
    'Number'
]

type Precedence = Literal[0, 1, 2, 3]

class TokenBase(ABC):
    value: str
    precedence: Precedence

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, TokenBase) and
            self.value == value.value
        )

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(value={repr(self.value)})'


class Operator(TokenBase):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return (
            hasattr(subclass, 'evaluate') and
            callable(subclass.evaluate)
        )


class PrefixOperator(Operator):
    @abstractmethod
    def evaluate(self, operand: float) -> float:
        raise NotImplementedError


class InfixOperator(Operator):
    @abstractmethod
    def evaluate(self, left_operand: float, right_operand: float) -> float:
        raise NotImplementedError
        

class LeftParen(TokenBase):
    def __init__(self) -> None:
        self.value = '('
        self.precedence = 3


class RightParen(TokenBase):
    def __init__(self) -> None:
        self.value = ')'
        self.precedence = 3


class Mult(InfixOperator):
    def __init__(self) -> None:
        self.value = '*'
        self.precedence = 2
    
    def evaluate(self, left_operand: float, right_operand: float) -> float:
        return left_operand * right_operand


class Div(InfixOperator):
    def __init__(self) -> None:
        self.value = '/'
        self.precedence = 2
    
    def evaluate(self, left_operand: float, right_operand: float) -> float:
        return left_operand / right_operand


class Plus(InfixOperator):
    def __init__(self) -> None:
        self.value = '+'
        self.precedence = 1
    
    def evaluate(self, left_operand: float, right_operand: float) -> float:
        return left_operand + right_operand

class Minus(PrefixOperator, InfixOperator):
    def __init__(self) -> None:
        self.value = '-'
        self.precedence = 1
    
    @overload
    def evaluate(self, *, operand: float) -> float: ...
    @overload
    def evaluate(self, *, left_operand: float, right_operand: float) -> float: ...
    def evaluate(self, **kwargs: float) -> float:
        assert not (kwargs.keys() >= {'operand', 'left_operand', 'right_operand'})

        if 'operand' in kwargs:
            return -1 * kwargs['operand']
        elif kwargs.keys() >= {'left_operand', 'right_operand'}:
            return kwargs['left_operand'] - kwargs['right_operand']
        else:
            raise TypeError


class Number(TokenBase):
    def __init__(self, value: str) -> None:
        self.value = value
        self.precedence = 0
    
    def __int__(self) -> int:
        return int(self.value)
