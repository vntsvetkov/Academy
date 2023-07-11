import sqlite3


class Entry:
    def init(self, name, surname, phone, city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.city = city

    @classmethod
    def from_json(cls, path: str):
        pass

    @classmethod
    def from_txt(cls, path: str):
        pass


class DBPhonebook:

    __connection: sqlite3.Connection = None
    __cursor: sqlite3.Cursor = None

    def connect(self, path: str):
        self.__connection = sqlite3.connect(path)

    def create_cursor(self):
        self.__cursor = self.__connection.cursor()

    def add_entry(self):
        pass

    def close_connection(self):
        self.__connection.close()

    def close_cursor(self):
        self.__cursor.close()

    def __del__(self):
        self.__connection.close()


class Phonebook:

    __data: list[Entry] = []

    def add_entry(self, entry: Entry):
        pass

    def delete_entry(self):
        pass

    def update_entry(self):
        pass

    def get_data(self):
        return self.__data