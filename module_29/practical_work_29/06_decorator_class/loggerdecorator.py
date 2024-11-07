from time import perf_counter
from typing import Callable
from functools import update_wrapper


class LoggerDecorator:
    def __init__(self, function: Callable) -> None:
        update_wrapper(self, function)
        self.function = function
    

    def __call__(self, *args, **kwargs):
        
        st_time = perf_counter()
        result = self.function(*args, **kwargs)
        run_time = perf_counter() - st_time

        print(f'Вызов функции {self.function.__name__}')
        print(f'Аргументы: {args}, {kwargs}')
        print(f'Результат: {result}')
        print(f'Время выполнения: {run_time}')

        return result
