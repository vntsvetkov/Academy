""" Модуль 9. День 1"""
"""
Object oriented programming
"""
from typing import List
# Задача 1. Описать класс программист.
class Programmer:

    name: str
    age: int
    gender: str
    language: str
    company: str

    def __init__(self, name: str, age: int, gender: str,
                language: str, company: str = None):
        """Конструктор класса Programmer"""
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        self.company = company

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Пол: {self.gender} \n" \
               f"Язык программирования: {self.language} \n" \
               f"Компания: {self.company}"

# Задача 1.1 Создать класс IT-Компания
class ITCompany:
    name: str
    address: str # лучше словарь
    programmers: List[Programmer]

    def __init__(self, name: str, address: str, programmers: list = None):
        self.name = name
        self.address = address
        if programmers is None:
            self.programmers = []
        else:
            self.programmers = programmers.copy()

    def __str__(self):
        return f"Название компании: {self.name} \n" \
               f"Адрес компании: {self.address} \n"


def execute_application():
    programmer1 = Programmer("Иван", 32, "male", "Python", "Yandex")
    programmer2 = Programmer("Петр", 36, "male", "C++", "Yandex")

    company = ITCompany("Yandex", "119021, Москва, ул. Льва Толстого, 16")
    company.programmers.append(programmer1)
    company.programmers.append(programmer2)
    print(company)
    for programmer in company.programmers:
        print(programmer)


if __name__ == "__main__":
    execute_application()