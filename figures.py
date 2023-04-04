# Прямоугольник
import math


class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimetr(self):
        return (self.__width + self.__height) * 2


class Circle:
    def __init__(self, x: int, y: int, radius: int):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.__radius
