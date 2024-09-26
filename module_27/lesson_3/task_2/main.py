from typing import Callable, Any, Generator


PLUGINS = dict()


# def regisred(function: Callable) -> Callable:
#     """Декоратор для регистрации функции, как плагина"""
#     def wrapped_for_registrator(*args: Any, **kwargs: Any) -> None:
#         """Функция-обёртка для постановки на учёт плагина"""
#         PLUGINS[function.__name__] = function
#         result_work = function(*args, **kwargs)
        
#         return result_work
#     return wrapped_for_registrator


def regisred(function: Callable) -> Callable:
    PLUGINS[function.__name__] = function
    return function


@regisred
def sum_square(num: int) -> int:
    """Функция подсчета квадратов ряда чисел от 1 до num"""
    return sum(i ** 2 for i in range(1, num + 1))


@regisred
def generator_numbers_fibbonachi(num: int) -> Generator[int, None, None]:
    """Генератор чисел Фиббоначи"""
    started_num = 0
    ended_num = 1
    yield started_num
    yield ended_num
    count_iter = 1
    while count_iter <= num:
        result_calc = started_num + ended_num
        yield result_calc
        started_num = ended_num
        ended_num = result_calc
        count_iter += 1


gen_fib_obj = generator_numbers_fibbonachi(25)
for num in gen_fib_obj:
    print(num, end=' ')
print()

num = 10
sum_square_number = sum_square(num)
print(f'Результат вычисления суммы квадротов числа от 1 до {num}: {sum_square_number}')

print('Итого зарегистрировано плагинов: ')
counter_plugins = 1
for name, func in PLUGINS.items():
    print('{:d}): {:s} функция, {:s} объект'.format(
        counter_plugins, name, str(func)
    ))
    counter_plugins += 1
