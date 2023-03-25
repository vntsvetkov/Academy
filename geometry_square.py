from math import sin, pi
from figures import Triangle
"""
Создайте класс для подсчета площади геометрических фигур. 
Класс должен предоставлять функциональность для подсчета площади треугольника по 3 разным формулам и площади круга. 
Методы класса для подсчета площади должны быть реализованы с помощью статических методов.
"""


class GeometrySquare:

    @staticmethod
    def triangle_square_by_side_and_height(a: float, h: float):
        return 0.5 * a * h

    @staticmethod
    def triangle_square_by_two_side_and_angle(a: float, b: float, angle: int):
        return 0.5 * a * b * sin(angle)

    @staticmethod
    def triangle_square_by_side_and_two_angle(a: float, angle_a: int, angle_b: int):
        return 0.5 * a * a * (sin(angle_a) * sin(angle_b)) / sin(angle_a + angle_b)

    @staticmethod
    def circle_square_by_diameter(d: float):
        return 0.25 * pi * d ** 2

    @staticmethod
    def circle_square_by_len_and_diameter(c: float, d: float):
        return 0.25 * c * d

    @staticmethod
    def circle_square_by_radius(r: float):
        return pi * r ** 2
