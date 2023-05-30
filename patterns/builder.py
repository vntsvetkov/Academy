from abc import ABC, abstractmethod


class Engine(ABC):
    pass


class DieselEngine(Engine):
    pass


class Computer(ABC):
    pass


class ServiceComputer(Computer):
    pass


class Car:
    def __init(self):
        self.engine = None
        self.computer = None
        self.seats = 0


class Builder(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def set_engine(self, engine):
        raise NotImplementedError

    @abstractmethod
    def set_computer(self, computer):
        raise NotImplementedError

    @abstractmethod
    def set_seats(self, count_seats):
        raise NotImplementedError

    @abstractmethod
    def get_car(self):
        raise NotImplementedError


class CarBuilder(Builder):
    __car: Car

    def create(self):
        self.__car = Car()

    def set_engine(self, engine: Engine):
        self.__car.engine = engine

    def set_computer(self, computer: Computer):
        self.__car.computer = computer

    def set_seats(self, count_seats):
        self.__car.seats = count_seats

    def get_car(self):
        return self.__car


if __name__ == "__main__":

    car_builder = CarBuilder()
    car_builder.create()
    car_builder.set_seats(4)
    car_builder.set_engine(DieselEngine())
    car_builder.set_computer(ServiceComputer())
    new_car = car_builder.get_car()
