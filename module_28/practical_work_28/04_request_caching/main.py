from typing import Tuple, Any, Callable
from functools import wraps


class LRUCache:
    """
    Класс для кеширования данных с интеграцией 
    очереди и обновлением по частоте запросов

    Args:
        capacity (int): Разрешённый размер хеш-таблицы

    Attributes:
        size (int): Текущий размер
        _cache (Any): Кэш - значения
        _keys (Any): Кэш - ключи
        queue (List): Очередь элементов

    Methods:
        _hash_function(): Хзш - функция
        _liner_probing(): Метод линейного пробирования
        get(): Метод для возврата значения по ключу
        cache(): Добавление элементов в хеш - таблицу
        print_cache(): Вывод в консоли содержания хеш - таблицы
    """
    def __init__(self, capacity: int = 3) -> None:
        self.capacity = capacity
        self.size = 0
        self._cache = [None] * self.capacity
        self._keys = [None] * self.capacity
        self.queue = []


    def _hash_function(self, key):
        return hash(key) % self.capacity


    def _liner_probing(self, key):
        """Метод линейного пробирования для исключения коллизии"""
        hash_val = self._hash_function(key)
        start = hash_val

        while (self._cache[hash_val] is not None 
                and self._keys[hash_val] != key):
            hash_val = (hash_val + 1) % self.capacity
            
            if hash_val == start:
                raise IndexError("Хеш таблица переполненна!")
            
        return hash_val


    def get(self, key):
        """
        Метод для получения значения по хешу.
        Если найден, обновляем порядок использования
        """
        hash_val = self._liner_probing(key)
        start = hash_val

        while self._cache[hash_val] is not None:
            if self._keys[hash_val] == key:
                self.queue.remove(hash_val)
                self.queue.insert(0, hash_val)
                return self.cache[hash_val]

            hash_val = (hash_val + 1) % self.capacity

            if hash_val == start:
                break
        
        return -1


    @property
    def cache(self):
        return self._cache
    

    @cache.setter
    def cache(self, key_value: Tuple[Any, Any]) -> None:
        """
        Сеттер для добавления элементов в хеш - таблицу,
        обновление очереди и повышение рейтинга при
        повторных запросах

        Args:
            key_value (tuple): Входные данные - ключ, значение
        """
        key, value = key_value

        if self.size >= self.capacity:
            old_key = self.queue.pop()
            self._cache[old_key] = None
            self._keys[old_key] = None
            self.size -= 1
        
        hash_value = self._liner_probing(key)

        if self._cache[hash_value] is None:
            self._cache[hash_value] = value
            self._keys[hash_value] = key
            self.size +=1

        if hash_value in self.queue:
            self.queue.remove(hash_value)

        self.queue.insert(0, hash_value)
        


    def print_cache(self):
        print(f'Кэш (id -> values): {self.cache}')
        print(f'Индекс (id -> key): {self._keys}')
        print(f'Очередь: {self.queue}')


cache = LRUCache()

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key4", "value4")

cache.print_cache()