class UserBase:
    """
    Простой класс для хранения идентификаторов пользователей на базе хеш-таблицы
    По умолчанию доступ имеет пользователь с идентификатором 'Admin'
    
    Args:
        permission (int): допустимое количество идентификаторов (default = 10)

    Attributes:
        permission (int): допустимое количество ячеек в хеш-таблице
        _user_permission (list): хеш-таблица для хранения идентификаторов
    
    Methods:
        _hash_function(): хеш-функция для генерации хеш-значений
        linear_probing(): метод для линейного пробирования хеш-значений
        user_permission(): геттеры и сеттеры для внесения изменений в хеш-таблицу
        deleted_user(): метод для удаления идентификаторов из хеш-таблицы
        __str__(): возвращает список пользователей, которые имеют доступ к ресурсу
    """
    def __init__(self, permission: int = 10) -> None:
        self.permission = permission
        self._user_permission = [None] * self.permission


    def _hash_function(self, key: str) -> int:
        """Простая хеш-функция, на базе встроенного метода hash()"""
        return hash(key) % self.permission


    def linear_probing(self, i_hash: int) -> int:
        """Метод линейного пробирования для исключения коллизий при добавлении новых элементов"""
        started_hash = i_hash

        while self._user_permission[i_hash] is not None:
            i_hash = (i_hash + 1) % self.permission

            if i_hash == started_hash:
                raise IndexError('Максимальное число пользователей!')

        return i_hash


    @property
    def user_permission(self):
        return self._user_permission


    @user_permission.setter
    def user_permission(self, key: str) -> None:
        """Добавление пользователя в хеш таблицу"""
        hash_val = self._hash_function(key)

        if self._user_permission[hash_val] is not None:
            hash_val = self.linear_probing(hash_val)

        self._user_permission[hash_val] = key


    def deleted_user(self, key: str) -> None:
        """Метод для удаления пользователя из хеш-таблицы по ключу"""
        hash_val = self._hash_function(key)
        start_index = hash_val

        while self.user_permission[hash_val] is not None:
            if self._user_permission[hash_val] == key:
                self._user_permission[hash_val] = None
                print(f'Пользователь {key} удален!')
                break

            hash_val = (hash_val + 1) % self.permission

            if hash_val == start_index:
                print(f'Пользователь {key} не найден в базе!')
                break


    def is_check(self, key: str) -> bool:
        hash_val = self._hash_function(key)
        start_index = hash_val

        while self.user_permission[hash_val] is not None:
            if self._user_permission[hash_val] == key:
                return True
            hash_val = (hash_val + 1) % self.permission
            if hash_val == start_index:
                break
        return False


    def __str__(self):
        result_str = 'Список пользователей, имеющих доступ к функции:\n'
        for name in self._user_permission:
            if name is not None:
                result_str += f'{name}\n'
        return result_str
