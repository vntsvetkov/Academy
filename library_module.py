import copy
from abc import abstractmethod
import json

class FoundBookError(Exception):
    def __init__(self, text: str):
        self.__text = text


class SearchingElements:
    @abstractmethod
    def get_objects(self):
        raise NotImplementedError


class Author:
    def __init__(self, name: str, surname: str, year: int):
        self.__name = name
        self.__surname = surname
        self.__year = year

    def __str__(self):
        return f"{self.__name} {self.__surname} {self.__year}"

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.__name == other.__name and \
                   self.__surname == other.__surname and \
                   self.__year == other.__year

        raise TypeError(f"Невозможно сравнить с объектом {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__name, self.__surname, self.__year))


class Book:
    def __init__(self, name: str, genre: str, pages: int, author: Author):
        self.__name = name
        self.__genre = genre
        self.__pages = pages
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def genre(self):
        return self.__genre

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    def __str__(self):
        return f"Название: {self.__name}, жанр: {self.__genre}, автор: {self.__author}"


class LibraryReader(SearchingElements):
    def __init__(self, name: str, ticket: int):
        self.__name = name
        self.__ticket = ticket
        self.__books = list()

    @property
    def book(self):
        return self.__books

    @property
    def name(self):
        return self.__name

    def take_book(self, book: Book):
        self.__books.append(book)

    def give_book(self, name: str):
        # TODO: реализовать метод возвращения книги
        for index, book in enumerate(self.__books):
            if book.name == name:
                return self.__books.pop(index)
        raise FoundBookError(f"У пользователя отсутствует книга {name}")

    def get_objects(self):
        for book in self.__books:
            yield book


class Library(SearchingElements):
    def __init__(self, name: str):
        self.__name = name
        self.__books = list()
        self.__readers = list()

    @property
    def books(self):
        return self.__books

    def add_book(self, book: Book):
        self.__books.append(copy.deepcopy(book))

    def del_book(self, name: str):
        for index, book in enumerate(self.__books):
            if book.name == name:
                self.__books.pop(index)
                return
        raise FoundBookError(f"В библиотеке отсутствует книга {name}")

    def print_books(self):
        for index, book in enumerate(self.__books, start=1):
            print(index, book)

    def get_objects(self):
        for book in self.__books:
            yield book


    # TODO: реализовать метод "Выдать читателю книгу"
    # TODO: реализовать метод "Принять у читателя книгу"
    # TODO: реализовать методы по удалению/добавлению нового читателя


class FilterLibrary:
    @staticmethod
    @abstractmethod
    def get_books(self, library: Library):
        raise NotImplementedError


class GenreFilterBooksLibrary(FilterLibrary):
    @staticmethod
    def get_books(library: Library, genre: str):
        books = library.get_objects()
        for book in books:
            if book.genre == genre:
                yield book


class AuthorFilterBooksLibrary(FilterLibrary):
    @staticmethod
    def get_books(library: Library, author: Author):
        books = library.get_objects()
        for book in books:
            if book.author == author:
                yield book


class AuthorJSONConverter:
    @staticmethod
    def to_dict(author: Author) -> dict:
        if isinstance(author, Author):
            result = author.__dict__
            result["className"] = author.__class__.__name__
            return result


class TestEncoder(json.JSONEncoder):
    def default(self, other):
        return {"Name": other.name, "Surname": other.surname, "Year": other.yaer, "className": other.__class__.__name__}


class JSONAuthorAdapter:
     @staticmethod
     def to_json(author: Author):
         if isinstance(author, Author):
             return json.dumps({
                 "name": author.name,
                 "surname": author.surname,
                 "year": author.year,
             })

     @staticmethod
     def from_json(data):
         obj = json.loads(data)

         try:
             return Author(obj["name"], obj["surname"], obj["year"])
         except AttributeError as e:
             print(e)


class JSONBookAdapter:
    @staticmethod
    def to_json(book: Book):
        if isinstance(book, Book):
            return json.dumps({
                "name": book.name,
                "genre": book.genre,
                "pages": book.pages,
                "author": {"name": book.author.name, "surname": book.author.surname, "year": book.author.year},
            })
    @staticmethod
    def from_json(data):
        obj = json.loads(data)

        try:
            return Book(obj["name"], obj["genre"], obj["pages"], Author(obj["author"]["name"], obj["author"]["surname"], obj["author"]["year"]))
        except AttributeError as e:
            print(e)
