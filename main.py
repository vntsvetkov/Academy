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


def database_connect(path: str) -> sqlite3.Connection:
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(e)
    else:
        print("Соединение установлено")
        return connection


def create_table(cursor, sql_request: str):
    cursor.execute(sql_request)
    print(f"Таблица создана")


def execute_application():

    # Задача 1. Создать таблицу
    # Способ 1. Выполнение запросов через открытие/закрытие

    # Подключиться к БД
    connection = database_connect('phonebook.db')
    cursor = connection.cursor()

    # Создать таблицу
    sql_request = f""" CREATE TABLE IF NOT EXISTS Contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            city TEXT
        ); """
    try:
        create_table(cursor, sql_request)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        # Закрыть БД
        connection.close()
        print("Соединение завершено")

    # Способ 2. Выполнение запросов через with

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
        cursor.close()

    # Задача 2. Добавить данные в таблицу
    # Способ 1. Через открытие/закрытие и commit

    connection = database_connect('phonebook.db')
    cursor = connection.cursor()

    sql_request = """ INSERT INTO Contacts (name, surname, phone, city)
                               VALUES
                               ('Paul', 'Jones', '456-678', 'New York'),
                               ('Alen', 'Delone', '458-478', 'Los Angeles'),
                               ('Teddy', 'Shark', '358-491', 'New York')
    """
    try:
        cursor.execute(sql_request)
    except Error as e:
        print(e)
    finally:

        connection.commit()  # зафиксировать изменения в БД перед закрытием подключения.
        # Выполняется, если в БД происходят изменения без использования with
        cursor.close()
        connection.close()
        print("Соединение завершено")

    # Способ 2. Через with

    connection = sqlite3.connect('phonebook.db')
    with connection:
        cursor = connection.cursor()
        sql_request = """ INSERT INTO Contacts (name, surname, phone, city)
                          VALUES
                          ('Paul', 'Jones', '456-678', 'New York'),
                          ('Alen', 'Delone', '458-478', 'Los Angeles'),
                          ('Teddy', 'Shark', '358-491', 'New York')
        """
        try:
            cursor.execute(sql_request)
            # Варианты выполнения запросов на добавление
            '''
            1. 
            cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
                                VALUES({0}, {1}, {2}, {3})
                                """.format('Paul', 'Jones', '456-678', 'New York'))
            '''
            '''
            2. 
            cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
                                VALUES(?, ?, ?, ?)""", ('Paul', 'Jones', '456-678', 'New York'))
            '''
            '''
            3. 
            cursor.execute(f""" INSERT INTO Contacts (name, surname, phone, city)
                                VALUES(:name, :surname, :phone, :city)""", 
                                {'name': 'Paul', 'surname': 'Jones', 'phone': '456-678', 'city': 'New York'})
            '''
        except Error as e:
            print(e)
        finally:
            cursor.close()

    # Задание 3. Выполнить запрос на извлечение данных
    connection = sqlite3.connect('phonebook.db')
    with connection:
        cursor = connection.cursor()
        sql_request = """ SELECT * FROM Contacts """
        try:
            cursor.execute(sql_request)
        except Error as e:
            print(e)
        else:
            data = cursor.fetchall()  # список кортежей
            # data = cursor.fetchone() # Итератор, возвращающий очередной кортеж выборки
            # data = cursor.fetchmany(size=3) # Итератор, возвращающий size элементов выборки в виде списка кортежей

            # Подзадача 3.1. Записать data в другую таблицу
            # Подключится к другой БД
            # Выполнить запрос на добавление в таблицу
            # with other_connection:
            #       other_cursor = other_connection.cursor()
            #       sql_req = """ Запрос на ставку данных с кортежем """
            #       other_cursor.executemany(sql_req, data)

            for record in data:
                print(record)

            # Вывод с использованием prettytable
            my_table = from_db_cursor(cursor)
            print(my_table)
        finally:
            cursor.close()

    # Задание 4. Получить информацию о всех полях таблицы
    connection = sqlite3.connect('phonebook.db')
    cursor = connection.cursor()
    table_name = "Contacts"
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        fields = cursor.fetchall()
    except Error as e:
        print(e)
    else:
        print(fields)
    finally:
        cursor.close()
        connection.close()
        print("Соединение завершено")


if __name__ == "__main__":
    execute_application()
