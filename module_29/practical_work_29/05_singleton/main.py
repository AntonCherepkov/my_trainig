from functools import wraps


def singleton(cls):
    """
    Декоратор-синглтон. 
    Работает по следующему принципу:
    1. Объявляем и сразу инициируем как None поле в переданном классе;
    2. В функции - обертке: если это поле пустое - передаем в него явно 
        вызов переданного класса;
    3. Возвращаем содержимое этого поля;
    4. Возвращаем объект обертки.
    """
    cls._instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        
        return cls._instance
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(f'{my_obj.__class__.__name__} -> {type(my_obj)}')
print(f'{my_another_obj.__class__.__name__} -> {type(my_another_obj)}')

print(f'id: {id(my_obj)}')
print(f'id: {id(my_another_obj)}')

print(f'Одна сущность: {my_obj is my_another_obj}')
