from typing import Iterable, TypeVar

T = TypeVar('T')

def chunked(items: list[T], size: int) -> list[list[T]]:
    if size <= 0:
        raise ValueError('size must be positive')
    return [items[i:i + size] for i in range(0, len(items), size)]

