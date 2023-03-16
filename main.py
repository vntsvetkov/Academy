""" Модуль 9. День 2. Object oriented programming"""
"""
Модификаторы доступа:
    public - общедоступный модификатор
    private - обращение доступно только внутри класса
    protected - обращение доступно только внутри класса и класса наследника
"""

class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str,
                 salary: float = 0, premium: float = 0):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__language = language
        self.__company = company
        self.__salary = salary
        self.__premium = premium

    def __str__(self):
        return f"Имя: {self.__name} \n" \
               f"Возраст: {self.__age} \n" \
               f"Пол: {self.__gender} \n" \
               f"Язык программирования: {self.__language} \n" \
               f"Компания: {self.__company} \n" \
               f"Заработная плата: {self.__salary + self.__premium}"

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    def __calc_premium(self, percent: float = 0):
        return self.__salary * percent / 100

    def get_premium(self):
        return self.__premium

    def set_premium(self, percent: float = 0):
        self.__premium = Programmer.__calc_premium(self, percent)


def execute_application():
    programmer = Programmer("Иван", 32, "male", "Python", "Яндекс", 100000)
    programmer.set_premium(10)
    print(programmer.get_premium())

    programmer.age = 21
    print(programmer.age)


if __name__ == "__main__":
    execute_application()
