import json


class Author:
    def __init__(self, name: str, surname: str, year: int):
        self.name = name
        self.surname = surname
        self.year = year

    def __str__(self):
        return f"{self.name} {self.surname} {self.year}"


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


if __name__ == "__main__":
    author = Author("Александр", "Пушкин", 1799)
    x = JSONAuthorAdapter.to_json(author)
    print(x)
    y = JSONAuthorAdapter.from_json(x)
    print(y)