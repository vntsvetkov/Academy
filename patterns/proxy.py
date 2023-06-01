from abc import ABC, abstractmethod

class InsufficientFundsError(Exception):
    def __init__(self, text):
        self.__text = text

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        raise NotImplementedError

    @abstractmethod
    def refill(self, amount):
        raise NotImplementedError


class Cash(Payment):
    __count = 0

    def pay(self, amount):
        if self.__count >= amount:
            self.__count -= amount
            print(f"Остаток: {self.__count}")
        else:
            raise InsufficientFundsError("Недостаточно средств")

    def refill(self, amount):
        self.__count += amount
        print(f"Текущий баланс: {self.__count}")


class CardPayment(Payment):

    def __init__(self, payment: Payment):
        self.__payment = payment

    def pay(self, amount):
        self.__payment.pay(amount)

    def refill(self, amount):
        self.__payment.refill(amount)


if __name__ == "__main__":
    card = CardPayment(Cash())
    card.refill(1000)
    card.pay(500)
    card.pay(500)
    card.pay(100)
