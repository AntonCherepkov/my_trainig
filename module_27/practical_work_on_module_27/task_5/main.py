from typing import Callable, Any
from functools import wraps


# def counter(function: Callable) -> Callable:
#     """Декоратор, подсчитывающий количество вызовов функции-мишени"""
#     count = [0]

#     @wraps(function)
#     def wrapper(*args: Any, **kwargs: Any) -> Any:
#         count[0] += 1
#         result = function(*args, **kwargs)
#         print(f'Количество вызовов: {count[0]}')
#         return result
#     return wrapper


def counter(function: Callable) -> Callable:
    """Декоратор, подсчитывающий количество вызовов функции-мишени"""

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.count += 1
        result = function(*args, **kwargs)
        print(f'Количество вызовов: {wrapper.count}')
        return result

    wrapper.count = 0
    return wrapper


@counter
def test_func():
    """Мини функция, возвращающая 1, когда её вызывают"""
    return 1


for _ in range(5):
    print(test_func())
