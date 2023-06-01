from abc import ABC, abstractmethod


class DescriptionProduct(ABC):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_price(self):
        raise NotImplementedError


class Product(DescriptionProduct):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class CompositeProduct(DescriptionProduct):

    def __init__(self, name):
        self.__name = name
        self.__products = []

    @property
    def products(self):
        return self.__products

    def add(self, product: DescriptionProduct):
        self.__products.append(product)

    def remove(self, product: DescriptionProduct):
        self.__products.remove(product)

    def clear(self):
        self.__products = []

    def get_name(self):
        return self.__name

    def get_price(self):
        price = 0
        for p in self.__products:
            price += p.get_price()
        return price


class Box(CompositeProduct):
    def __init__(self, name):
        super(Box, self).__init__(name)

    def get_price(self):
        price = 0
        for p in self.products:
            price += p.get_price()
        return price


if __name__ == "__main__":

    p1 = Product("Ipad", 50000)

    c_p1 = CompositeProduct("Инструменты для сверления")
    c_p1.add(Product("Дрель", 5000))
    c_p1.add(Product("Шуруповерт", 7000))

    c_p2 = CompositeProduct("Слесарные инструменты")
    c_p2.add(Product("Молоток", 500))
    c_p2.add(Product("Ножовка", 700))

    c_p3 = CompositeProduct("ИНструменты")
    c_p3.add(c_p1)
    c_p3.add(c_p2)

    box = Box("Посылка")
    box.add(p1)
    box.add(c_p3)

    print(box.get_price())

