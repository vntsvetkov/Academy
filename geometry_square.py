from math import sin
"""Создайте класс для подсчета площади геометрических
фигур. Класс должен предоставлять функциональность
для подсчета площади треугольника по разным формулам,
площади прямоугольника, площади квадрата, площади
ромба. Методы класса для подсчета площади должны
быть реализованы с помощью статических методов."""


class GeometrySquare:

    @staticmethod
    def triangle_square_1(a: float, h: float):
        return 0.5 * a * h

    @staticmethod
    def triangle_square_2(a: float, b: float, angle: int):
        return 0.5 * a * b * sin(angle)

    @staticmethod
    def triangle_square_3(a: float, angleA: int, angleB: int):
        return 0.5 * a * a * (sin(angleA) * sin(angleB)) / sin(angleA + angleB)
