from article import Article


class Model:

    @staticmethod
    def get_articles_from_db():
        # Делаем запрос к БД
        art1 = Article()
        art1.title = "Статья 1"
        art1.author = "Автор 1"
        art1.description = "Описание 1"
        articles = [art1]
        return articles

