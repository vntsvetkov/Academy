""" Принципы проектирования классов SOLID Роберта К. Мартина

S – Принцип единственной ответственности (Single Responsibility Principle),

O – Принцип открытости/закрытости (Open‐Closed Principle),

L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

I – Принцип разделения интерфейсов (Interface Segregation Principle),

D – Принцип инверсии зависимостей (Dependency Inversion Principle). """

""" Принцип единственной ответственности.  У каждого класса должна быть только одна «ответственность» и он не должен брать на себя другие обязанности.

Пример 1. Требуется разработать телефонный справочник, в котором будет класс TelephoneDirectory. 
Он будет «нести ответственность» за ведение записей справочника, то есть телефонных номеров и названий организаций, которым принадлежат номера. 
Ожидается, что класс будет выполнять следующие операции: 
    - добавлять новую запись (name и phone_number)
    - удалять существующую запись
    - изменять номер телефона
    - выполнять поиск, который будет возвращать номер """


class PhoneDirectory:

    def __init__(self):
        self.__phoneDirectory = {}

    def add_entry(self, name, number):
        self.__phoneDirectory[name] = number

    def delete_entry(self, name):
        self.__phoneDirectory.pop(name)

    def update(self, name, number):
        self.__phoneDirectory[name] = number

    def get_number(self, name):
        return self.__phoneDirectory[name]


"""
А теперь предположим, что в проекте есть еще требование:  сохранить/загрузить содержимое справочника в файл. 
Добавив функцию сохранения в файл в класс PhoneDirectory, класс берет на себя дополнительные обязанности, которые не входят в его основную зону ответственности. 
В будущем, если появятся какие-то требования, связанные с сохранением данных, это может привести к изменениям в классе TelephoneDirectory. 
Получается, что класс TelephoneDirectory подвержен изменениям по причинам, которые не являются его основной ответственностью.
Так мы гарантируем, что у класса TelephoneDirectory есть лишь одна причина для изменения – это изменения в его основной «ответственности».
"""


class FileSystemManagementPhoneDirectory:

    @staticmethod
    def save(phone_directory: PhoneDirectory):
        pass

    @staticmethod
    def load(path: str):
        pass


""" 
Пример 2. Допустим нужно разработать класс CarService и в нем реализовать несколько методов: 
    - найти машину по номеру, 
    - забронировать машину, 
    - распечатать заказ на бронирование
    - получить информацию о машине
    - отправить сообщение о бронировании клиенту.

Необходимо разделить данный класс CarService на несколько, и тем самым, следуя принципу единой ответственности, предоставить каждому классу отвечать только за одну зону или действие.
Так в дальнейшем его будет проще дополнять и модифицировать.

"""


class Car:

    def __init__(self, car_number: str):
        self.__car_number = car_number

    @property
    def car_number(self):
        return self.__car_number


class Client:

    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name


class Order:

    def __init__(self, number: int):
        self.__number = number

    @property
    def number(self):
        return self.__number


class CarService:

    def __init__(self):
        self.__cars = []

    def search(self, car_number: str):
        index = -1
        for index, car in enumerate(self.__cars):
            if car.car_number == car_number:
                return self.__cars[index]

    def order_car(self, car_number: str, client: Client):
        pass


class CarPrintService:
    def print_order(self, order: Order):
        pass


class CarInfoService:
    def car_info(self, car: Car):
        pass


class NotificationService:
    def send_message(self, type_message: str, message: str):
        pass

