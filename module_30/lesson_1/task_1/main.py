from typing import Callable
from functools import wraps

def count_instance(function: callable) -> Callable:
    loc_count = 0
    
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        nonlocal loc_count
        loc_count += 1
        global glob_count
        glob_count += 1

        print(f'Вызвали и записали в соседнем окружении: {loc_count}')
        return function(*args, **kwargs)
    return wrapped_function


@count_instance
def test_1():
    print(f'Вызвали и записали в глобальную переменную: {glob_count}')


glob_count = 0
test_1()
test_1()
test_1()

print(dir(__builtins__))
