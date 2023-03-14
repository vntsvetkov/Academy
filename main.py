""" Модуль 9. День 1"""
"""
Object oriented programming
"""
# Задача 1. Описать класс программист.
class Programmer:

    name: str
    age: int
    gender: str
    language: str
    company: str

    def __init__(self, name: str, age: int, gender: str,
                language: str, company: str):
        """Конструктор класса Programmer"""
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        self.company = company


def execute_application():
    programmer = Programmer()
    print(programmer.__dict__)
    programmer1 = Programmer()
    print(programmer1.__dict__)


if __name__ == "__main__":
    execute_application()