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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    def __calc_premium(self, percent: float = 0):
        return self.__salary * percent / 100

    def get_premium(self):
        return self.__premium

    def set_premium(self, percent: float = 0):
        self.__premium = self.__calc_premium(percent)
        # self.__premium = self.__salary * percent / 100


def execute_application():
    programmer = Programmer("Иван", 32, "male", "Python", "Яндекс", 100000)


if __name__ == "__main__":
    execute_application()