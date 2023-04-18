""" День 10. Взаимодействие между классами"""
import copy
"""
3 способа взаимодействия между классами:
    1. Наследование.
    2. Ассоциация. Это когда один класс включает в себя 
    другой класс в качестве полей. 
    
        2.1. Композиция - это способ когда объект A не существует отдельно от 
        объекта B. Объект A создается при создании объекта B.

class Engine:
    def __init__(self, power: int):
        self.__power = power

    @property
    def power(self):
        return self.__power


class Car:
    def __init__(self):
        self.__engine = Engine(100)

    @property
    def engine(self):
        return self.__engine

#car = Car()
#print(f"Мощность автомобиля: {car.engine.power}")

"""

"""

    2.2. Агрегация - это способ когда экземпляр класса A создается где-то
    в другом месте кода и передается параметром в класс B.
    
    Dependency Injection (Внедрение зависимостей)
    Способы внедрения зависимостей:
        1. Через метод инициализации (конструктор класса)
        2. Через метод установки (сеттер)
        3. Через метод класса
"""


class Engine:
    def __init__(self, power: int):
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        self.__power = value


class Car:
    def __init__(self, engine: Engine):         # метод инициализации
        self.__engine = copy.copy(engine)

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine: Engine):       # метод установки
        self.__engine = copy.copy(engine)


class Racer:
    def __init__(self, car: Car):
        self.__car = copy.deepcopy(car)

    @property
    def car(self):
        return self.__car


class CarSrvice:
    @staticmethod
    def change_engine(car: Car, power: int):
        car.engine = Engine(power)


def execute_application():
    engine = Engine(100)
    car = Car(engine)
    print(f"Мощность двигателя автомобиля: {car.engine.power}")
    car.engine.power = 200
    print(f"Мощность двигателя автомобиля: {car.engine.power}")
    racer = Racer(car)
    print(f"Мощность старого двигателя автомобиля гонщика: {racer.car.engine.power}")
    CarSrvice.change_engine(racer.car, 1000)
    print(f"Мощность нового двигателя автомобиля гонщика: {racer.car.engine.power}")


if __name__ == "__main__":
    execute_application()