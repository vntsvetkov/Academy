from abc import ABC, abstractmethod
from enum import Enum
""" Принципы проектирования классов SOLID
1. Принцип единственной ответственности
У каждого класса должна быть только одна «ответственность» 
и он не должен брать на себя другие обязанности.

2. Принцип открытости/закрытости
Классы должны быть открыты для расширения, но закрыты для изменений

3. Принцип подстановки Барбары Лисков
Объекты в программе должны быть заменяемы экземплярами их подтипов 
без ущерба корректности работы программы

4. Принцип разделения интерфейса

5. Принцип инверсии зависимостей
obj.capacity
"""


class Radio:
    def __init__(self, station: str):
        self.__station = station

    @property
    def station(self):
        return self.__station

    @station.setter
    def station(self, station):
        self.__station = station

    def play(self):
        return f"Вы слушаете {self.__station}"


class MixinRadio:
    @staticmethod
    def turn_radio(radio: Radio):
        print(radio.play())


class MobilePhone(MixinRadio):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color


class Power:
    LOWER = 100
    MEDIUM = 150
    TOP = 200
    MAX = 300


class Car(MixinRadio):
    def __init__(self, brand: str, year: int, color: str, power: int):
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power
        self.__capacity = {}

    def __str__(self):
        return f"Марка: {self.__brand} год: {self.__year} цвет: {self.__color}"

    @property
    def power(self):
        return self.__power

    def get_capacity(self):
        return self.__capacity
    def set_capacity(self, place, trunk):
        self.__capacity = {"Количество мест": place, "Объем багажника": trunk}


class SUV(Car):
    pass


class Sedan(Car):
    pass


class NalogCalculation(ABC):
    @abstractmethod
    def get_nalog(self):
        pass

class NalogCalculationLower(NalogCalculation):
    def __init__(self, power: int):
        self.__power = power

    def get_nalog(self):
        return self.__power * 2.5

class NalogCalculationMedium(NalogCalculation):
    def __init__(self, power: int):
        self.__power = power

    def get_nalog(self):
        return self.__power * 3.5



class FileManagementCar:
    @staticmethod
    def save(car: Car, path: str):
        pass

    @staticmethod
    def load(path: str):
        pass


class DBManagementCar:
    @staticmethod
    def save(car: Car, name: str):
        pass

    @staticmethod
    def load(name: str) -> Car:
        pass


def print_capacity_car(obj):
    capacity = obj.get_capacity()
    for key in capacity.keys():
        print(key, capacity[key])


def get_nalog(power: int):
    if power < Power.LOWER:
        return NalogCalculationLower(power).get_nalog()
    elif Power.LOWER <= power < Power.MEDIUM:
        return NalogCalculationMedium(car.power).get_nalog()


def execute_application():
    radio = Radio("Авто-радио")

    mobile_phone = MobilePhone("Iphone 14", 2023, "white")
    mobile_phone.turn_radio(radio)

    car = Car("BMW", 2005, "black", 80)
    car.turn_radio(radio)
    print(get_nalog(car.power))


    suv = SUV("Jeep", 2010, "red", 160)
    sedan = Sedan("KIA", 2020, "gray", 105)
    car.set_capacity(4, 500)
    suv.set_capacity(6, 1000)
    sedan.set_capacity(4, 300)
    print_capacity_car(car)
    print_capacity_car(sedan)
    print_capacity_car(suv)


if __name__ == "__main__":
    execute_application()