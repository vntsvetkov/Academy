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

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

    def info(self):
        print(f"Класс: {self.__class__.__name__} \n"
              f"Имя: {self.__name} \n"
              f"Возраст: {self.__age}")


class Employee(Person):
    _AGE = 18
    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)
        self.__position = position
        self.__salary = salary
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        self.__salary = value

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

    @property
    def age(self):
        return Employee.age.fget(self)
    @age.setter
    def age(self, value):
        if value >= 18:
            Employee.age.fset(self, value)
        else:
            raise ErrorSettingAge(f"Возраст сотрудника должен быть больше либо равен", Employee._AGE)
    def info(self):
        super().info()
        print(f"Язык: {self.__language} \n"
              f"Уровень: {self.__level} \n")


def execute_application():
    person = Person("Вася", 34)
    person.info()
    print()

    employee = Employee("Петя", 45, "Менеджер", 50000)
    employee.info()
    print()

    programmer = Programmer("Иван", 36, "Программист", 160000, "Go", "Junior")
    #programmer.age = 20
    programmer.info()
    print()


if __name__ == "__main__":
    execute_application()