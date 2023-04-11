"""День 8. Принципы SOLID"""
from abc import ABC, abstractmethod
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


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()