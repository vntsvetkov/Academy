from model import Model
from view import View
from controller import Controller

"""
MVC (model-view-controller) - схема разделения данных приложения и 
управляющей логики на 3 отдельных компонента таким образом, что
модификация каждого компонента выполняется независимо
"""


def execute_application():
    model = Model()
    controller = Controller(model)
    view = View(model, controller)

    """ Сценарий 1. Вывести пользователю все статьи подряд """
    controller.get_articles()


if __name__ == "__main__":
    execute_application()
