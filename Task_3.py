class ExpressionConverter:
    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def to_postfix(expression: str) -> list:
        pass

    @staticmethod
    def to_infix(expression: list) -> str:
        pass


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression
