from abc import ABC, abstractmethod


class ProductDeletionError(Exception):
    def __init__(self, text):
        self.__text = text


class BasketState(ABC):

    @staticmethod
    @abstractmethod
    def add(basket, data):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def remove(basket, data):
        raise NotImplementedError


class Basket:
    data: list = []

    def __init__(self, bs: BasketState):
        self.__basket_state = bs

    def get_state(self):
        print(self.__basket_state)

    @property
    def basket_state(self):
        return self.__basket_state

    @basket_state.setter
    def basket_state(self, bs):
        self.__basket_state = bs

    def add(self, data):
        self.__basket_state.add(self, data)

    def remove(self, data):
        self.__basket_state.remove(self, data)


class EmptyBasket(BasketState):

    @staticmethod
    def add(basket: Basket, data):
        basket.data.append(data)
        print(f"В корзине {len(basket.data)} товаров")
        basket.basket_state = FullBasket()

    @staticmethod
    def remove(basket: Basket, data):
        print("Корзина пуста")


class FullBasket(BasketState):

    @staticmethod
    def add(basket: Basket, data):
        basket.data.append(data)
        print(f"В корзине {len(basket.data)} товаров")

    @staticmethod
    def remove(basket: Basket, data):
        basket.data.remove(data)
        if len(basket.data) == 0:
            basket.basket_state = EmptyBasket()
            print("Корзина пуста")
        else:
            raise ProductDeletionError("Не удалось удалить товар из пустой корзины")


if __name__ == '__main__':
    basket = Basket(EmptyBasket())
    basket.add("Футболка")
    basket.get_state()
    basket.add("Шорты")
    basket.get_state()
    basket.remove("Футболка")
    basket.remove("Шорты")
    basket.get_state()
    basket.remove("Футболка")
