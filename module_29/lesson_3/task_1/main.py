from typing import Union, Callable
from time import time, sleep
from functools import wraps
from datetime import datetime


def print_info(cls) -> Callable:
    """Декоратор класса, который выводит информацию о времени создания и список методов объекта класса"""
    @wraps(cls)
    def wrapped_info(*args, **kwargs) -> Callable:
        print(f'Время создания объекта {datetime.now()}')
        print(f'Aтрибуты объекта:')
        for method_name in dir(cls):
            if method_name.startswith('__') is False:
                print(method_name)
        
        return cls(*args, **kwargs)
    return wrapped_info


@print_info
class MyMathClass:
    """Это простой класс, содержащий несколько методов в качестве примера"""
    def __init__(self, num_pi=3.14):
        self.num_pi = num_pi


    def valume_parallepiped(length, width, height) -> Union[int, float]:
        return length * width * height


    def valume_cube(height: Union[int, float]) -> Union[int, float]:
        return pow(height, 3)


    def circle_len(radius: Union[int, float]) -> Union[int, float]:
        return 2 * self.num_pi * radius


    def circle_sq(radius: Union[int, float]) -> Union[int, float]:
        return self.num_pi * pow(radius, 2)


    def surface_area_sphere(radius: Union[int, float]) -> Union[int, float]:
        return 4 * self.num_pi * pow(radius, 2)



math_funcs = MyMathClass()
sleep(2)
math_funcs_2 = MyMathClass()