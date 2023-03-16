""" Модуль 9. День 2. Object oriented programming"""


class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str,
                 salary: float = 0, premium: float = 0):
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        self.company = company
        self.salary = salary
        self.premium = premium

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Пол: {self.gender} \n" \
               f"Язык программирования: {self.language} \n" \
               f"Компания: {self.company} \n" \
               f"Заработная плата: {self.salary + self.premium}"

    def calc_premium(self, percent: float = 0):
        return self.salary * percent / 100


def execute_application():
    programmer = Programmer("Иван", 32, "male", "Python", "Яндекс", 100000)
    premium = programmer.calc_premium(5)
    programmer.premium = premium
    print(programmer)


if __name__ == "__main__":
    execute_application()
