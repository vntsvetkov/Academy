import copy
"""
Реализовать класс Книга, Автор, Читатель, [Бибилиотека]
Описать требуемые зависимости
Протестировать функциональность:
    - Создать книгу
    - Создать читателя
    - Выдать читателю книгу
    - Поменять читателю книгу
"""


class FoundBookError(Exception):
    def __init__(self, text: str):
        self.__text = text


class Author:
    def __init__(self, name: str, surname: str, year: int):
        self.__name = name
        self.__surname = surname
        self.__year = year

    def __str__(self):
        return f"{self.__name} {self.__surname} {self.__year}"

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

class Book:
    def __init__(self, name: str, genre: str, pages: int, author: Author):
        self.__name = name
        self.__genre = genre
        self.__pages = pages
        self.__author = author

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"(Название: {self.__name}, автор: {self.__author})"


class LibraryReader:
    def __init__(self, name: str, ticket: int):
        self.__name = name
        self.__ticket = ticket
        self.__book = list()

    @property
    def book(self):
        return self.__book

    @property
    def name(self):
        return self.__name

    def take_book(self, book: Book):
        self.__book.append(book)

    def give_book(self, name: str):
        # TODO: реализовать метод возвращения книги
        for index, book in enumerate(self.__book):
            if book.name == name:
                return self.__book.pop(index)
        raise FoundBookError(f"У пользователя отсутствует книга {name}")


class Library:
    # Список книг
    # Список читателей
    # Выдать читателю кнгигу
    # Принять у читателя книгу
    # Удалить/добавить нового читателя
    # Удалить/добавить новую книгу
    pass