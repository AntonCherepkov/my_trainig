from user_base import UserBase
from functools import wraps
from typing import Callable, Any, Optional


all_users = UserBase()

def check_permission(user_name: Optional[str] = None) -> Callable:
    """
    Декоратор для проверки прав доступа к ресурсу

    Args:
        user_name (str): Имя пользователя для проверки его права доступа к ресурсу
    """
    def decorator_permission(function: Callable) -> Callable:
        @wraps(function)
        def wrapped_permission(*args, **kwargs) -> Any:
            if user_name is not None:
                try:
                    has_permission = all_users.is_check(user_name)
                    if has_permission:
                        return function(*args, **kwargs)
                    raise PermissionError
                except PermissionError as exc:
                    print(f'У пользователя {user_name} недостаточно прав, чтобы выполнить функцию {function.__name__}')
            else:
                raise LookupError('Декоратор должен получить ID пользователя')

        return wrapped_permission
    return decorator_permission


@check_permission('Admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_10')
def add_comment():
    print('Добавляем комментарий')


all_users.user_permission = 'Admin'
for i in range(9):
    name = 'User_' + str(i)
    all_users.user_permission = name

delete_site()
add_comment()
