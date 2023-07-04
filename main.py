import sqlite3
from sqlite3 import Error
from prettytable import from_db_cursor

"""
Написать приложение 'Телефонный справочник'.
Организовать взаимодействие с БД
БД содержит одну таблицу contacts
Таблица contacts хранит ФИО, номер телефона, город
Установить - SimpleSqliteBrowser
"""


def database_connect(path: str) -> sqlite3.Cursor:
    connection = sqlite3.connect(path)
    print("Соединение установлено")
    cursor = connection.cursor()
    return cursor


def create_table(cursor, sql_request: str):
    try:
        cursor.execute(sql_request)
    except Error as e:
        print(e)
    else:
        print(f"Таблица создана")


def database_close(cursor):
    cursor.close()
    print("Соединение завершено")


def execute_application():
    # Способ 1
    '''
    # Подключиться к БД
    cursor = database_connect('phonebook.db')
    # Создать таблицу
    sql_request = f""" CREATE TABLE IF NOT EXISTS Contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            city TEXT
        ); """
    create_table(cursor, sql_request)
    # Закрыть БД
    database_close(cursor)
    '''

    # Способ 2. Выполнение запросов через with
    '''
    connection = sqlite3.connect('phonebook.db')
    with connection:
        cursor = connection.cursor()
        sql_request = f""" CREATE TABLE IF NOT EXISTS Contacts (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     surname TEXT NOT NULL,
                     phone TEXT NOT NULL UNIQUE,
                     city TEXT
                 ); """
        cursor.execute(sql_request)
    '''
    # Добавить данные

    # connection = sqlite3.connect('phonebook.db')
    # with connection:
    #     cursor = connection.cursor()
    #     sql_request = """ INSERT INTO Contacts (name, surname, phone, city)
    #                       VALUES
    #                       ('Paul', 'Jones', '456-678', 'New York'),
    #                       ('Alen', 'Delone', '458-478', 'Los Angeles'),
    #                       ('Teddy', 'Shark', '358-491', 'New York')
    #     """
    #     try:
    #         cursor.execute(sql_request)
    #         '''
    #         cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
    #                             VALUES({0}, {1}, {2}, {3})
    #                             """.format('Paul', 'Jones', '456-678', 'New York'))
    #         '''
    #         '''
    #         cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
    #                             VALUES(?, ?, ?, ?)""", ('Paul', 'Jones', '456-678', 'New York'))
    #         '''
    #         '''
    #         cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
    #                             VALUES(:name, :surname, :phone, :city)""", {'name': 'Paul', 'surname': 'Jones', 'phone': '456-678', 'city': 'New York'})
    #         '''
    #     except Error as e:
    #         print(e)

    # Выполнить запрос на извлечение данных
    connection = sqlite3.connect('phonebook.db')
    with connection:
        cursor = connection.cursor()
        sql_request = """ SELECT * FROM Contacts """
        try:
            cursor.execute(sql_request)
        except Error as e:
            print(e)
        else:
            data = cursor.fetchall() # список кортежей

            # Записать data в другую таблицу
            # Подключится к другой БД
            # Выполнить запрос на добавление в таблицу
            # with other_connection:
                # other_cursor = other_connection.cursor()
                # sql_req = """ Запрос на ставку данных с кортежем """
                # other_cursor.executemany(sql_req, data)

            for record in data:
                 print(record)
            # my_table = from_db_cursor(cursor)
            # print(my_table)


if __name__ == "__main__":
    execute_application()