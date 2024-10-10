from time import sleep, time
from functools import wraps
from typing import Callable, Optional


def set_time_delay(_function: Optional[Callable] = None, *, set_time: int = 1) -> Callable:
    def decorator_time_delay(function: Callable) -> Callable:
        
        @wraps(function)
        def wrapped_time(*args, **Kwargs):
            sleep(set_time)
            result = function(*args, **Kwargs)

            return result
        return wrapped_time
    
    if _function is None:
        return decorator_time_delay
    return decorator_time_delay(_function)


@set_time_delay(set_time=2)
def mul_even_num(num):
    return sum([i ** 2 for i in range(num)])


@set_time_delay
def my_print():
    print('Работа функции!')


st_1 = time()
result = mul_even_num(5)
print(f'Результат работы функции если что: {result}')
run_time_1 = time() - st_1
print(f'Время задержки составило: {run_time_1}')

st_2 = time()
my_print()
run_time_2 = time() - st_2
print(f'Время задержки составило: {run_time_2}')
