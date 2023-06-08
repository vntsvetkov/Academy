from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass


class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y


class Multiplicator(BaseStrategy):
    def do_work(self, x, y):
        return x * y


class Calculator:

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))


if __name__ == '__main__':
    calc = Calculator()
    calc.set_strategy(Adder())
    calc.calculate(1, 2)

    calc.set_strategy(Multiplicator())
    calc.calculate(1, 4)

