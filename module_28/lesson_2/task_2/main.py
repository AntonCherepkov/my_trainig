from typing import Tuple 
from abc import ABC, abstractmethod


class GeometricShapes(ABC):
    """Абстрактный базовый класс, общий для описания фигур"""
    def __init__(self, length: int, width: int, coord_x: int, coord_y: int) -> None:
        self.length: int = length
        self.width: int = width
        self.coord_x: int = coord_x
        self.coord_y: int = coord_y
        self.name: str = 'Фигура'


    @abstractmethod
    def move() -> None:
        pass

    def __str__(self):
        return f"{self.name} имеет размеры: {self.length, self.width}"


class ResizingMixin:
    """Класс примесь, добавляющий возможность изменять размеры фигур"""
    def resizing(self, new_length: int, new_width: int) -> None:
        self.length = new_length
        self.width = new_width


class Squar(GeometricShapes, ResizingMixin):
    """Дочерний класс, описывающий поведение квадрата."""
    def __init__(self, length: int, coord_x: int, coord_y: int) -> None:
        super().__init__(length=length, width=length, coord_x=coord_x, coord_y=coord_y)
        self.name = 'Квадрат'


    def move(self, new_coord_x: int, new_coord_y: int) -> None:
        self.coord_x = new_coord_x
        self.coord_y = new_coord_y


class Rectangle(GeometricShapes, ResizingMixin):
    """Дочерний класс, описывающий поведение прямоугольника"""
    def __init__(self, length: int, width: int, coord_x: int, coord_y: int) -> None:
        super().__init__(length=length, width=width, coord_x=coord_x, coord_y=coord_y)
        self.name = 'Прямоугольник'


    def move(self, new_coord_x: int, new_coord_y: int) -> None:
        self.coord_x = new_coord_x
        self.coord_y = new_coord_y


one_squar = Squar(length=8, coord_x=5, coord_y=5)
two_squar = Squar(length=5, coord_x=6, coord_y=4)

one_rectangle = Rectangle(length=10, width=24, coord_x=10, coord_y=8)
two_rectangle = Rectangle(length=9, width=23, coord_x=7, coord_y=11)

for figure in [one_squar, two_squar, one_rectangle, two_rectangle]:
    print(figure)
    figure.resizing(figure.length * 2, figure.width * 2)
    print(figure)
