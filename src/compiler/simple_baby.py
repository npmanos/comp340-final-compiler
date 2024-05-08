from abc import abstractmethod
from collections import Counter, deque
from collections.abc import Iterable, Sequence
from typing import Callable, Collection, Protocol, SupportsIndex, TypeAlias, TypeVar, runtime_checkable


BABY_WORDS = {
    'pee': '+',
    'gah': '-',
    'milk': '*',
    'heh': '/',
    'mama': '(',
    'dada': ')'
}

T = TypeVar("T", covariant=True)

Predicate: TypeAlias = Callable[[T], bool]

class SupportsDepop(Collection[T], Protocol[T]):
    @abstractmethod
    def __getitem__(self, key: SupportsIndex, /) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def pop(self) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def popleft(self) -> T:
        raise NotImplementedError


def _str_is_a(c: str) -> bool:
    return c == 'a'

def _popwhile(predicate: Predicate[T], iterable: SupportsDepop[T]):
    while len(iterable) > 0 and predicate(iterable[0]):
        yield iterable.popleft()

def _join_deque(que: deque[str]) -> str:
    return "".join(que)

def decipher(babyExp: str) -> str:
    deciphered_code = ''
    cur_baby_word = ''
    baby_que: deque[str] = deque(babyExp)
    
    while len(baby_que) > 0:
        c = baby_que.popleft()
        match c:
            case c if c.isspace():
                continue
            case 'b':
                a_counter = Counter(_popwhile(_str_is_a, baby_que))
                deciphered_code += str(a_counter['a'])
            case c if c.isalpha():
                cur_baby_word += c
                if cur_baby_word in BABY_WORDS:
                    deciphered_code += BABY_WORDS[cur_baby_word]
                    cur_baby_word = ''
            case _:
                raise SyntaxError

    return deciphered_code