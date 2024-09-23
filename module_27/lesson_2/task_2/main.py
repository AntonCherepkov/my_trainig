from typing import Callable, Any


def timer_decorator(function: Callable[[Any, ...], Any]) -> Callable[[Any, ...], Any]:
    """
    Декоратор для измерения времени работы обёрнутой функции

    :param function: оборачиваемая функция
    :type function: Callable[[Any, ...], Any]
    :return: объект декорированной функции
    :rtype: Callable[[Any, ...], Any]
    """
    from time import perf_counter

    def wrapper_func(*args: Any, **kwargs: Any) -> Any:
        """
        Функция-обёртка для измерения скорости выполнения функций

        :param args: любые позиционные аргументы
        :type args: Any
        :param kwargs: любые именованые значения
        :type kwargs: Any
        :return: любое значение, на выходе функции мишени
        :rtype: Any
        """
        started_at = perf_counter()
        result = function(*args, **kwargs)
        stoped_at = perf_counter()
        return round(stoped_at - started_at, 5), result
        
    return wrapper_func


@timer_decorator
def factorial(number: int) -> int:
    """Вычисление факториала числа самым долгим способом"""
    result = 1

    for i in range(2, number + 1):
        result *= i
    
    return result


time_sec, value = factorial(10)
print(f'Время выполнения функции: {time_sec}\nПолученное значение: {value}')
