from functools import wraps
from typing import Callable


def decorator_with_args_for_any_decorator(decorator):
    """Декоратор, декарирующий декоратор"""

    @wraps(decorator)
    def real_decorator(*args, **kwargs):
        """Обертка, позволяющая запустить декарирующий декаратор, передав ему параметры"""
        return decorator(*args, **kwargs)
    return real_decorator
   

@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs):
    """Декоратор для декоратора, принимающий на вход также некоторые параметры"""
    print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
    
    def decorator_for_function(function):
        """Декоратор, принимающий на вход декорируемую функцию"""
    
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            """Обёртка для функции, запускающая её, и передающая ей параметры"""
            
            return function(*args, **kwargs)
        return wrapped_function        
    return decorator_for_function


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
