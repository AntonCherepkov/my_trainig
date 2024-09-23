import typing


def to_twice(function: typing.Callable) -> typing.Callable:
    """Декоратор двойного вызова функции"""

    def wrapper_func(*arg: typing.Any, **kwarg: typing.Any) -> None:
        for _ in range(2):
            function(*arg, **kwarg)
    
    return wrapper_func


@to_twice
def greenting(name: str) -> None:
    print(f'Привет, {name}!')


greenting('Tom')
