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
        self.__name = name
        self.__age = age

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Имя: {self.__name} \n"
              f"Возраст: {self.__age}")

    """
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 18:
            self.__age = value
        else:
            raise ErrorSettingAge("Возраст не может быть равен ", value)
    """
class Employee(Person):
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)
        self.__position = position
        self.__salary = salary

    def info(self):
        super().info()
        print(f"Должность: {self.__position} \n"
              f"Зарплата: {self.__salary}")


class Programmer(Employee):
    def __init__(self, name: str, age: int, position: str, salary: float,
                 language: str, level: str ):
        super().__init__(name, age, position, salary)
        self.__language = language
        self.__level = level

    def info(self):
        super().info()
        print(f"Язык: {self.__language} \n"
              f"Уровень: {self.__level} \n")


def execute_application():
    person = Person("Вася", 34)
    #person.age = 6
    person.info()
    print()

    employee = Employee("Петя", 45, "Менеджер", 50000)
    employee.info()
    print()

    programmer = Programmer("Иван", 36, "Программист", 160000, "Go", "Junior")
    programmer.info()
    print()


if __name__ == "__main__":
    execute_application()