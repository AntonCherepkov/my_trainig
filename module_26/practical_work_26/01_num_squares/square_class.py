from typing import Iterator


class SquareIterClass:
    
    """The iterator class for squaring a sequance of numbers"""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.__count = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self):
        if self.__count >= self.limit:
            raise StopIteration
        else:
            self.__count += 1
            return pow(self.__count, 2)
