""" Модуль 9. День 1"""
"""
Object oriented programming
"""
# Задача 1. Описать класс программист.
class Programmer:
    # Поля класса
    name: str
    age: int
    gender: str
    language: str
    company: str


def execute_application():
    programmer = Programmer()
    programmer.name = "Николай"
    programmer.age = 28
    programmer.gender = "male"
    programmer.language = "Python"
    programmer.company = "Tensor"
    print(programmer.__dict__)


if __name__ == "__main__":
    execute_application()