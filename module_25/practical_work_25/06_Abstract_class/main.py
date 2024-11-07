from abc import ABC, abstractmethod
import math


class Sharp(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Sharp):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


class Rectangle(Sharp):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Sharp):
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth

    def area(self):
        return 0.5 * self.base * self.heigth


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
