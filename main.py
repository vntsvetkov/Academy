""" Модуль 9. День 2. Object oriented programming"""


class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str, salary: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language
        self.company = company
        self.salary = salary

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Пол: {self.gender} \n" \
               f"Язык программирования: {self.language} \n" \
               f"Компания: {self.company} \n" \
               f"Заработная плата: {self.salary}"

    def get_premium(self, percent: float):
        return self.salary * percent / 100


def execute_application():
    programmer = Programmer("Иван", 32, "male", "Python", "Яндекс", 100000)
    premium = programmer.get_premium(10)
    print(programmer)
    print(f"Премия: {premium}")


if __name__ == "__main__":
    execute_application()
