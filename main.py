""" Модуль 9. День 2. Object oriented programming"""


class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str):
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


def execute_application():
    programmer = Programmer("Иван", 32, "male", "Python", "Яндекс")
    print(programmer)


if __name__ == "__main__":
    execute_application()
