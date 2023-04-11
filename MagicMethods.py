import pickle
class Point:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{Point.__name__}(x: {self.__x}, y: {self.__y})"

    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}"

    def __bytes__(self):
        return pickle.dumps(self.__dict__)

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__x, self.__y))