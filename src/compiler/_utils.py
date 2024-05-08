from abc import abstractmethod
from collections.abc import Callable, Collection
from typing import NamedTuple, Protocol, SupportsIndex, TypeAlias, TypeVar


__all__ = ["T", "Predicate", "SupportsLPop", "SyntaxErrorDetails"]

T = TypeVar("T", covariant=True)

Predicate: TypeAlias = Callable[[T], bool]


class SupportsLPop(Collection[T], Protocol[T]):
    @abstractmethod
    def __getitem__(self, key: SupportsIndex, /) -> T:
        raise NotImplementedError

    @abstractmethod
    def popleft(self) -> T:
        raise NotImplementedError


class SyntaxErrorDetails(NamedTuple):
    """
    Details tuple for :py:exception::`SyntaxError`.

    For errors in f-string fields, the message is prefixed by "f-string: " and
    the offsets are offsets in a text constructed from the replacement
    expression. For example, compiling f'Bad {a b} field' results in this args
    attribute:

    ```
    (
        'f-string: ...',
        SyntaxErrorDetails(
            filename='',
            lineno=1, offset=2,
            text='(a b)n',
            end_lineno=1,
            end_offset=5
        )
    )
    ```

    See `SyntaxError`_

    .. _SyntaxError: https://docs.python.org/3/library/exceptions.html#SyntaxError
    """

    filename: str | None = None
    """The name of the file the syntax error ocurred in."""

    lineno: int | None = None
    """
    Which line number in the file the error occurred in. This is 1-indexed: the
    first line in the file has a `lineno` of 1.
    """

    offset: int | None = None
    """
    The column in the line where the error occurred. This is 1-indexed: the
    first character in the line has an `offset` of 1.
    """

    text: str | None = None
    """The source code involved in the error."""

    end_lineno: int | None = None
    """
    Which line number in the file the error occurred in. This is 1-indexed: the
    first line in the file has a `lineno` of 1.
    """

    end_offset: int | None = None
    """
    The column in the end line where the error occurred finishes. This is
    1-indexed: the first character in the line has an `offset` of 1.
    """
