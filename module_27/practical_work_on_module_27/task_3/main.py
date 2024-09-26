from typing import Callable, Any, List
import functools
import datetime
from random import randint


def archiving_errors(errors: str, name_func: str) -> None:
    """
    Архиватор ошибок

    :param errors: описание ошибок
    :type errors: str
    :param name_func: имя функции, где была выброшена ошибка
    :type name_func: str
    """
    with open(file='function_error.log', mode='a+', encoding='utf-8') as file_error:
        file_error.write(
            str(datetime.datetime.now()) 
            + ' -> ' + name_func.ljust(15, ' ')
            + ' -> ' + errors + '\n'
        )


def logging(func: Callable) -> Callable:
    """Декоратор логирования ошибок"""
    @functools.wraps(func)
    def catching_errors(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            archiving_errors(str(exc), func.__name__)
    return catching_errors


@logging
def test_func(num):
    """Функция, выбрасывающая ошибку, если ей передали не [int]"""
    if not isinstance(num, int):
        print('Внутри. Видим не верный тип данных!')
        raise TypeError('Тип данных не [int]')
    print(f'Внутри, видим {num}')
    return num


@logging
def random_error():
    """Функция, которая выбрасывает ошибку с вероятностью 1 к 5"""
    if randint(1, 5) == 1:
        print('Внутри. Случайная ошибка!')
        raise Exception('Случайная ошибка!')
    print('Внутри. Случайной ошибки не случилось!')


for arg in [1, 2, 3, '4', 5, '6', 7, 8, 9.5, 10]:
    test_func(arg)

for _ in range(10):
    random_error()
