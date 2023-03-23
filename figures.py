from math import sqrt
class Triangle:
    __color: str
    __ANGLE_SUM: int = 180
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def height(self, key: str):
        side = {"a": self.__a, "b": self.__b, "c": self.__c}
        p = (self.__a + self.__b + self.__c) / 2
        return 2 * sqrt(p*(p-self.__a)*(p-self.__b)*(p-self.__c)) / side[key]

    @staticmethod
    def is_triangle(a: float, b: float, c: float):
        if (a < b + c) and (b < a + c) and (c < a + b):
            return Triangle(a, b, c)
        else:
            raise Exception("Треугольника с данными сторонами не существует")

    @classmethod
    def create_triangle_by_angles(cls, a: float, angleA: int, angleB: int):
        b = None
        c = None
        return cls(a, b, c)

    def __str__(self):
        return f"Сторона a: {self.__a} \n" \
               f"Сторона b: {self.__b} \n" \
               f"Сторона с: {self.__c} \n"

class Circle:
    pass

