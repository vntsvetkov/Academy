class Point:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{Point.__name__}(x: {self.__x}, y: {self.__y})"

    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}"

    def __bytes__(self):
        # перевод в байтовое представление
        pass

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        raise Exception(f"{other.__class__} не является объектом класса Point")

    def __hash__(self):
        return hash((self.__x, self.__y))