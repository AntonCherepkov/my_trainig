from typing import Callable


def decorator_with_args_for_any_decorator(update_decorator) -> Callable:
    """Декоратор для декоратора, который принимает его как обычную функцию"""
    
    def decorator_for_decorator(*args, **kwargs) -> Callable:
        """Декоратор, который декорирует что либо с аргументами, сохраняя их"""
        
        def wraps_for_decorator(decorator):
            """Обёртка для изменяемого декоратора"""
            return update_decorator(decorator, *args, **kwargs)
        return wraps_for_decorator
    return decorator_for_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    
    def wrapped_function(*func_args, **func_kwargs) -> Callable:
        print(f'Переданные арги и кварги: {args}, {kwargs}')
        return func(*func_args, **func_kwargs)
    return wrapped_function


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
