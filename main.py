""" День 3. Object-oriented programming"""
"""
Классификация методов.
1. Методы объекта/экземпляра класса. Обязательно первым параметром
указывается self (указывает на текущий объект класса)
2. Методы класса. Отмечаются декоратором @classmethod. Обязательно первым
параметром указывается cls (указывает на текущий класс)
Альтернативный конструктор.
3. Статические методы. Отмечаются декоратором @staticmethod.
Статический метод не может изменять ни состояние объекта, ни состояние класса.
Они работают как обычные функции

Статические поля класса - общие поля для всех объектов этого класса (определяются до метода init)
"""
class Programmer:

    def __init__(self, name: str, age: int, gender: str,
                 language: str, company: str,
                 salary: float = 0, premium: float = 0):
        # assert isinstance(age, int), "Неверный тип данных в поле age"
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__language = language
        self.__company = company
        self.__salary = salary
        self.__premium = premium

    @classmethod
    def init_from_file(cls, path: str):
        with open(path, "r", encoding="utf-8") as file:
            name = file.readline().rstrip("\n")
            age = int(file.readline().rstrip("\n"))
            gender = file.readline().rstrip("\n")
            language = file.readline().rstrip("\n")
            company = file.readline().rstrip("\n")
            salary = float(file.readline().rstrip("\n"))
            return cls(name, age, gender, language, company, salary)

    @staticmethod
    def read_from_file(path: str) -> tuple:
        with open(path, "r", encoding="utf-8") as file:
            name = file.readline().rstrip("\n")
            age = int(file.readline().rstrip("\n"))
            gender = file.readline().rstrip("\n")
            language = file.readline().rstrip("\n")
            company = file.readline().rstrip("\n")
            salary = float(file.readline().rstrip("\n"))
            return name, age, gender, language, company, salary

    def __str__(self):
        return f"Имя: {self.__name} \n" \
               f"Возраст: {self.__age} \n" \
               f"Пол: {self.__gender} \n" \
               f"Язык программирования: {self.__language} \n" \
               f"Компания: {self.__company} \n" \
               f"Заработная плата: {self.__salary + self.__premium}"

    @property
    def name(self):
        """@SelfDocument"""
        return self.__name

    @name.setter
    def name(self, name: str):
        # Подумать над обработкой
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        """

        :param age:
        :return:
        """
        if isinstance(age, int):
            if 18 <= age <= 65:
                self.__age = age
            else:
                raise Exception("Возраст не подходит")
        else:
            raise Exception("Не подходит тип значения")
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    def __calc_premium(self, percent: float = 0):
        """

        :param percent:
        :return:
        """
        return self.__salary * percent / 100

    def get_premium(self):
        return self.__premium

    def set_premium(self, percent: float = 0):
        self.__premium = self.__calc_premium(percent)
        # self.__premium = self.__salary * percent / 100


def execute_application():
    """Задание 1. Написать сеттер для поля класса age с вызовом исключения"""
    '''
    programmer = Programmer("Иван", 34, "male", "Python", "Яндекс", 100000)

    try:
        programmer.age = 45
    except Exception as e:
        print(e)

    print(programmer.age)
    '''

    """Задание 2. Создание экземпляра класса через classmethod"""
    '''
    programmer = Programmer.init_from_file("./employees/programmers.txt")
    print(programmer)
    '''

    """Задание 3. Создание экземпляра с использовнаием staticmethod"""
    '''
    # в data будет записан кортеж с данными объекта ("Иван", 32, ...)
    data = Programmer.read_from_file("./employees/programmers.txt")
    programmer = Programmer(*data)
    print(programmer)
    '''

if __name__ == "__main__":
    execute_application()