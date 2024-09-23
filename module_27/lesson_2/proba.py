def logging(function):
    """Декоратор для вызова функций и отображения их названия"""

    def wrapped_func(*args, **kwarg):
        print(f'Вызвана функция {function.__name__}')
        function()
    
    return wrapped_func


@logging
def my_name():
    print('Anton')


@logging
def name_boss():
    print('Evgeniy')


my_name()
name_boss()
