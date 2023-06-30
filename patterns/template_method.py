import time
from abc import ABC, abstractmethod


class DataParser:

    def data_parse(self):
        self.open_file()
        self.get_data()
        self.parse_data()
        self.save_data()
        self.close_file()

    @abstractmethod
    def open_file(self):
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
    def parse_data(self):
        raise NotImplementedError

    @abstractmethod
    def save_data(self):
        raise NotImplementedError

    @abstractmethod
    def close_file(self):
        raise NotImplementedError


class DocDataParser(DataParser):

    def open_file(self):
        print("Выполняется метод 1 класса ", self.__class__.__name__)
        time.sleep(1)

    def get_data(self):
        print("Выполняется метод 2 класса ", self.__class__.__name__)
        time.sleep(1)

    def parse_data(self):
        print("Выполняется метод 3 класса ", self.__class__.__name__)
        time.sleep(1)

    def save_data(self):
        print("Выполняется метод 4 класса ", self.__class__.__name__)
        time.sleep(1)

    def close_file(self):
        print("Выполняется метод 5 класса ", self.__class__.__name__)
        time.sleep(1)


class PDFDataParser(DataParser):

    def open_file(self):
        print("Выполняется метод 1 класса ", self.__class__.__name__)
        time.sleep(1)

    def get_data(self):
        print("Выполняется метод 2 класса ", self.__class__.__name__)
        time.sleep(1)

    def parse_data(self):
        print("Выполняется метод 3 класса ", self.__class__.__name__)
        time.sleep(1)

    def save_data(self):
        print("Выполняется метод 4 класса ", self.__class__.__name__)
        time.sleep(1)

    def close_file(self):
        print("Выполняется метод 5 класса ", self.__class__.__name__)
        time.sleep(1)


if __name__ == '__main__':
    a = DocDataParser()
    b = PDFDataParser()

    a.data_parse()

    b.data_parse()

