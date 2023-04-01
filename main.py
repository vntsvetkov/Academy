"""День 5. Object-oriented programming. Наследование классов."""

"""
Наследование. 
1. Позволяет выделить общие характеристики для нескольких классов
2. Позволяет избежать повторения кода при определинии классов
3. Один из принципов ООП

Базовые (родительские) классы
Производные (дочерние) классы

"""
class ErrorSettingAge(Exception):
    def __init__(self, text, value):
        self.__text = text
        self.__value = value


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Имя: {self._name} \n"
              f"Возраст: {self._age}")

class Employee(Person):
    _AGE_LIMIT = 18
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)
        self._position = position
        self._salary = salary
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        self._position = value
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        self._salary = value
    @Person.age.setter
    def age(self, value):
        if value >= 18:
            self._age = value
        else:
            raise ErrorSettingAge(f"Возраст сотрудника должен быть больше либо равен", Employee._AGE_LIMIT)
    def info(self):
        super().info()
        print(f"Должность: {self._position} \n"
              f"Зарплата: {self._salary}")


class Programmer(Employee):
    def __init__(self, name: str, age: int, position: str, salary: float,
                 language: str, level: str ):
        super().__init__(name, age, position, salary)
        self.__language = language
        self.__level = level

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    def info(self):
        super().info()
        print(f"Язык: {self.__language} \n"
              f"Уровень: {self.__level} \n")


def execute_application():

    programmer = Programmer("Иван", 36, "Программист", 160000, "Go", "Junior")
    #programmer.age = 15
    programmer.info()
    print()


if __name__ == "__main__":
    execute_application()