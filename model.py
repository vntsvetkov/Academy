from article import Article
from datetime import date
"""  Тут можно реализовать паттерн Стратегия. 
Например, для одного приложения мы можем создать несколько моделей. Одна будет отладочной, а другая рабочей. 
Первая может хранить свои данные в файле, а вторая уже задействует базу данных."""


class Model:
    """ Отвечает за внутреннюю логику работы программы.
    Здесь мы можем скрыть способы хранения данных, а также правила и алгоритмы обработки информации."""

    @staticmethod
    def get_articles_from_db():
        articles = Article.select().where(Article.date == "2023-08-02")

        return articles

    @staticmethod
    def add_article(article: tuple):
        title, author, date_, description = article
        Article.create(title=title,
                       author=author,
                       date=date_,
                       description=description
                       )

