from typing import Callable, Union, Any
import math
from functools import wraps



def inputdata(function: Callable) -> Callable:
    """
    Декоратор, проверяющий поля передаваемого метода
    """
    @wraps(function)
    def wrap_param(*args, **kwargs) -> Any:
        try:
            if (all(isinstance(a, (int, float)) for a in args) and 
                    all(isinstance(k, (int, float)) for k in kwargs.values())):
                return function(*args, **kwargs)
            else:
                raise TypeError()
        except TypeError as exc:
            return 'Не возможно вывести значение!'

    return wrap_param


class MyMath:
    @staticmethod
    @inputdata
    def valume_parallepiped(length, width, height) -> Union[int, float]:
        return length * width * height


    @staticmethod
    @inputdata
    def valume_cube(height: Union[int, float]) -> Union[int, float]:
        return pow(height, 3)

    
    @staticmethod
    @inputdata
    def circle_len(radius: Union[int, float]) -> Union[int, float]:
        return 2 * math.pi * radius


    @staticmethod
    @inputdata
    def circle_sq(radius: Union[int, float]) -> Union[int, float]:
        return math.pi * pow(radius, 2)

    
    @staticmethod
    @inputdata
    def surface_area_sphere(radius: Union[int, float]) -> Union[int, float]:
        return 4 * math.pi * pow(radius, 2)


res_1 = MyMath.circle_len(5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.valume_cube(height=3)
res_4 = MyMath.surface_area_sphere(4)
res_5 = MyMath.valume_parallepiped(length=2, width=6, height='4')

print(f'Длина окружности: {res_1}')
print(f'Площадь круга: {res_2}')
print(f'Объём куба: {res_3}')
print(f'Площадь поверхности сферы: {res_4}')
print(f'Площадь параллелограмма: {res_5}')
