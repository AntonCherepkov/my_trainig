from typing import Callable, Any
from functools import wraps
from time import perf_counter


def timer_decorator(function: Callable) -> Callable:
    @wraps(function)
    def timer_wrapped(*args, **kwargs) -> Any:
        started_at = perf_counter()
        result = function(*args, **kwargs)
        ended_at = perf_counter()
        run_time = ended_at - started_at
        print(f'Функция {function.__name__} работала: {run_time}')

        return result
    return timer_wrapped


def hash_decorator(function: Callable) -> Callable:
    """Декоратор для хеширования возвращаемых значений рекурсивных функций"""
    hash_dict = dict()
    @wraps(function)
    def hash_wrapped(*args: int, **kwargs: int) -> int:
        if args not in hash_dict:
            hash_dict[args] = function(*args, **kwargs)

        return hash_dict[args]
    return hash_wrapped


@timer_decorator
@hash_decorator
def fibonachi(num: int) -> int:
    """Рекурсивная функция вычислений чисел Фибоначчи"""
    if num <= 1:
        return num

    return fibonachi(num - 1) + fibonachi(num - 2)


print(fibonachi(10))
