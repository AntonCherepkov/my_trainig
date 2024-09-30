from __future__ import annotations
from typing import Union


class File:
    """Контекстный менеджер для работы с файлами"""
    def __init__(self, name: str, mode: str) -> None:
        self.file_obj = None
        self.name = name
        self.mode = self.mode_control(mode)

    
    def mode_control(self, mode) -> str:
        if mode == 'r' or mode == 'w':
            return mode
        raise TypeError(f'Не верные поле mode={mode}; Доступно для установки "r" или "w"')


    def __enter__(self) -> File:
        self.file_obj = open(file=self.name, mode=self.mode, encoding='utf-8')
        return self.file_obj


    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.file_obj.close()


with File('my_test.txt', 'w') as file:
    file.write('Привет мир!')
