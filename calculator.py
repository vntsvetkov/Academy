import math


class Calculator:

    @staticmethod
    def add(x, y) -> float | int:
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mult(x, y):
        return x * y

    @staticmethod
    def div(x, y) -> float|str:
        if y != 0:
            return x / y
        else:
            return "Деление на ноль невозможно"

    @staticmethod
    def sqrt(n):
        if n >= 0:
            return math.sqrt(n)

        raise ValueError(f"Невозможно вычислить квадратный корень из {n}")


class EngineerCalculator(Calculator):
    pass


class ProgrammerCalculator(Calculator):
    pass
