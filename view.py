from article import Article

""" Например, мы можем создать простое консольное представление для нашего приложения, 
а уже потом добавить красиво оформленный GUI. Причем, остается возможность сохранить оба типа интерфейсов."""


class View:
    """
    Отвечает за отображение данных Модели.
    На этом уровне мы лишь предоставляем интерфейс для взаимодействия пользователя с Моделью.

    """
    def __init__(self, model, controller):
        self.__model = model
        self.__controller = controller
        self.__controller.set_view(self)

    @staticmethod
    def output_articles(articles: list[Article]):
        for article in articles:
            print(article)

    def main(self):
        """ Сценарий 1. Вывести пользователю все статьи подряд """
        self.__controller.get_articles()
