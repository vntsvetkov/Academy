from math import sqrt, cos


class Triangle:
    __color: str
    __ANGLE_SUM: int = 180

    def __init__(self, a: float = 0, b: float = 0, c: float = 0,
                 angle_a: int = 0, angle_b: int = 0, angle_c: int = 0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__angle_a = angle_a
        self.__angle_b = angle_b
        self.__angle_c = angle_c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def height(self, key: str):
        side = {"a": self.__a, "b": self.__b, "c": self.__c}
        p = (self.__a + self.__b + self.__c) / 2
        return 2 * sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)) / side[key]

    @staticmethod
    def is_triangle(a: float, b: float, c: float):
        return (a < b + c) and (b < a + c) and (c < a + b)

    @classmethod
    def create_triangle_by_angle_and_two_side(cls, a: float, b: float, angle: int):
        c = int(sqrt(a*a + b*b - 2*a*b*cos(angle)))
        return cls(a, b, c, angle)

    def __str__(self):
        return f"Сторона a: {self.__a} \n" \
               f"Сторона b: {self.__b} \n" \
               f"Сторона с: {self.__c} \n"

