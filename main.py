"""День 8. Принципы SOLID"""
from abc import ABC, abstractmethod
from copy import copy, deepcopy
from MagicMethods import Point
"""
4. Принцип разделения интерфейса
Ни один класс не должен зависеть от методов, которые он не использует.

Задача 1. Определить классы для создания устройства, которое может печатать,
сканировать, копировать документы.

"""


class CallingDevice(ABC):
    @abstractmethod
    def make_calls(self):
        pass


class MessagingDevice(ABC):
    @abstractmethod
    def send_messages(self):
        pass


class InternetDevice(ABC):
    @abstractmethod
    def connect_internet(self):
        pass


class SmartPhone(CallingDevice, MessagingDevice, InternetDevice):
    def make_calls(self):
        # TODO: реализовать логику совершения звонков
        pass

    def send_messages(self):
        # TODO: реализовать логику отправки сообщений
        pass

    def connect_internet(self):
        # TODO: реализовать логику подключения к интернету
        pass


class MobilePhone(CallingDevice, MessagingDevice):
    def make_calls(self):
        # TODO: реализовать логику совершения звонков
        pass

    def send_messages(self):
        # TODO: реализовать логику отправки сообщений
        pass


class StationaryPhone(CallingDevice):
    def make_calls(self):
        # TODO: реализовать логику совершения звонков
        pass


"""
5. Принцип инверсии зависимостей
Модуль высокого уровня не должен зависеть от модулей низкого уровня. 
И то, и другое должно зависеть от абстракций. 

Задача 2. Создать систему оплаты для магазина.

"""


class Payment(ABC):
    @abstractmethod
    def do_transaction(self, amount: float):
        pass


class Cash(Payment):
    def do_transaction(self, amount: float):
        # TODO: реализовать логику сделки по наличному расчету
        print(f"Проведена оплата наличными: {amount} руб.")
        pass


class Card(Payment):
    def do_transaction(self, amount: float):
        # TODO: реализовать логику сделки по банковской карте
        print(f"Проведена оплата по банковской карте: {amount} руб.")
        pass


class Remittance(Payment):
    def do_transaction(self, amount: float):
        # TODO: реализовать логику сделки по онлайн-переводу
        print(f"Проведена оплата онлайн-переводом: {amount} руб.")
        pass


class Shop:

    def __init__(self, payment: Payment):
        self.__payment = copy(payment)

    def do_payment(self, amount: float):
        self.__payment.do_transaction(amount)


def execute_application():

    point1 = Point(1, 2)
    point2 = Point(1, 2)
    print(hash(point1))
    print(hash(point2))
    print(point1 == point2)


if __name__ == "__main__":
    execute_application()