from article import Article


class View:
    """
    Отвечает за представление данных пользователю.
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
