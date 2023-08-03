from article import Article, db
import datetime

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
        db.connect()

    @staticmethod
    def output_articles(articles):
        for article in articles:
            print(article)

    def main(self):
        """ Сценарий 1. Вывести пользователю все статьи подряд """
        self.__controller.get_articles()
        """ Сценарий 2. Добавить новую статью """
        # title = "Как стать тимлидом?"
        # author = "Alexy Pirogov"
        # description = "Всем привет! Я Александр Яковлев, в Тинькофф руковожу " \
        #               "разработкой бизнес-линии в нефинансовых сервисах " \
        #               "Расскажу, чем занимаются тимлиды у нас в компании " \
        #               "и что делать, чтобы вырасти до тимлида, а еще " \
        #               "пройдусь по распространенным заблуждениям о работе. "
        #
        # date = datetime.date.today()
        # article = title, author, date, description
        # self.__controller.add_article(article)

    def __del__(self):
        db.close()

