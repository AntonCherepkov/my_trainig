from typing import Union, Any, Callable, Optional
from datetime import datetime
from functools import wraps
from time import sleep


def save_log(function: Callable) -> Callable:
    """Декоратор для записи логов в файл"""
    @wraps(function)
    def wrapped_save(*args, **kwargs):
        data_name = function.__name__
        data_doc = function.__doc__.split('\n')[0].lstrip()
        
        info_date = str(datetime.now())

        param = ' '.join([kwarg for kwarg in kwargs.keys()])

        result = function(*args, **kwargs)
        
        with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
            log_file.write(
                'Вызван метод: ' + data_name + '\n'
                + 'Дата вызова: ' + info_date + '\n'
                + 'Параметры функции: ' + param + '\n'
                + 'Назначение параметра: ' + data_doc + '\n\n'
            )

        return result
    return wrapped_save


def logging(decorator: Callable) -> Callable:
    """Декоратор класса для логирования работы методов"""
    @wraps(decorator)
    def wrapped_decorator(cls) -> Any:
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                current_method = getattr(cls, i_method)
                decorate_method = decorator(current_method)
                setattr(cls, i_method, decorate_method)

        return cls
    return wrapped_decorator


@logging(save_log)
class TestClass:
    """Тестовый класс"""
    def __init__(self, prime_num=1):
        self.prime_num = prime_num

    def method_1(self):
        """Первый тестовый метод"""
        return self.prime_num

    def method_2(self, param):
        """Второй тестовый метод"""
        return self.prime_num + param

    def method_3(self):
        """Третий тестовый метод"""
        return self.prime_num + 2


one_test_object = TestClass()
print(one_test_object.method_1())

sleep(2)

two_test_object = TestClass()
print(two_test_object.method_2(2))

sleep(2)

tree_test_object = TestClass()
print(tree_test_object.method_3())
