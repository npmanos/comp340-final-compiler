from abc import abstractmethod
from collections.abc import Callable, Collection
from typing import Protocol, SupportsIndex, TypeAlias, TypeVar


__all__ = ["T", "Predicate", "SupportsLPop"]

T = TypeVar("T", covariant=True)

Predicate: TypeAlias = Callable[[T], bool]


class SupportsLPop(Collection[T], Protocol[T]):
    @abstractmethod
    def __getitem__(self, key: SupportsIndex, /) -> T:
        raise NotImplementedError

    @abstractmethod
    def popleft(self) -> T:
        raise NotImplementedError