from time import sleep
from typing import Callable, Any, List
import functools


def decorator_slowing_down(function: Callable) -> Callable:
    """
    Декоратор, замедляющий работу переданной функции
    """
    @functools.wraps(function)
    def deceleration_wrapper(*args, **kwargs) -> Any:
        if 'timer' in kwargs:
            print(f'Замедляю функцию на {kwargs["timer"]} секунд')
            sleep(kwargs['timer'])
            kwargs.pop('timer')
        else:
            print(f'Значения, на которое надо было замедлить функцию не было передано, '
                   'поэтому замедлим функцию на 2 секунды...')
            sleep(2)

        result = function(*args, **kwargs)

        return result
    return deceleration_wrapper


@decorator_slowing_down
def list_numbers_fib(number: int) -> List[int]:
    """Функция, которая формирует список чисел Фиббоначи, самым убогим способом
    
    :param number: Количество чисел в возвращаемой последовательности
    :type number: int
    :return: список чисел Фиббоначи
    :rtype: List[int]
    """
    result_list = [0, 1]
    started_num = 0
    ended_num = 1

    for _ in range(number - 2):
        summ = started_num + ended_num
        result_list.append(summ)
        started_num = ended_num
        ended_num = summ
    
    return result_list


list_nums = list_numbers_fib(5, timer=5)

print('Вывод тестового прогона декорируемой функции: ', end='')
for num in list_nums:
    print(num, end=' ')
