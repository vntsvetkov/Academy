""""""
""" Принципы проектирования классов SOLID
1. Принцип единственной ответственности
У каждого класса должна быть только одна «ответственность» 
и он не должен брать на себя другие обязанности.

2. Принцип открытости/закрытости
Классы должны быть открыты для расширения, но закрыты для изменений
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
        return f"В эфире радио {self.__station}"


class MixinRadio:

    def play_radio(self, radio: Radio):
        print(radio.play())


class MobilePhone(MixinRadio):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color


class Car(MixinRadio):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color

    def __str__(self):
        return f"Марка: {self.__brand} год: {self.__year} цвет: {self.__color}"


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


def execute_application():
    car = Car("BMW", 2005, "black")
    radio = Radio("Авто радио")
    car.play_radio(radio)

    mobile_phone = MobilePhone("Iphone 14", 2023, "white")
    radio.station = "Европа +"
    mobile_phone.play_radio(radio)


if __name__ == "__main__":
    execute_application()