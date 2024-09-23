from typing import Callable, Any


def bread_decorator(function: Callable) -> Callable:
    """Декоратор для добавления булочек в сэндвич"""
    def wrapper_func(*args) -> None:
        """Функция обёртка для булочек сэндвича"""
        print('</--------\\>')
        function()
        print('\\________/>')
    return wrapper_func


def filling_decorator(function: Callable) -> Callable:
    """Декоратор для добавления начинки в сэндвич"""
    def wrapper_func(*args) -> None:
        """Функция обёртка для начинки сэндвича"""
        print('#помидор#')
        function()
        print('~~салат~~')

    return wrapper_func


@bread_decorator
@filling_decorator
def sandwich():
    print('--ветчина--')


sandwich()
