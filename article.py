from peewee import *

db = SqliteDatabase('articles.db')


class Article(Model):

    class Meta:
        database = db

    title = CharField()
    author = CharField()
    date = DateField()
    description = TextField()

    def __str__(self):
        return f"{self.title} \n" \
               f"{self.author} \n" \
               f"{self.description}"
