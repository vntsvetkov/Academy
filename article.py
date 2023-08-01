""" Тут можно применить паттерн Builder """


class Article:
    title: str
    author: str
    date: str
    themes: list[str]
    description: str

    def __str__(self):
        return f"{self.title} \n" \
               f"{self.author} \n" \
               f"{self.description}"
