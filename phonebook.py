import sqlite3


class Entry:
    def __init__(self, name, surname, phone, city, street):
        # вместо полей сделать словарь
        self.name = name
        self.surname = surname
        self.phone = phone
        self.city = city
        self.street = street

    @classmethod
    def from_json(cls, path: str):
        pass

    @classmethod
    def from_txt(cls, path: str):
        pass

    def get_tuple_entry(self) -> tuple:
        # Преобразование словаря к кортежу
        return self.name, self.surname, self.phone, self.city, self.street


class DBSingleton:
    __connection: sqlite3.Connection = None

    @classmethod
    def connect(cls, path):
        if not cls.__connection:
            cls.__connection = sqlite3.connect(path)
        return cls.__connection


class DBPhonebook:

    __connection: sqlite3.Connection = None
    __cursor: sqlite3.Cursor = None

    def connect(self, path: str):
        self.__connection = sqlite3.connect(path)

    def create_cursor(self):
        self.__cursor = self.__connection.cursor()

    def create_table(self, path: str):
        # можно проверить существование файла
        with open(path, 'r') as sqlite_file:
            sql_script = sqlite_file.read()

        if self.__cursor is not None:
            self.__cursor.executescript(sql_script)

    def add_entry(self, data: tuple):
        if self.__cursor is not None:
            self.__cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city, street)
                                        VALUES(?, ?, ?, ?, ?)""", data)
            self.__connection.commit()
            print("Запись добавлена")

    def add_list_entry(self, data: list[tuple]):
        pass

    def get_data(self) -> list[tuple]:
        if self.__cursor is not None:
            sql_request = """ SELECT * FROM Contacts """
            self.__cursor.execute(sql_request)
            # return self.__cursor.fetchone()
            return self.__cursor.fetchall()

    def close_connection(self):
        self.__connection.close()

    def close_cursor(self):
        self.__cursor.close()

    def __del__(self):
        self.__connection.close()


class Phonebook:

    __data: list[Entry] = []

    @classmethod
    def create_from_execute(cls, data: list[tuple]):
        # конвертация из list[tuple] в объект list[Entry]
        pass

    def add_entry(self, entry: Entry):
        pass

    def delete_entry(self):
        pass

    def update_entry(self):
        pass

    def get_data(self):
        return self.__data

