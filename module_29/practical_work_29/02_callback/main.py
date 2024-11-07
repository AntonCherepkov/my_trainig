from typing import Callable, Any, Optional, Union, Dict
from functools import wraps


routes: Dict[Any, Callable] = {}


def callback(event: Union[str, int]) -> Callable:
    """
    Декоратор для регистрации функции в глобальной структуре данных, для
    последующего обратного вызова
    """
    def call_decorator(function: Callable) -> Callable:
        routes[event] = function
        @wraps(function)
        def call_func_wrapped(*args, **kwargs) -> Any:

            result = function(*args, **kwargs)

            return result
        return call_func_wrapped
    return call_decorator

# def callback(event: Union[str, int]) -> Callable:
#     """
#     Декоратор для регистрации функции в глобальной структуре данных, для
#     последующего обратного вызова без возможности передать в нее аргументы
#     """
#     def call_decorator(function: Callable) -> Callable:
#         routes[event] = function
#         return function
#     return call_decorator

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


class Terminal:
    def get(self, data: Union[str, int] = 0) -> Union[Callable, None]:
            return routes.get(data, None)


app = Terminal()

route: Callable = app.get('//')
if route:
    response = route()
    print('Ответ: ', response)
else:
    print('Такого пути нет')
