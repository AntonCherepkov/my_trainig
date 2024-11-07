import inspect
from typing import Callable, Optional, Any, Type
from functools import wraps
from my_time import MyTime
from time import perf_counter


def log_method(_function=None, *, time_format: str, method_info: str, child: bool) -> Callable[[Callable], Callable]:
    def loging_decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapped_function(*args, **kwargs) -> Any:
            file_log = open(file='log_file.txt', mode='a+', encoding='utf-8') 
            now_time = MyTime.now(time_format)
            start_time = perf_counter()
            file_log.write(f'- Запускается {method_info}. Дата и время запуска: {now_time}\n')
            
            if child:
                file_log.write(f'Тут метод {function.__name__} у наследника\n')
            else:
                file_log.write(f'Тут метод {function.__name__}\n')

            result = function(*args, **kwargs)

            run_time = round(perf_counter() - start_time, 4)
            file_log.write(f'- Завершение {method_info}. Время работы: {run_time}\n')
            file_log.close()

            return result
        return wrapped_function
    if _function is None:
        return loging_decorator
    return loging_decorator(_function)


def log_methods(*args) -> Callable:
    def decorator_for_methods(cls):
        is_child = all(i_class is not object for i_class in cls.__bases__)
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                current_method = getattr(cls, i_method)
                if inspect.isfunction(current_method) or inspect.ismethod(current_method):
                    method_info = f'{cls.__name__}.{i_method}'
                    decorate_method = log_method(current_method, time_format=args[0],method_info=method_info, child=is_child)
                    setattr(cls, i_method, decorate_method)

        return cls
    return decorator_for_methods
