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


def check_phone(cursor, phone: str, table: str) -> bool:
    cursor.execute(f"""SELECT * FROM {table} WHERE phone = ?""", (phone, ))

    return cursor.fetchall() == []


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
        for field in fields:
            print(field[1])
    finally:
        cursor.close()
        connection.close()
        print("Соединение завершено")

    # Задача 5. Удаление строки данных из таблицы
    connection = sqlite3.connect('phonebook.db')
    cursor = connection.cursor()
    table_name = "Contacts"
    city = input("Введите название города: ")
    try:
        # Cделать выборку по введнному city
        # sql_request = f""" SELECT * FROM {table_name}
        #                    WHERE city = ?
        #                     """
        # cursor.execute(sql_request, (city, ))
        # data = cursor.fetchall()
        # Подключиться к резервной базе и добавить туда

        sql_request = f""" DELETE FROM {table_name} 
                           WHERE city = ?
                       """
        cursor.execute(sql_request, (city,))
    except Error as e:
        print(e)
    else:
        print("Запрос на удаление выполнен")
    finally:
        connection.commit()
        cursor.close()
        connection.close()

    # Задача 6. Обновление данных. Поменять номер телефона пользователя
    connection = sqlite3.connect('phonebook.db')
    cursor = connection.cursor()
    table_name = "Contacts"
    last_phone = "456-678"
    new_phone = input("Введите новый номер: ")

    if check_phone(cursor, new_phone, table_name):

        try:
            sql_request = f""" UPDATE {table_name}
                               SET phone = ?
                               WHERE phone = ? 
                           """
            cursor.execute(sql_request, (new_phone, last_phone))
        except Error as e:
            print(e)
        else:
            print("Номер телефона изменен")
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    else:
        print("Такой номер уже сществует, введите другой")
        cursor.close()
        connection.close()

    # Добавление столбца
    connection = sqlite3.connect('phonebook.db')
    cursor = connection.cursor()
    table_name = "Contacts"
    column_name = "street"
    try:
        sql_request = f"""ALTER TABLE {table_name}
                          ADD COLUMN {column_name} TEXT
                       """
        cursor.execute(sql_request)
    except Error as e:
        print(e)
    else:
        print(f"Столбец {column_name} добавлен")
    finally:
        connection.commit()
        cursor.close()
        connection.close()

    # Выполнение скрипта на добавление таблицы
    sqlite_connection = sqlite3.connect('phonebook.db')
    cursor = sqlite_connection.cursor()
    with open('sqlite_create_tables.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    try:
        cursor.executescript(sql_script)
        print("Скрипт SQLite успешно выполнен")
    except Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        cursor.close()
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

    # Бэкап всей базы

    sqlite_con = sqlite3.connect('phonebook.db')
    backup_con = sqlite3.connect('phonebook_backup.db')
    with backup_con:
        try:
            sqlite_con.backup(backup_con)
            print("Резервное копирование выполнено успешно")
        except Error as error:
            print("Ошибка при резервном копировании: ", error)
        finally:
            backup_con.close()
            sqlite_con.close()


if __name__ == "__main__":
    execute_application()

