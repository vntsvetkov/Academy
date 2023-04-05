import math
from abc import ABC, abstractmethod


class RectangleFormulas(ABC):
    @abstractmethod
    def area_by_diagonal(self):
        pass


class CircleFormulas(ABC):
    @abstractmethod
    def area_by_diameter(self):
        pass


class Figure:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Rectangle(Figure, RectangleFormulas):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimetr(self):
        return (self.__width + self.__height) * 2

    def __diagonal(self):
        return math.sqrt(self.__width**2 + self.__height**2)

    def area_by_diagonal(self):
        d = self.__diagonal()
        return self.__width * math.sqrt(d**2 - self.__width**2)


class Circle(Figure, CircleFormulas):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.__radius

    def __diameter(self):
        return 2 * self.__radius

    def area_by_diameter(self):
        d = self.__diameter()
        return 0.25 * d**2 * math.pi
