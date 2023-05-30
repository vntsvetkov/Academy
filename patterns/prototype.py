from abc import ABC, abstractmethod
from copy import deepcopy


class Shape(ABC):
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    @abstractmethod
    def clone(self):
        raise NotImplementedError


class Rectangle(Shape):

    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self.__width = width
        self.__height = height

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    rect = Rectangle(1, 2, "black", 2, 4)
    new_rect = rect.clone()
    print(rect)
    print(new_rect)
