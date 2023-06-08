""" Responsibility """


class Account:
    successor = None
    name = None

    def __init__(self, balance):
        self.balance = balance

    def can_pay(self, amount):
        return self.balance >= amount

    def set_next(self, account):
        self.successor = account

    def pay(self, amount):
        if self.can_pay(amount):
            print(f"Оплата совершена картой {self.name}")
        elif self.successor is not None:
            self.successor.pay(amount)
        else:
            raise Exception("Недостаточно средств...")


class CardA(Account):
    name = "A"


class CardB(Account):
    name = "B"


class CardC(Account):
    name = "C"


if __name__ == '__main__':
    card_a = CardA(100)
    card_b = CardB(300)
    card_c = CardC(500)

    card_a.set_next(card_b)
    card_b.set_next(card_c)

    card_a.pay(700)

    