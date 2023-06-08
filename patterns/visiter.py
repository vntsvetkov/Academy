

class Car:

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color


class CarVisiter:
    __path: str

    def create_car_info(self, car: Car):

        name = car.get_name()
        color = car.get_color()

        # Записать в файл
        self.__path = "car.txt"

    def get_car_info(self):
        return self.__path