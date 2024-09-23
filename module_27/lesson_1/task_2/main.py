import time
from time import perf_counter
from typing import Callable, Any, Union, Tuple, Generator


def timer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Tuple[float, Any]:
    """
    Измерение времени работы переданной функции

    :param func: функция первого порядка, для измерения времени её работы
    :type func: Callable[..., Any]
    :param args: любые и любое количество позиционных аргументов, передаваемые в функцию первого порядка
    :type args: Any
    :param kwargs: любые и любое количество именованных аргументов, передаваемых в функцию первого порядка
    :type kwargs: Any
    :return: кортеж, в котором первое значение - время работы функции, второе значение - результат
    :rtype: Tuple[float, Any]
    """
    start_timing = time.perf_counter()
    result_calculation = func(*args, **kwargs)
    end_timing = time.perf_counter()
    lead_time = round(end_timing - start_timing, 20)

    return lead_time, result_calculation


def factorial(number: int) -> int:
    """
    Рекурсивное определение факториала числа

    :param number: число для определения его факториала
    :type number: int
    :return: значение факториала
    :rtype: int
    """
    if number <= 1:
        return 1
    result = factorial(number - 1)
    return result * number


def fibbonachi_numbers_gen(count_iter: int = 0, started_num: int = 0, ended_num: int = 1) -> Generator[int, None, None]:
    """
    Генератор чисел Фиббоначи

    :param count_iter: число итераций по числам Фиббоначи
    :param started_num: Начальное значение
    :param ended_num: Конечное значение
    :return: генератор числа
    """
    while count_iter < 10:
        count_iter += 1
        next_num = started_num + ended_num
        started_num = ended_num
        ended_num = next_num
        yield ended_num


def show_work(func: Callable[..., Any], time_work: float, value: Union[Generator[int, None, None], float, int]) -> None:
    """
    Вывод на экран имени функции, её назначения и времени последнего прогона

    :param func: объект функции, в которой запрашивается её имя и первая строка из doc string
    :type func: Callable[..., Any]
    :param time_work: время работы функции
    :type time_work: float
    :param value: Union[str, float, int]
    """
    if isinstance(value,Generator):
        val_list = []
        for num in value:
            val_list.append(str(num))
        value = ', '.join(val_list)

    print('Функция "{:s}"\nВыполняла работу за: {:.8f} c\nПолучили значение: {}'. format(
        func.__name__ + ': ' + func.__doc__.strip().split('\n')[0],
        time_work,
        str(value)
    ))


time_1, val_1 = timer(factorial, 10)
show_work(factorial, time_work=time_1, value=val_1)

print()

time_2, val_2 = timer(fibbonachi_numbers_gen)
show_work(fibbonachi_numbers_gen, time_work=time_2, value=val_2)
