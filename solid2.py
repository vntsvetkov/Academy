from abc import ABC, abstractmethod
""" Принципы проектирования классов SOLID Роберта К. Мартина

S – Принцип единственной ответственности (Single Responsibility Principle),

O – Принцип открытости/закрытости (Open‐Closed Principle),

L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

I – Принцип разделения интерфейсов (Interface Segregation Principle),

D – Принцип инверсии зависимостей (Dependency Inversion Principle). """

""" Принцип открытости/закрытости. Классы должны быть открыты для расширения, но закрыты для изменений.
Следование этому принципу гарантирует, что класс определен достаточно, чтобы делать то, что он должен делать. 
Добавление любых дополнительных функций может быть реализовано путем создания новых сущностей, которые расширяют возможности существующего класса 
и добавляют дополнительные функции самим себе. Таким образом можно предотвратить частые и тривиальные изменения в хорошо зарекомендовавшем себя классе низкого уровня. 


Пример 1. Разработать систему скидок в магазине в зависимости от типа скидочной карты покупателя (стандартная, серебряная, золотая, платиновая и т.п.)  

Давайте представим, что у вас есть магазин, и вы даете скидку в 20% для ваших стандартных покупателей используя класс Discount. 
Если бы вы решаете удвоить 20-ти процентную скидку для silver клиентов, вы могли бы изменить класс следующим образом:


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'standart':
            return self.price * 0.2
        if self.customer == 'silver':
            return self.price * 0.4


Этот пример нарушает принцип открытости/закрытости. Например, если мы хотим дать новую скидку для другого типа покупателей, то это потребует добавления новой логики в класс. 
Чтобы следовать данному принципу, мы добавим новый класс, который будет расширять класс Discount.

"""


class Discount:
    def __init__(self, price):
        self._price = price

    @abstractmethod
    def give_discount(self):
        return NotImplementedError


class StandardDiscount(Discount):
    def give_discount(self):
        return self._price * 0.2


class SilverDiscount(Discount):
    def give_discount(self):
        return self._price * 0.4


class GoldenDiscount(Discount):
    def give_discount(self):
        return self._price * 0.6


class PlatinumDiscount(Discount):
    def give_discount(self):
        return self._price * 0.8

"""
Пример 2. Разработать систему отправки оповещений клиенту

Представим, что у нас есть класс NotificationService который представляет собой сервис отправки оповещений. Мы можем отправлять оповещения по email, sms.

class NotificationService:
    def sendMessage(type_message: str, message: str) {
        if (typeMessage == "email"):
            #write email
        if (typeMessage == "sms"):
            #write sms

Этот пример нарушает принцип открытости/закрытости. Например, если мы хотим добавить новый способ оповещений, это потребует добавления новой логики в классе.
Для того чтобы придерживаться принципа открытости/закрытости необходимо спроектировать наш код таким образом, чтобы каждый мог повторно использовать нашу функцию, просто расширив ее.

"""


class NotificationService:
    @abstractmethod
    def send_message(self, message: str):
        return NotImplementedError


class EmailNotification(NotificationService):

    def send_message(self, message: str):
        # TODO: реализовать алгоритм отправки оповещения по email
        pass


class MobileNotification(NotificationService):

    def send_message(self, message: str):
        # TODO: реализовать алгоритм отправки оповещения по sms
        pass


