from __future__ import annotations
from typing import Literal, Optional


class File:
    """Контекст-менеджер для работы с файлами"""
    def __init__(self, name: str, mode: Literal['r', 'w']) -> None:
        self.name = name
        self.mode = self.__class__.mode_control(mode)
        self.file: Optional[File] = None


    @classmethod
    def mode_control(cls, mode: Literal['r', 'w']) -> str:
        if mode not in ['r', 'w']:
            raise TypeError('Не корректный режим работы!')
        return mode


    def __enter__(self) -> File:
        try:
            self.file = open(file=self.name, mode=self.mode, encoding='utf-8')
        except FileNotFoundError as exc:
            print('Файл не обнаружен, создаём пустой файл!')
            self.file = open(file=self.name, mode='w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('proba.txt', 'w') as my_file:
    my_file.write('Hello word!')


with File('proba.txt', 'r') as my_file:
    for string in my_file.readlines():
        print(string)
